#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier

import pprint

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
#plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

def classifiyKNN(features_train, labels_train):
    clf = KNeighborsClassifier(n_neighbors=3, algorithm="ball_tree")
    clf = clf.fit(features_train, labels_train)
    return clf

def classifiyKNN(features_train, labels_train):
    clf =KNeighborsClassifier(n_neighbors=3, algorithm="ball_tree")
    clf = clf.fit(features_train, labels_train)
    return clf

def classifyAdaBoost(features_train, labels_train):
    clf = AdaBoostClassifier(n_estimators=1000, random_state=0)
    clf = clf.fit(features_train, labels_train)
    return clf

def classifyFandomForest(features_train, labels_train):
    clf = RandomForestClassifier(max_depth=2, random_state=0)
    clf = clf.fit(features_train, labels_train)
    return clf

def runKNN():
    clf = classifiyKNN(features_train, labels_train)
    clf.predict(features_test)
    prettyPicture(clf, features_test, labels_test, "bumpiness", "grade", "knn.png")
    acc = clf.score(features_test, labels_test) 
    return acc


def runAdaBoost():
    clf = classifyAdaBoost(features_train, labels_train)
    clf.predict(features_test)
    acc = clf.score(features_test, labels_test) 
    prettyPicture(clf, features_test, labels_test, "bumpiness", "grade", "adaBoost.png")
    return acc

def runRandomForest():
    clf = classifyFandomForest(features_train, labels_train)
    clf.predict(features_test)
    acc = clf.score(features_test, labels_test) 
    prettyPicture(clf, features_test, labels_test, "bumpiness", "grade", "randomForest.png")
    return acc


summary = []
summary.append({"model": "KNN",  "acc": runKNN()})
summary.append({"model": "adaBoost",  "acc": runAdaBoost()})
summary.append({"model": "random forest",  "acc": runRandomForest()})

pprint.pprint(summary)
