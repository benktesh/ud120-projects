#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
import pprint


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

#########################################################
### your code goes here ###
from sklearn.svm import SVC

result = []
CS = [10, 100, 1000, 10000]

print 'Testing four C values'
for c in CS:    
    clf = SVC(kernel="rbf", C = c)

    t0 = time()
    clf.fit(features_train, labels_train)
    print "Training time:", round(time()-t0, 3), "s"



    t0 = time()
    pred = clf.predict(features_test)
    print 'Testing time:', round(time()-t0, 3), "s"

    #########################################################
    from sklearn.metrics import accuracy_score
    acc = accuracy_score(pred, labels_test)
    print "Accuracy from SVM: "
    print(acc)

    result.append({"C": c, "accuracy": acc})

pprint.pprint(result)
print '............Done testing four C values'