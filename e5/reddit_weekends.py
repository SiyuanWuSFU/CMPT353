import sys
import pandas as pd
from datetime import date
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np


# In[222]:
OUTPUT_TEMPLATE = (
    "Initial T-test p-value: {initial_ttest_p:.3g}\n"
    "Original data normality p-values: {initial_weekday_normality_p:.3g} {initial_weekend_normality_p:.3g}\n"
    "Original data equal-variance p-value: {initial_levene_p:.3g}\n"
    "Transformed data normality p-values: {transformed_weekday_normality_p:.3g} {transformed_weekend_normality_p:.3g}\n"
    "Transformed data equal-variance p-value: {transformed_levene_p:.3g}\n"
    "Weekly data normality p-values: {weekly_weekday_normality_p:.3g} {weekly_weekend_normality_p:.3g}\n"
    "Weekly data equal-variance p-value: {weekly_levene_p:.3g}\n"
    "Weekly T-test p-value: {weekly_ttest_p:.3g}\n"
    "Mann-Whitney U-test p-value: {utest_p:.3g}"
)

def main():
    reddit_counts = sys.argv[1]

    # ...



    counts = pd.read_json("reddit-counts.json.gz", lines=True)


    # In[223]:


    counts_canada = counts.loc[counts['subreddit'] == "canada"]
    filtered = counts_canada.loc[(counts_canada['date'].dt.year==2013) | (counts_canada['date'].dt.year==2012)]


    # In[224]:


    weekend = filtered.loc[(filtered['date'].dt.dayofweek==5)|(filtered['date'].dt.dayofweek==6)]
    weekday = filtered.loc[(filtered['date'].dt.dayofweek!=5)& (filtered['date'].dt.dayofweek!=6)]


    # In[225]:


    ttest = stats.ttest_ind(weekend["comment_count"],weekday["comment_count"],equal_var = False)
    #print(ttest.statistic)
    #print(ttest.pvalue)


    # In[226]:


    weekend_n = stats.normaltest(weekend["comment_count"])
    #print("normality ",weekend_n.pvalue)
    weekday_n = stats.normaltest(weekday["comment_count"])
    #print("normality ",weekday_n.pvalue)
    stat,p= stats.levene(weekend["comment_count"],weekday["comment_count"])
    #print("equal variance p-value: ",p)

    #print("Not normally distrubuted, not equal variance")
    #print("It is very unlikely that there are same number of comments on weekdays and weekends")


    # In[227]:

    """
    plt.figure()
    plt.hist((weekend["comment_count"],weekday["comment_count"]),label = ['weekend','weekday'])
    plt.legend(loc='upper right')
    plt.show()
    """

    # In[228]:


    weekend_trans = np.sqrt(weekend["comment_count"])
    weekday_trans = np.sqrt(weekday["comment_count"])
    weekend_n_trans = stats.normaltest(weekend_trans)
    #print("normality ",weekend_n.pvalue)
    weekday_n_trans = stats.normaltest(weekday_trans)
    #print("normality ",weekday_n.pvalue)
    stat,p_trans= stats.levene(weekend_trans,weekday_trans)
    #print("equal variance p-value: ",p)
    #print("First one normally distrubuted,equal variance")


    # In[229]:


    ## adopted from https://stackoverflow.com/questions/48058304/how-to-apply-series-in-isocalendar-function-in-pandas-python
    ## Fix 2


    weekend_CLT = filtered.loc[(filtered['date'].dt.dayofweek==5)|(filtered['date'].dt.dayofweek==6)]
    weekday_CLT = filtered.loc[(filtered['date'].dt.dayofweek!=5)& (filtered['date'].dt.dayofweek!=6)]

    weekday_CLT = weekday_CLT.copy()
    weekend_CLT = weekend_CLT.copy()

    weekend_CLT["year"] = weekend_CLT["date"].apply(lambda x: str(x.isocalendar()[0]) )
    weekend_CLT["month"] = weekend_CLT["date"].apply(lambda x: str(x.isocalendar()[1]) )

    weekday_CLT["year"] = weekday_CLT["date"].apply(lambda x: str(x.isocalendar()[0]) )
    weekday_CLT["month"] = weekday_CLT["date"].apply(lambda x: str(x.isocalendar()[1]) )

    aggregated_weekend = weekend_CLT.groupby(['year', 'month']).mean()
    aggregated_weekday = weekday_CLT.groupby(['year', 'month']).mean()
    #aggregated = counts.groupby(['year', 'month']).mean()
    #print(aggregated_weekend)
    #print(aggregated_weekday)
    #print(aggregated)


    # In[233]:


    a_ttest = stats.ttest_ind(aggregated_weekend["comment_count"],aggregated_weekday["comment_count"])
    #print(a_ttest.pvalue)


    # In[231]:


    a_weekend_n = stats.normaltest(aggregated_weekend["comment_count"])
    #print("normality ",a_weekend_n.pvalue)
    a_weekday_n = stats.normaltest(aggregated_weekday["comment_count"])
    #print("normality ",a_weekday_n.pvalue)
    stat,weekly_p= stats.levene(aggregated_weekend["comment_count"],aggregated_weekday["comment_count"])
    #print("equal variance p-value: ",weekly_p)


    # In[232]:

    """
    plt.figure()
    plt.hist((aggregated_weekend["comment_count"],aggregated_weekday["comment_count"]),label = ['weekend','weekday'])
    plt.legend(loc='upper right')
    plt.show()
    """

    # In[243]:


    ##fix 3
    weekend_u = filtered.loc[(filtered['date'].dt.dayofweek==5)|(filtered['date'].dt.dayofweek==6)]
    weekday_u = filtered.loc[(filtered['date'].dt.dayofweek!=5)& (filtered['date'].dt.dayofweek!=6)]
    u_test = stats.mannwhitneyu(weekend_u["comment_count"],weekday_u["comment_count"],alternative = 'two-sided')


    print(OUTPUT_TEMPLATE.format(
        initial_ttest_p=ttest.pvalue,
        initial_weekday_normality_p=weekday_n.pvalue,
        initial_weekend_normality_p=weekend_n.pvalue,
        initial_levene_p=p,
        transformed_weekday_normality_p=weekday_n_trans.pvalue,
        transformed_weekend_normality_p=weekend_n_trans.pvalue,
        transformed_levene_p= p_trans,
        weekly_weekday_normality_p=a_weekday_n.pvalue,
        weekly_weekend_normality_p=a_weekend_n.pvalue,
        weekly_levene_p= weekly_p,
        weekly_ttest_p=a_ttest.pvalue,
        utest_p=u_test.pvalue,
    ))

if __name__ == '__main__':
    main()
    # In[ ]:
