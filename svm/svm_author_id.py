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
from sklearn.metrics import accuracy_score


def createAndPredict(c, features_train, labels_train, features_test, labels_test):
    clf = SVC(kernel="rbf", C = c)

    t0 = time()
    clf.fit(features_train, labels_train)
    trainingTime = round(time()-t0, 3),

    t0 = time()
    pred = clf.predict(features_test)
    testingTime = round(time()-t0, 3)
    accuracy = accuracy_score(pred, labels_test)
    return pred, testingTime, trainingTime, accuracy

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


features_train_subset = features_train[:len(features_train)/100]
labels_train_subset = labels_train[:len(labels_train)/100]

#########################################################
### your code goes here ###
from sklearn.svm import SVC

result = []
CS = [10, 100, 1000, 10000]


#CS = [10000]
selectedC = CS[0]
maxAcc = -1
print 'Testing %d values to get optimal value for c on subset', len(CS) 
for c in CS:    


    pred, testingTime, trainingTime, acc = createAndPredict(c, features_train_subset, labels_train_subset, features_test, labels_test)
    
    if(acc > maxAcc):
        selectedC = c
        maxAc = acc
    result.append({"C": c, "accuracy": acc, "testingTime":testingTime, "trainingTime": trainingTime })

pprint.pprint(result)
print '............Done testing four C values'

#final result
print "Running final with C: ", selectedC , "full data"
pred, testingTime, trainingTime, acc = createAndPredict(c, features_train, labels_train, features_test, labels_test)

print 'Testing Time', testingTime, "s."
print 'Training Time', trainingTime, "s." 
print 'Accuracy: ', acc * 100 , "%."





