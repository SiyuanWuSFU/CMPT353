
import time
from implementations import all_implementations
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd


# In[101]:
total =time.time()
data = []
count = 0
while count<55:
    #random_array = np.random.normal(loc=500, scale = 250,size=1000).astype(int)
    random_array = np.random.randint(10000,size = 20000)
    one_sort = []
    for sort in all_implementations:
        st = time.time()

        res = sort(random_array)
        en = time.time()
        #print(en-st)
        one_sort.append(en-st)
        count = count +(en-st)
    data.append(one_sort)
    #print("count: ",count)

#print(count)
# In[102]:

"""
plt.figure()
plt.hist(random_array, bins = 20)
plt.show()
"""

# In[103]:


#normal = stats.normaltest(random_array)
#print(random_array)
#print(normal.pvalue)


# In[104]:



df = pd.DataFrame(data,columns=['qs1','qs2','qs3','qs4','qs5','merge1','partition_sort'])

df.to_csv("data.csv",index = False)
# In[105]:


#print(df)
end =time.time()
print("total time: ", end-total)
# In[ ]:
