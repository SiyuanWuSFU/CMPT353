import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

def chi_score(df1,df2):
    df1= df1.groupby('cluster_x').count()
    df2= df2.groupby('cluster_x').count()
    #print(chain)
    list1 = df1['var1'].tolist()
    list2 = df2['var2'].tolist()
    return list1, list2

def create_chi_data(list1,list2):
    chi_data = []
    for i in range(len(list1)):
        one_group = [list1[i],list2[i]]
        chi_data.append(one_group)
    return chi_data

def separate(all,one_subset):
    new_df = pd.merge(all, one_subset,  how='left', on=['var1','var2'])
    new_df = new_df.dropna(subset=['cluster_y'])
    #print(new_df)
    return new_df

all = pd.read_csv("data/all_data.csv")
chain = pd.read_csv("data/cl_data.csv")
non_chain = pd.read_csv("data/ncl_data.csv")




#new_df.to_csv('a.csv')



all_chain = separate(all,chain)
all_non_chain = separate(all,non_chain)






chain_list, non_chain_list = chi_score(all_chain,all_non_chain)
#print(chain_list,non_chain_list)

chi_data = create_chi_data(chain_list,non_chain_list)
#print(chi_data)
chi2, p , dof, exp = stats.chi2_contingency(chi_data)
output = f"{p:.9f}"
reject = 0.05/8
reject_output= f"{reject:.9f}"
print('p-value: ', output)
print('Rejecting p-value with Bonferroni correction: ', reject_output)
