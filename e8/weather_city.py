import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage.color import lab2rgb
from skimage.color import rgb2lab
import sys
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import sys
from sklearn.preprocessing import StandardScaler

monthly_data_labelled = sys.argv[1]
monthly_data_unlabelled= sys.argv[2]
labels = sys.argv[3]

data = pd.read_csv(monthly_data_labelled)
X = data.iloc[:,2:62]
y = data['city']
X_train, X_valid, y_train, y_valid = train_test_split(X, y)
#print(X)

bayes_rgb_model = GaussianNB()

knn_rgb_model = make_pipeline(StandardScaler(),KNeighborsClassifier(n_neighbors = 12))
rf_rgb_model = make_pipeline(StandardScaler(),DecisionTreeClassifier(max_depth = 13))

models = [bayes_rgb_model, knn_rgb_model, rf_rgb_model]
models_name = ['baye_model', 'knn_model', 'rf_model']
for i, m in enumerate(models):  # yes, you can leave this loop in if you want.
    m.fit(X_train, y_train)

    print(models_name[i],':', m.score(X_valid, y_valid))

unlabel_data = pd.read_csv(monthly_data_unlabelled)
X_test = unlabel_data.iloc[:,2:62]
predictions =  bayes_rgb_model.predict(X_test)
#print(predictions)
pd.Series(predictions).to_csv(sys.argv[3], index=False, header=False)
