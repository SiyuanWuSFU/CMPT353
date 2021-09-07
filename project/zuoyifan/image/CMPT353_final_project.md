#  <center>CMPT353 Project Report<center/>

### Part 1: Travelling Route(Yifan Zuo)

---

- Problem addressing:

  - `What is the most reasonable travel route over the original data`?
  -  A reasonable travel route is connected by several reasonable travel points.
  - A reasonable travel point should near by at least four most important amenities, another amenity is optional:
    - **food**: a travel point should near by lots of restaurants...tec.
    - **transportation**: a travel point should be transportation convenient and transportation relavent place.
    - **entertainment**: a travel point should be fun. 
    - **shopping and banking**: a travel point should near by bank and shopping mall.
    - **living and storage** (optional): place to have rest such as hotel. luggage deposit.

- Data cleaning (data_cleaning.py):

  - Remove irrevalent amenities:

    - amenities such as fire_station, kindergarten...etc shouldn't be our consideration, those are irrelavent to our problem.

  - Group the remaining amenities and classify them as above five amenities.

    - **Food**: cafe, fast_food, bbq, vending_machine, restaurant, drinking_water, juice_bar, watering_place, water_point, food_court, ice_cream.  
    - **transportation**: fuel, parking_entrance, bicycle_parking, parking, ferry_terminal, car_rental, car_sharing, bicycle_rental, seaplane terminal, car_wash, bicycle_repair_station, parking_space, taxi, bus_station, motorcycle_parking, boat_rental, loading_dock, car_rep, motorcycle_rental.
    - **entertainment**: pub, public_building, cinema, theatre, bar, arts_centre, fountain, nightclub, stripclub, gambling, bistro, playground, spa, events_venue, internet_cafe, social_centre, gym, park, biergarten, leisure.
    - **shopping and banking**: atm, bank, bureau_de_change, marketplace, atm;bank, money_transfer, shop|clothes. 
    - **living and storage**: bench, shelter, luggage_locker, lounge, housing co-op, storage.

  - Remove the rows which name is Nan. 

    - If the name is Nan, then traveller cannot search these places and therefore those information are useless.

  - Remove outlier:

    - In order to make later clustering center point more clear, we can use `LocalOutlierFactor()` to remove some outliers base on the latitude and longitude of the points.

      |              cleaned data before remove outlier              |              cleaned data after remove outlier               |
      | :----------------------------------------------------------: | :----------------------------------------------------------: |
      | <img src="/Users/sakazuho/Desktop/大四/third semester/cmpt353/cmpt353/zuoyifan/image_and_report/before_remove_outlier.png" alt="before_remove_outlier" style="zoom:15%;" /> | <img src="/Users/sakazuho/Desktop/大四/third semester/cmpt353/cmpt353/zuoyifan/image_and_report/after_remove_outlier.png" alt="after_remove_outlier" style="zoom:15%;" /> |

- Data Written (data_cleaning.py):

  - After data cleaning process, the cleaned data will be written into cleaned_data.csv, and five separate data: food.csv, transportation.csv, entertainment.csv, living_stroage.csv, shopping_banking.csv.
  - All processed data in the directory named 'data'.

- Clustering (map_cluster.ipynb, cluster.py):

  - Use python `folium` to present the map.

  - Use `sklearn.cluster Kmean`  to do the clustering.

    - the n_cluster is tuned to the best value: food: 14 clusters, transportation: 11 clusters, entertainment: 10 clusters, shopping and banking: 15 clusters, living and storage: 3 clusters.
    - The center point of each cluster(big blue point) can be calculate by mean of lon and lat of that cluster points
    - Different color represent diffierent cluster. The blue big point represent the center point of that cluster.

    |                             Food                             |                        transportation                        |                        Entertainment                         |
    | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
    | <img src="/Users/sakazuho/Desktop/大四/third semester/cmpt353/cmpt353/zuoyifan/image_and_report/food_cluster.png" alt="food_cluster" style="zoom:50%;" /> | <img src="/Users/sakazuho/Desktop/大四/third semester/cmpt353/cmpt353/zuoyifan/image_and_report/transportation_cluster.png" alt="transportation_cluster" style="zoom:50%;" /> | <img src="/Users/sakazuho/Desktop/大四/third semester/cmpt353/cmpt353/zuoyifan/image_and_report/entertainment_cluster.png" alt="entertainment_cluster" style="zoom:50%;" /> |
    |                     banking and shopping                     |                      living and storage                      |                                                              |
    | <img src="/Users/sakazuho/Desktop/大四/third semester/cmpt353/cmpt353/zuoyifan/image_and_report/shopping_banking_cluster.png" alt="shopping_banking_cluster" style="zoom:50%;" /> | <img src="/Users/sakazuho/Desktop/大四/third semester/cmpt353/cmpt353/zuoyifan/image_and_report/living_storage_cluster.png" alt="living_storage_cluster" style="zoom:50%;" /> |                                                              |

- Analysis and Conclusion (analysis.ipynb):

  - Amenity grouping: (groups image)

    - Base on the above five different clustering, we now present the all center points of the five amenities.
    - Blue point: food, green point: banking and shopping, red point: entertainment, black point: transportation, purple point: living and storage.
    - The red square box represent a group of those different center points. Every red square should conatin at least one of blue, red, gren black center point meaning that travel point should near by at least four most important amenities. The purple center point is optional. We mentioned early. 
    - We can see the image below, there are 8 qualified groups(red box). 

  - Travel route: (travel route image)

    - We can calculate the center point among those groups(red big point) shown on the below image. The big red point is actually our travel points.

    - Then the problem become TSP problem, we can find the shortest path among those points, and the path is shown as the blue arrow.

    - The latitude and longitude travel route(red big points):

      `(49.17918741164552, -123.13875940395383)`$\rightarrow$`(49.2734536397419, -123.13272939827512)`$\rightarrow$`(49.26395053943205, -123.0885422157221)`$\rightarrow$`(49.2346415642415, -122.99360688849441)`$\rightarrow$`(49.221810611933634, -122.8984494528381)`$\rightarrow$`(49.26632186591236, -122.79747464328304)`$\rightarrow$`(49.20270020618055, -122.620861450625)`$\rightarrow$`(49.12279338831816, -122.67356765116651)`

    - The rough location travel route:

      `Richmond: Golden Village`$\rightarrow$`Vancouver: Granville Bridge`$\rightarrow$`Vancouver: Main Street-Science World`$\rightarrow$`Burnaby: Deer Lake Park`$\rightarrow$`New Westminister: Fraser Cemetery`$\rightarrow$`Port Coquitlam`$\rightarrow$`Maple Ridge: Langley Bog`$\rightarrow$`Langley City: Langley Township`

    |                        Grouping image                        |                      Travel route image                      |
    | :----------------------------------------------------------: | :----------------------------------------------------------: |
    | <img src="/Users/sakazuho/Desktop/大四/third semester/cmpt353/cmpt353/zuoyifan/image_and_report/travel_cluster.jpeg" alt="travel_cluster" style="zoom:50%;" /> | <img src="/Users/sakazuho/Desktop/大四/third semester/cmpt353/cmpt353/zuoyifan/image_and_report/travel_route.jpeg" alt="travel_route" style="zoom:50%;" /> |

- Limitation:

  - The grouping techique(not clustering) is not supported by statistical test for roughly the same mean of longitude and latitude, we only can conclude by see the graph.
  - we need to tune the n_cluster parameter for the Kmean clustering, in some cases it's not perfect.

  

  

  

  

  

  

  

  

  

  ​	