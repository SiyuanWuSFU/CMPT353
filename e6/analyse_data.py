import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd


# In[105]:


df = pd.read_csv("data.csv")

#print(df)


# In[106]:


anova = stats.f_oneway(df["qs1"],df["qs2"],df["qs3"],df["qs4"],df["qs5"],df["merge1"],df["partition_sort"])
print("anova p-value: ",anova.pvalue)


# In[108]:

"""
normal = stats.normaltest(df["qs1"])
print(normal.pvalue)
normal = stats.normaltest(df["qs2"])
print(normal.pvalue)
normal = stats.normaltest(df["qs3"])
print(normal.pvalue)
normal = stats.normaltest(df["qs4"])
print(normal.pvalue)
normal = stats.normaltest(df["qs5"])
print(normal.pvalue)
normal = stats.normaltest(df["merge1"])
print(normal.pvalue)
normal = stats.normaltest(df["partition_sort"])
print(normal.pvalue)
plt.figure()
plt.hist(df["qs5"])
plt.show()
"""

# In[81]:


melt = pd.melt(df)
#print(melt)


# In[82]:


post_hoc = pairwise_tukeyhsd(melt['value'],melt['variable'],alpha=0.05)


# In[83]:


print(post_hoc.summary())


# In[55]:


fig = post_hoc.plot_simultaneous()
plt.show()

# In[ ]:
