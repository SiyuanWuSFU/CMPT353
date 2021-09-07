import numpy as np
import sys
import pandas as pd
import difflib
from math import cos, asin, sqrt, pi
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Adapted from https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula/21623206
    answered by user Salvador Dali
    """
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a))* 1000  # unit in meters

def find_best( data1_lat, data1_lon, data):

    data['distance'] = data.apply(lambda row: calculate_distance(row['latitude'], row['longitude'], data1_lat, data1_lon),axis = 1 )
    best_match = data[data.distance == data.distance.min()]
    #print(best_match["station"])
    #print(name)
    #sum = data['sum'].sum()
    return best_match["avg_tmax"].iloc[0]


stations_file = sys.argv[1]
city_data = sys.argv[2]
p = sys.argv[3]
stations = pd.read_json(stations_file, lines=True)
city = pd.read_csv(city_data)
city = city.dropna()
city["area"] = city["area"]* (10**-6)
city["population density"] = city["population"]/city["area"]

city = city.drop(city[city.area > 10000].index)

#city['best_match'] =  find_best(city['name'].iloc[1], city['latitude'].iloc[1], city['longitude'].iloc[1],stations)
city['best_match'] = city.apply(lambda row: find_best(row['latitude'], row['longitude'],stations),axis = 1 )
city['best_match'] = city['best_match']/10
#city['avg_tmax']  =
plt.figure()
plt.scatter(city['best_match'],city["population density"])
plt.title("Temperature vs Population Density")
plt.xlabel("Avg Max Temperature (\u00b0C)")
plt.ylabel("Population Density (people/km\u00b2)")
#plt.show()
plt.savefig('output.svg')
#print(city)
#print(stations)
