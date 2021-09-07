import numpy as np
import sys
import pandas as pd
import difflib


filename1 = sys.argv[1]
filename2 = sys.argv[2]
filename3 = sys.argv[2]
movie_list = open(filename1).readlines()

accurate_name = pd.DataFrame(data={"movie name": movie_list})
accurate_name = accurate_name.replace('\n','', regex=True)
accurate_name.sort_values("movie name")
#print(accurate_name)

movie_ratings = pd.read_csv(filename2)
movie_ratings.sort_values("title")
#print(movie_ratings)

movie_ratings['title'] = movie_ratings.apply(lambda row: difflib.get_close_matches(row["title"],accurate_name["movie name"]),axis = 1 )
movie_ratings['title'] = movie_ratings['title'].str[0]
movie_ratings.dropna(subset = ["title"], inplace=True)
movie_ratings.groupby('title')
#print(movie_ratings)
df1 = movie_ratings.groupby('title').mean()
df1.rating = df1.rating.round(2)
df1.sort_values('title', ascending=False)
df1.to_csv("output.csv")
#df1["rating"] = df1["rating"].astype(int)
#a=np.array(df1["rating"].tolist())
#print(a)
#df2 = df1.T
#df2.apply(lambda col: difflib.get_close_matches(row["title"],accurate_name["movie name"]),axis = 0 )
#print(df1)
