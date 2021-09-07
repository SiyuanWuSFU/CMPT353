# The code is adapted from Zuo Yifan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



from sklearn.cluster import KMeans


def lat_lon_mean(l):
	lat_sum, lon_sum = 0, 0
	length = len(l)
	for pair in l:
		lat_sum += pair[0]
		lon_sum += pair[1]

	lat_mean = lat_sum / length
	lon_mean = lon_sum / length

	return (lat_mean, lon_mean)



def cluster_mean(file, num_cluster):
	# read data file
	data = pd.read_csv(file, index_col=0)
	X = np.stack([data['lat'], data['lon']], axis=1)
	model = KMeans(n_clusters=num_cluster)
	y = model.fit_predict(X)

	dic = {}

	for index, row in data.iterrows():
		if y[index] not in dic.keys():
			dic[y[index]] = [(row['lat'], row['lon'])]	# append a new index of lat lon pair
		else:
			dic[y[index]].append((row['lat'], row['lon']))

	mean = []
	for i in range(num_cluster):
		mean.append(lat_lon_mean(dic[i]))

	return mean
