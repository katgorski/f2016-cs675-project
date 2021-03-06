#!/usr/bin/env python2

from __future__ import print_function
from sklearn.decomposition import PCA
#from sklearn import svm
import numpy as np
import funct
from sys import argv

script, d_f, l_f = argv

data = funct.Data(d_f, l_f, w0 = False)
labels = data.test_labels
training_data = data.training_rows
#print(labels)

training_data = [data.data[i] for i in training_data]
#print(training_data)
training_labels = [data.labels[i] for i in data.training_rows]

test_data = [data.data[i] for i in labels]

data = np.asarray(training_data)
#print("Original training data")
#print(data)

pca = PCA(n_components = 2)
pca.fit(data)
#print(pca.components_)
data_applied = pca.transform(data)
#print("Training data")
#print(data_applied)

#print("Original test data")
#print(np.asarray(test_data))

test_data_applied = pca.transform(np.asarray(test_data))
#print("Test data")
#print(test_data_applied)
#print(test_data_applied[0])

#clf = svm.SVC()
#clf.fit(data_applied, training_labels)
#predictions = clf.predict(np.asarray(test_data_applied))
#print(predictions)

for i in range(len(training_data)):
    print("%d %f %f" % (training_labels[i], data_applied[i][0], data_applied[i][1]))
