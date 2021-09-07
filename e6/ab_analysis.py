import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


# In[46]:
OUTPUT_TEMPLATE = (
    '"Did more/less users use the search feature? A: We cannot reject null hypothesis, so we cannot tell \n a relation between new feature and more/less users uses them " p-value:  {more_users_p:.3g}\n'
    '"Did users search more/less?" A: p>0.05, we cannot reject null hypothesis so user search less  p-value:  {more_searches_p:.3g} \n'
    '"Did more/less instructors use the search feature?" A: p >0.05, so we cannot reject less \ninstructors use the search feature p-value:  {more_instr_p:.3g}\n'
    '"Did instructors search more/less?" A: p<0.05, that means instructors search more than before. p-value:  {more_instr_searches_p:.3g}'
)

def main():
    searchdata_file = sys.argv[1]

    # ...

    # Output

    searches =  pd.read_json("searches.json",orient='records', lines=True)


    # In[47]:


    #print(searches)


    # In[48]:


    new = searches.loc[(searches['uid']%2 == 1)]
    original = searches.loc[(searches['uid']%2 == 0)]


    # In[49]:


    new_one_search = new[new["search_count"] > 0]
    new_no_search = new[new["search_count"] == 0]
    original_one_search = original[original["search_count"] > 0]
    original_no_search = original[original["search_count"] == 0]

    contingency = [[original_one_search.shape[0],original_no_search.shape[0]],
                  [new_one_search.shape[0],new_no_search.shape[0]]]
    #print(contingency)


    # In[50]:


    chi2, p , dof, exp = stats.chi2_contingency(contingency)
    #print(p)
    #print("there might be no relationship")


    # In[51]:


    teacher_new = searches.loc[(searches['uid']%2 == 1)&(searches['is_instructor']==True)]
    teacher_original = searches.loc[(searches['uid']%2 == 0)&(searches['is_instructor']==True)]


    # In[52]:


    teacher_new_one_search = teacher_new[teacher_new["search_count"] > 0]
    teacher_new_no_search = teacher_new[teacher_new["search_count"] == 0]
    teacher_original_one_search = teacher_original[teacher_original["search_count"] > 0]
    teacher_original_no_search = teacher_original[teacher_original["search_count"] == 0]

    contingency = [[teacher_original_one_search.shape[0],teacher_original_no_search.shape[0]],
                  [teacher_new_one_search.shape[0],teacher_new_no_search.shape[0]]]
    #print(contingency)


    # In[53]:


    chi2, T_p , dof, exp = stats.chi2_contingency(contingency)
    #print(T_p)
    #print("there might be some relationship")


    # In[28]:


    """
    plt.figure()
    plt.hist((new["search_count"],original["search_count"]),label = ['new','original'])
    plt.legend(loc='upper right')
    plt.show()
    """

    # In[29]:


    #print(new)
    #print(original)


    # In[56]:


    ##U-test
    u_test = stats.mannwhitneyu(new["search_count"],original["search_count"])
    #print(u_test.pvalue)


    # In[57]:


    Teacher_u_test = stats.mannwhitneyu(teacher_new["search_count"],teacher_original["search_count"])
    #print(Teacher_u_test.pvalue)
    #print("null h can be rejected with p<0.05")

    print(OUTPUT_TEMPLATE.format(
        more_users_p=p,
        more_searches_p=u_test.pvalue,
        more_instr_p=T_p,
        more_instr_searches_p=Teacher_u_test.pvalue,
    ))
    # In[ ]:


if __name__ == '__main__':
    main()
