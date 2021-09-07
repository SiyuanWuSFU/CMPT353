# <center>CMPT353<center/>

### part 1: Travelling route:(zuoyifan)

---

- Order of execution:

  - data_cleaning.py
  - map_cluster.ipynb
  - analysis.ipynb

- data_cleaning.py:

  - Required library: `numpy`, `pandas`, `sklearn.neighbors`

  - Functions:

    - **drop_useless_amenities(data):**

      Read from @data, drop irrelavent amenities rows. Return data.

    - **combine_samilar_amenities(data):**

      Read from @data, combine amenities to five similar amenities: 'food' 'transportation' 'entertainment' 'living_stroage' 'shopping_banking'. Return data.

    - **remove_null_name(data):**

      Read from @data, remove null name rows. Return data.

    - **remove_outlier(data):**

      Read from @data, use LocalOutlierFactor() to remove outlier. Return data.

    - **store_partial_data(data):**

      Read from @data, classify by the five amenities, then written data to csv file base on the classification.

  - File produced: 

    data/food.csv, data/transportation.csv, data/entertainment.csv, data/living_stroage.csv, data/shopping_banking.csv. All in zuoyifan/data directory.

  - Run: `python3 data_cleaning`

- map_cluster.ipynb:

  - Required library: `numpy`, `pandas`, `matplotlib.pyplot`, `folium`, `sklearn.cluster`

    - folium: python3 -m pip install folium

  - Import functions: `from data_cleaning.py import remove_outlier`, ` from cluster.py import cluster_mean`

  - Functions:

    - **map_scatter_plot(data_file)**:

      Read from @data_file, create map centered at mean lat and lon of the data then add every data point to the map.

    - **initial_map(data_file, num_cluster)**:

      Read from @data_file, use KMean clustering the n_clusters is read from @num_cluster. Initialize the folium map, return the map, cluster points and data points.

    - **cluster_map(data_file, num_cluster):**

      @data_file, @num_cluster is pass to the Initial_map, then plot the points using different colors base on the different clusterings. Return the map.

    - **add_cluster_center(data_file, num_cluster, data_map):**  

      Read from @data_file, for each cluster points, calculate the center point base on the mean of longitude and latitude. Then add those center points to the map. Return those center points and the map.

  - Run: 

    The sample code is the example of running file data/transportation.csv. There are five of them, data/food.csv etc. Modify the @data_file and the @num_cluster then `restart the kernel`.

    - data/food.csv: 14 cluster
    - data/transportation: 11 cluster
    - data/entertainment: 10 cluster
    - data/shopping_banking: 15 cluster
    - data/living)_storage: 3 cluster

- cluster.py:

  - Required library: `numpy`, `pandas`, `matplotlib.pyplot`, `sklearn.cluster`

  - Import functions: `from data_cleaning.py import remove_outlier`

  - Functions:

    - **lat_lon_mean(l):**

      Read @l longitude and latitude pairs, calculate the mean longitude and latitude. Return the (lat_mean, lon_mean) pair.

    - **cluster_mean(file, num_cluster):**

      Read from the @file, do KMean using @num_cluster, store different cluster points to a python dictionary, then use lat_lon_mean to calculate each cluster center points. Return those center points.

  - Run: this is the helper function used in map_cluster.ipynb and analysis.ipynb.

- analysis.ipynb:

  - Required library: `numpy`, `pandas`, `matplotlib.pyplot`, `folium`

  - Import functions: `from cluster import lat_lon_mean`

  - Functions:

    - **draw_base_map():**

      Create map centered at mean latitude and longitude of the data [49.121383503296705, -122.67246901153845]. Retune the map.

    - **draw_pivot_point(data_map, pivot, color):**

      Read the @pivot, add the pivot center point to the map by the @color. Return the data_map.

    - **draw_cluster_center(data_map):**

      Based on the cluster center points longitude and latitude, calculate the grouping center points(travlling points), add those points to the @data_map. Return the data_map. 

  - Run: `restart the kernel`

### part 2: Chain and Non-chain Restaurant Identification(LeonWu)

---

- Order of execution:

  - data_forming.py
  - map_cluster.ipynb
  - stat_test.py

- data_forming.py:

  - Required library: `numpy`, `pandas`, `sklearn.neighbors`, `sys`, `difflib`, `matplotlib.pyplot`, `requests`, `BeautifulSoup`

  - Functions:

    - **fetch_wiki_directory(url):**

      Fetch the directory from the given @url and return the table as a data frame.

    - **fetch_wiki_table(url,fetch_all):**

      Fetch the tables from the given @url and return the table as a data frame. If @fetch_all = true then all table from the page will be fetch

    - **chain_restaurant_name(df):**

      Perform manual data cleaning for data @df

    - **user_defined_chain(data,number_of_restaurant):**

      Select all data entries from @data, where number of restaurant > @number_of_restaurant

    - **chain_restaurant(chain_name,data):**

      Return all entries in @data where the name is in @chain_name

  - File produced:

    data/all_restaurant.csv, data/non_chain.csv, data/chain.csv all in LeonWu/data directory.

  - Run: `python3 data_forming.py`

- map_cluster.ipynb:

  - Required library: `numpy`, `pandas`, `sklearn.neighbors`,  `matplotlib.pyplot`,  `folium`, `sklearn.cluster`, `folium.plugins`

  - Import functions: ` from cluster.py import cluster_mean`

  - Functions:

    - **map_scatter_plot(data_file)**:

      Read from @data_file, create map centered at mean lat and lon of the data then add every data point to the map.

    - **initial_map(data_file, num_cluster)**:

      Read from @data_file, use KMean clustering the n_clusters is read from @num_cluster. Initialize the folium map, return the map, cluster points and data points.`

    - **cluster_map(data_file, num_cluster):**

      @data_file, @num_cluster is pass to the Initial_map, then plot the points using different colors base on the different clusterings. Return the map.

    - **add_cluster_center(data_file, num_cluster, data_map,marker_color):**

      Read from @data_file, for each cluster points, calculate the center point base on the mean of longitude and latitude. Then add those center points to the map. Return those center points and the map.

  - File produced:

    data/all_data.csv, data/cl_data.csv, data/ncl_data.csv all in LeonWu/data directory.

  - Run: `restart the kernel`

- cluster.py:

  - Required library: `numpy`, `pandas`, `matplotlib.pyplot`, `sklearn.cluster`

  - Functions:

    - **lat_lon_mean(l):**

      Read @l longitude and latitude pairs, calculate the mean longitude and latitude. Return the (lat_mean, lon_mean) pair.

    - **cluster_mean(file, num_cluster):**

      Read from the @file, do KMean using @num_cluster, store different cluster points to a python dictionary, then use lat_lon_mean to calculate each cluster center points. Return those center points.

  - Run: this is the helper function used in map_cluster.ipynb and analysis.ipynb.

- stat_test.py

  - Required library: `numpy`, `pandas`, `matplotlib.pyplot`, `scipy.stats`

  - Functions:

    - separate(all,one_subset):

      Extract the desired @one_subset from the @all data

    - chi_score(df1,df2):

      Returns a count of feature for @df1 and @df2

    - create_chi_data(list1,list2):

      Create contingency table for chi-square test using @list1 and @list2

  - Run: `python3 cluster.py`

### part 3: Hotel Choose:(shuang)

- part3.ipynb

  - Required library: `numpy`, `pandas`, `matplotlib.pyplot`, `folium`, `sklearn.cluster`

  - File used:

    amenities-vancouver.json.gz

    listing.csv : summary information and metrics for listings of Airbnb in Vancouver and compiled at 06 July 2021.

  - base map:

    Create map centered at mean latitude and longitude of the data [49.121383503296705, -122.67246901153845].

  - data clean:

    - amenities-vancouver.json.gz:

      using folium to located food, transportation, entertainment, shopping mall on base map.

    - Airbnb:

      using folium to located Airbnb on base map : one for all Airbnb and one for Airbnb's price higher than 200

  - cluster:

      Read from @data_file, for each cluster points, calculate the center point base on the mean of longitude and latitude. 
      
      Then add those center points to the map. Return those center points and the map.

  - Run: `restart the kernel`
---



