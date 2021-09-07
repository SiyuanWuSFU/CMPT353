import numpy as np
data = np.load('monthdata.npz')
totals = data['totals']
counts = data['counts']
print(totals)
print(counts)
sum_total=totals.sum(axis=1)
#print(sum_total)
lowest_p = np.argmin(sum_total)
print("Row with lowest total precipitation:" ,lowest_p)

Total_p = totals.sum(axis=0)
Total_c = counts.sum(axis=0)
avg_p =Total_p / Total_c
print("Average precipitation in each month: ", avg_p)

Total_p = totals.sum(axis=1)
Total_c = counts.sum(axis=1)
avg_p =Total_p / Total_c
print("Average precipitation in each city: ", avg_p)


num_rows, num_cols = totals.shape

q_total = totals.reshape(4*num_rows,3)
q_sum_total=q_total.sum(axis=1)
final_total = q_sum_total.reshape(num_rows,4)
print("Quarterly precipitation totals:")
print(final_total)
