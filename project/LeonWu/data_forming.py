import numpy as np
import sys
import pandas as pd
import difflib
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

canada_chain_url="https://en.wikipedia.org/wiki/List_of_Canadian_restaurant_chains#Major_chains"   # webpage contain all chain resturant in Canada
US_chain_url = "https://en.wikipedia.org/wiki/List_of_restaurant_chains_in_the_United_States"
#international_chain_url = 'https://en.wikipedia.org/wiki/List_of_restaurant_chains#International'


def fetch_wiki_directory(url):
    response=requests.get(url)                                                          #fetch page
    #print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')
    indiatable=', '.join(p.text for p in soup.find_all("li", {"class": "toclevel-2"}))  # return all name from directory separated by ,
    split_data = indiatable.split(',')
    df = pd.DataFrame(split_data, columns =['Name'])
    return df

def fetch_wiki_table(url,fetch_all):
    response=requests.get(url)                                                          #fetch page
    table_class="wikitable sortable jquery-tablesorter"
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup.find_all('table'))
    if fetch_all:
        all_table = soup.find_all('table',{'class':"wikitable sortable"})
        df=pd.read_html(str(all_table))
        all_table=pd.DataFrame(df[0])
        for i in range(len(df)):
            next_table=pd.DataFrame(df[i])
            all_table = pd.concat([all_table, next_table], axis=0)

        all_table = all_table['Name'].reset_index(drop=True)
        return all_table
    else:
        indiatable=soup.find('table',{'class':"wikitable sortable"})

        df=pd.read_html(str(indiatable))
        #print(indiatable)
        df=pd.DataFrame(df[0])
        name = df['Name']
        #print(name.head())
        return name

def chain_resturant_name(df):
    df['chain_resutrant'] = df['Name'].str.extract(r'\d\.\d+ (.*)')
    df['chain_resutrant'][1] = 'A&W'
    df['chain_resutrant'][2] = 'Baton Rouge'
    df['chain_resutrant'][3] = 'BeaverTails'
    #print(df['chain_resutrant'])
    #df.to_csv('check.csv')                   #extract resturant name only


    return df['chain_resutrant']

def user_defined_chain(data,number_of_resturant):
    resturant = data.loc[data['amenity'] == 'restaurant']
    dups_resturant = resturant.pivot_table(index=['name'], aggfunc='size')
#print(dups_resturant.size())
    dups_resturant =dups_resturant.to_frame().reset_index()
    dups_resturant = pd.DataFrame(dups_resturant)
    dups_resturant['count'] = dups_resturant.iloc[:, 1]
    dups_resturant = dups_resturant.sort_values(by=['count'], ascending=False)

    #dups_resturant.to_csv('count.csv')
    dups_resturant = dups_resturant.loc[dups_resturant['count'] > number_of_resturant].reset_index()
    #print(dups_resturant)


    return dups_resturant


def chain_resturant(chain_name,data):
    resturant = data.loc[data['amenity'] == 'restaurant']
    selected = user_defined_chain(data,3)
    selected_chain = resturant.loc[resturant['name'].isin(selected['name'])]
    chain_resturant= resturant.loc[resturant['name'].str.lower().isin(chain_name.str.lower())]
    all_chain = pd.concat([selected_chain, chain_resturant], axis=0)
    all_chain =all_chain.drop_duplicates(subset=['lat','lon','name'])
    non_chain_restruant = resturant.loc[~resturant['name'].str.lower().isin(chain_name.str.lower())]
    #non_chain_restruant.to_csv('non.csv')
    #chain_resturant.to_csv('chain.csv')
    #print(all_chain)
    return all_chain, non_chain_restruant


amenities = pd.read_json("data/amenities-vancouver.json.gz", lines=True)
amenities = amenities[amenities['name'].notna()]
amenities = amenities.reset_index(drop=True)
amenities.to_csv('data/all_restaurant.csv')

content= fetch_wiki_directory(canada_chain_url)
US_chain_name = fetch_wiki_table(US_chain_url,True)
#international_chain_name = fetch_wiki_table(international_chain_url,False)
canada_chain_name = chain_resturant_name(content)

all_chain_name = pd.concat([US_chain_name, canada_chain_name], axis=0)
all_chain_name = all_chain_name.drop_duplicates()
all_chain_name = all_chain_name.reset_index(drop=True)

chain_data, non_chain_data = chain_resturant(all_chain_name,amenities)
chain_data = chain_data.reset_index(drop=True)
non_chain_data = non_chain_data.reset_index(drop=True)
non_chain_data.to_csv('data/non_chain.csv')
chain_data.to_csv('data/chain.csv')
#print(non_chain_data)
