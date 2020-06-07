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
from sklearn.svm import SVC


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

def runMuiltipleCs(CS, features_train_subset, labels_train_subset,features_test,labels_test ):
    print 'Testing %d values to get optimal value for c on subset', len(CS) 
    selectedC = CS[0]
    maxAcc = -1
    for c in CS:    
        pred, testingTime, trainingTime, acc = createAndPredict(c, features_train_subset, labels_train_subset, features_test, labels_test)
        if(acc > maxAcc):
            selectedC = c
            maxAc = acc
        result.append({"C": c, "accuracy": acc, "testingTime":testingTime, "trainingTime": trainingTime })
    return result, selectedD, maxAcc 

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#by default C=10000
selectedC = 10000 
optimizeC = False
useSubset = False


features_train_subset = features_train[:len(features_train)/100]
labels_train_subset = labels_train[:len(labels_train)/100]

if(optimizeC):
    result, selC, maxAcc = runMuiltipleCs(CS, features_train_subset, labels_train_subset, features_test, labels_test)
    pprint.pprint(result)
    selectedC = selC


if(not useSubset):
    pred, testingTime, trainingTime, acc = createAndPredict(selectedC, features_train, labels_train, features_test, labels_test)
else: 
    pred, testingTime, trainingTime, acc = createAndPredict(selectedC, features_train_subset, labels_train_subset, features_test, labels_test)

print "Value 1: ", len(pred[pred==1])
print "Value 0: ", len(pred[pred==0])

print 'Testing Time', testingTime, "s."
print 'Training Time', trainingTime, "s." 
print 'Accuracy: ', acc * 100 , "%."

print "Prediction for 10, 26 50: ",  pred[[10, 26, 50]]












