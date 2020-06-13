#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
sys.path.append("../choose_your_own/")
from email_preprocess import preprocess
from sklearn.tree import DecisionTreeClassifier 
import pprint

from class_vis import prettyPicture, output_image
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl


def classify(features_train, labels_train):
    clf = DecisionTreeClassifier(min_samples_split=40)
    clf = clf.fit(features_train, labels_train)
    return clf

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

print(len(features_train[0]))
clf = classify(features_train, labels_train)
clf.predict(features_test)
acc = clf.score(features_test, labels_test)

print(acc)
