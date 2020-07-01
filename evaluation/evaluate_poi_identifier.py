#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.3, random_state=42)
clf = DecisionTreeClassifier()
clf.fit(features_train,labels_train)
score = clf.score(features_test,labels_test)
print ("Score: ", score)


import numpy as np
predicted_test = clf.predict(features_test)

print (len([e for e in predicted_test if e == 1.0]))
print (len(labels_test))



# identifier prediected 0.
print 1.0 - 4.0/29


#find precision
from sklearn.metrics import * 
ps = precision_score(labels_test,clf.predict(features_test))
print("Presiion : ", ps)

#find recall
print ("Recall :", recall_score(labels_test,clf.predict(features_test)))


predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

true_positive = 0
for i in range(len(predictions)): 
    if( predictions[i] == true_labels[i] == 1):
        true_positive = true_positive+1

print "True positive: ", true_positive


#Find true negative
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]


true_negative = 0
for i in range(len(predictions)): 
    if( predictions[i] == true_labels[i] == 0):
        true_negative = true_negative+1

print "True negative: ", true_negative


#find false positive
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

false_positive = 0
for i in range(len(predictions)): 
    if( predictions[i] != true_labels[i] and predictions[i] == 1):
        false_positive = false_positive+1

print "False positive: ", false_positive


#find false negative
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

false_negative = 0
for i in range(len(predictions)): 
    if( predictions[i] != true_labels[i] and predictions[i] == 0):
        false_negative = false_negative+1

print "False negative: ", false_negative


#find precision
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

print "Precision score ", precision_score(true_labels,predictions)

#find recall
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

print "Recall :", recall_score(true_labels,predictions)