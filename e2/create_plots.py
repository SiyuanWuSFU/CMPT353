import sys
import pandas as pd
import matplotlib.pyplot as plt


filename1 = sys.argv[1]
filename2 = sys.argv[2]

def read_data(filename):
    formatted_data = pd.read_csv(filename, sep=' ', header=None, index_col=1,
        names=['lang', 'page', 'views', 'bytes'])
    return formatted_data

# def plotting():
#     plt.figure(figsize=(10, 5)) # change the size to something sensible
#     plt.subplot(1, 2, 1) # subplots in 1 row, 2 columns, select the first
#     plt.plot(…) # build plot 1
#     plt.subplot(1, 2, 2) # ... and then select the second
#     plt.plot(…) # build plot 2
#     return

plt.figure(figsize=(10, 5))

data1 = read_data(filename1)
sorted_1 = data1.sort_values(by=['views'], ascending=False).reset_index()
plt.subplot(1, 2, 1) # subplots in 1 row, 2 columns, select the first
plt.plot(sorted_1['views'].values)
plt.title("Popularity Distribution")
plt.xlabel("Rank")
plt.ylabel("Views")


data2 = read_data(filename2).reset_index()

merged_data = data1.merge(data2, on = 'page', how = 'left')
#print(merged_data)
plt.subplot(1, 2, 2) # ... and then select the second
plt.scatter(merged_data['views_x'], merged_data['views_y'], marker='o', s=10);
plt.xscale("log")
plt.yscale("log")
plt.title("Hourly Correlation")
plt.xlabel("Hour 1 views")
plt.ylabel("Hour 2 views")
plt.savefig('wikipedia.png')
