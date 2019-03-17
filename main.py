import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
import numpy as np

all_data = pd.read_csv('forest_dataset.csv')

labels = all_data[all_data.columns[-1]].values
feature_matrix = all_data[all_data.columns[:-1]].values

#print(feature_matrix)

train_feature_matrix, test_feature_matrix, train_labels, test_labels = train_test_split(feature_matrix, labels,test_size=0.2, random_state=42)
#print(train_feature_matrix)
scaler = StandardScaler()
train_feature_matrix = scaler.fit_transform(train_feature_matrix)
test_feature_matrix = scaler.fit_transform(test_feature_matrix)
#print(train_feature_matrix)

clf = KNeighborsClassifier()
clf.fit(train_feature_matrix, train_labels)
print(train_labels)
train_labels = train_labels.reshape(-1,1)
print(train_labels)
pred_labels = clf.predict(test_feature_matrix)
#accuracy_score(test_labels, pred_labels)
print(len(test_labels))
print(len(pred_labels))
print(accuracy_score(test_labels, pred_labels))
'''
params = {'weights': ['uniform', 'distance'], 'n_neighbors': [1,2,3,4,5,6,7,8,9,10], 'metric': ['manhattan', 'euclidean']}
train_labels = np.ravel(train_labels)
clf_grid = GridSearchCV(clf, params, cv=5, scoring='accuracy', n_jobs=-1)
clf_grid.fit(train_feature_matrix, train_labels)
print(clf_grid.best_params_)
'''
optimal_clf = KNeighborsClassifier(n_neighbors=4, weights='distance', metric='manhattan')
optimal_clf.fit(train_feature_matrix, train_labels)
pred_prob = optimal_clf.predict_proba(test_feature_matrix)
print(pred_prob)

unique, freq = np.unique(test_labels, return_counts=True)
freq = list(map(lambda x: x / len(test_labels),freq))

pred_freq = pred_prob.mean(axis=0)
plt.figure(figsize=(10, 8))
plt.bar(range(1, 8), pred_freq, width=0.4, align="edge", label='prediction')
plt.bar(range(1, 8), freq, width=-0.4, align="edge", label='real')
plt.legend()
#plt.show()
print(pred_prob[2],pred_freq[2])