import pandas as pd
totals = pd.read_csv('totals.csv').set_index(keys=['name'])



min_p = totals.sum(axis=1).idxmin()
#c_name = totals.iloc[min_p,:]
print("City with lowest total precipitation:")
print(min_p)

counts = pd.read_csv('counts.csv').set_index(keys=['name'])
#print(counts)

totals_p = totals.sum(axis=0)/counts.sum(axis=0)

#totals["sum_t"] = totals.sum(axis=0)
#avg_p =Total_p / Total_c
print("Average precipitation in each month:")
print(totals_p)

totals_c = totals.sum(axis=1)/counts.sum(axis=1)
print("Average precipitation in each city:")
print(totals_c)
