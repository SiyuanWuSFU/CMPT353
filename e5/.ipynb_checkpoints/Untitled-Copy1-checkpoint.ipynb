{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 221,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "import pandas as pd\n",
    "from datetime import date\n",
    "from scipy import stats\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 222,
   "metadata": {},
   "outputs": [],
   "source": [
    "counts = pd.read_json(\"reddit-counts.json.gz\", lines=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 223,
   "metadata": {},
   "outputs": [],
   "source": [
    "counts_canada = counts.loc[counts['subreddit'] == \"canada\"]\n",
    "filtered = counts_canada.loc[(counts_canada['date'].dt.year==2013) | (counts_canada['date'].dt.year==2012)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 224,
   "metadata": {},
   "outputs": [],
   "source": [
    "weekend = filtered.loc[(filtered['date'].dt.dayofweek==5)|(filtered['date'].dt.dayofweek==6)]\n",
    "weekday = filtered.loc[(filtered['date'].dt.dayofweek!=5)& (filtered['date'].dt.dayofweek!=6)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 225,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-19.068164546804166\n",
      "6.138975517118774e-60\n"
     ]
    }
   ],
   "source": [
    "ttest = stats.ttest_ind(weekend[\"comment_count\"],weekday[\"comment_count\"],equal_var = False)\n",
    "print(ttest.statistic)\n",
    "print(ttest.pvalue)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 226,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "normality  0.0015209196859635404\n",
      "normality  1.0091137251707994e-07\n",
      "equal variance p-value:  0.04378740989202803\n",
      "Not normally distrubuted, not equal variance\n",
      "It is very unlikely that there are same number of comments on weekdays and weekends\n"
     ]
    }
   ],
   "source": [
    "weekend_n = stats.normaltest(weekend[\"comment_count\"])\n",
    "print(\"normality \",weekend_n.pvalue)\n",
    "weekday_n = stats.normaltest(weekday[\"comment_count\"])\n",
    "print(\"normality \",weekday_n.pvalue)\n",
    "stat,p= stats.levene(weekend[\"comment_count\"],weekday[\"comment_count\"])\n",
    "print(\"equal variance p-value: \",p)\n",
    "\n",
    "print(\"Not normally distrubuted, not equal variance\")\n",
    "print(\"It is very unlikely that there are same number of comments on weekdays and weekends\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 227,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure()\n",
    "plt.hist((weekend[\"comment_count\"],weekday[\"comment_count\"]),label = ['weekend','weekday'])\n",
    "plt.legend(loc='upper right')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 228,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "normality  0.10760562894666933\n",
      "normality  0.03687221613365365\n",
      "equal variance p-value:  0.5560544297516696\n",
      "First one normally distrubuted,equal variance\n"
     ]
    }
   ],
   "source": [
    "weekend_trans = np.sqrt(weekend[\"comment_count\"])\n",
    "weekday_trans = np.sqrt(weekday[\"comment_count\"])\n",
    "weekend_n = stats.normaltest(weekend_trans)\n",
    "print(\"normality \",weekend_n.pvalue)\n",
    "weekday_n = stats.normaltest(weekday_trans)\n",
    "print(\"normality \",weekday_n.pvalue)\n",
    "stat,p= stats.levene(weekend_trans,weekday_trans)\n",
    "print(\"equal variance p-value: \",p)\n",
    "print(\"First one normally distrubuted,equal variance\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 229,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            comment_count\n",
      "year month               \n",
      "2008 10          4.000000\n",
      "     11          2.000000\n",
      "     13          2.500000\n",
      "     14          2.500000\n",
      "     15          2.500000\n",
      "...                   ...\n",
      "2015 5         216.041667\n",
      "     6         267.650000\n",
      "     7         254.476190\n",
      "     8         276.809524\n",
      "     9         228.250000\n",
      "\n",
      "[378 rows x 1 columns]\n",
      "            comment_count\n",
      "year month               \n",
      "2008 10          2.000000\n",
      "     11          3.250000\n",
      "     12          1.666667\n",
      "     13          5.200000\n",
      "     14          7.000000\n",
      "...                   ...\n",
      "2015 5         323.639344\n",
      "     6         311.950000\n",
      "     7         334.444444\n",
      "     8         313.440678\n",
      "     9         371.603774\n",
      "\n",
      "[382 rows x 1 columns]\n"
     ]
    }
   ],
   "source": [
    "## adopted from https://stackoverflow.com/questions/48058304/how-to-apply-series-in-isocalendar-function-in-pandas-python\n",
    "## Fix 2 \n",
    "all_weekend = counts.loc[(counts['date'].dt.dayofweek==5)|(counts['date'].dt.dayofweek==6)]\n",
    "all_weekday = counts.loc[(counts['date'].dt.dayofweek!=5)& (counts['date'].dt.dayofweek!=6)]\n",
    "all_weekend = all_weekend.copy()\n",
    "all_weekday = all_weekday.copy()\n",
    "#counts[\"year\"] = counts[\"date\"].apply(lambda x: str(x.isocalendar()[0]) )\n",
    "#counts[\"month\"] = counts[\"date\"].apply(lambda x: str(x.isocalendar()[1]) )\n",
    "\n",
    "\n",
    "all_weekend[\"year\"] = all_weekend[\"date\"].apply(lambda x: str(x.isocalendar()[0]) )\n",
    "all_weekend[\"month\"] = all_weekend[\"date\"].apply(lambda x: str(x.isocalendar()[1]) )\n",
    "\n",
    "all_weekday[\"year\"] = all_weekday[\"date\"].apply(lambda x: str(x.isocalendar()[0]) )\n",
    "all_weekday[\"month\"] = all_weekday[\"date\"].apply(lambda x: str(x.isocalendar()[1]) )\n",
    "\n",
    "aggregated_weekend = all_weekend.groupby(['year', 'month']).mean()\n",
    "aggregated_weekday = all_weekday.groupby(['year', 'month']).mean()\n",
    "#aggregated = counts.groupby(['year', 'month']).mean()\n",
    "print(aggregated_weekend)\n",
    "print(aggregated_weekday)\n",
    "#print(aggregated)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 233,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6.804952118330573e-09\n"
     ]
    }
   ],
   "source": [
    "ttest = stats.ttest_ind(aggregated_weekend[\"comment_count\"],aggregated_weekday[\"comment_count\"])\n",
    "print(ttest.pvalue)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 231,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "normality  1.5508062713375688e-59\n",
      "normality  7.48833352976539e-27\n",
      "equal variance p-value:  0.328428138503014\n"
     ]
    }
   ],
   "source": [
    "a_weekend_n = stats.normaltest(aggregated_weekend[\"comment_count\"])\n",
    "print(\"normality \",a_weekend_n.pvalue)\n",
    "a_weekday_n = stats.normaltest(aggregated_weekday[\"comment_count\"])\n",
    "print(\"normality \",a_weekday_n.pvalue)\n",
    "stat,p= stats.levene(aggregated_weekend[\"comment_count\"],aggregated_weekday[\"comment_count\"])\n",
    "print(\"equal variance p-value: \",p)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 232,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\leonwu\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\numpy\\core\\_asarray.py:83: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray\n",
      "  return array(a, dtype, copy=False, order=order)\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure()\n",
    "plt.hist((aggregated_weekend[\"comment_count\"],aggregated_weekday[\"comment_count\"]),label = ['weekend','weekday'])\n",
    "plt.legend(loc='upper right')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 243,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MannwhitneyuResult(statistic=15099.0, pvalue=8.624453234733935e-53)\n"
     ]
    }
   ],
   "source": [
    "##fix 3\n",
    "weekend = filtered.loc[(filtered['date'].dt.dayofweek==5)|(filtered['date'].dt.dayofweek==6)]\n",
    "weekday = filtered.loc[(filtered['date'].dt.dayofweek!=5)& (filtered['date'].dt.dayofweek!=6)]\n",
    "u_test = stats.mannwhitneyu(weekend[\"comment_count\"],weekday[\"comment_count\"],alternative = 'two-sided')\n",
    "print(u_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
