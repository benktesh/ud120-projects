#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r+"))

#Find the lenght of the dictionary
no_of_people = len(enron_data) 
print "no_of_people: ", no_of_people

#Find number of features
no_of_features = len(enron_data[enron_data.keys()[0]])
print "no_of_features: ", no_of_features

#Check the attrbitues
print(enron_data[enron_data.keys()[0]])

#NumberOfPOI
#data[PersonName][Poi] = 1;

count = 0
# Iterate over all the items in dictionary and filter items which has correctkeys 
for (key, val) in enron_data.items():
   if(val['poi']):
       count= count+1
print 'Numbe of poi: ', count

#avoid loop and use lambda
newDict = dict(filter(lambda (key,val) : val['poi'], enron_data.items()))
count = len(newDict)


print 'Numbe of poi: ', count

import sys
sys.path.append('../final_project/')
from poi_email_addresses import poiEmails 

print '# of Poi emails: ', len(poiEmails())

names = open("../final_project/poi_names.txt", "r")
#first three lines are headers
print "Number of names ", len(names.readlines()[2:])

print "James Prince, total stock value: ", enron_data['PRENTICE JAMES']['total_stock_value']



#find the keys
print enron_data['PRENTICE JAMES'].keys()

print "Email from this to poi: ", enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print enron_data['SKILLING JEFFREY K']



#Check names in order
for name in sorted(enron_data.keys()):
    print name

#Find total payments
print(enron_data['FASTOW ANDREW S']['total_payments'])
print(enron_data['LAY KENNETH L']['total_payments'])
print(enron_data['SKILLING JEFFREY K']['total_payments'])

#find the features
#for name in sorted(enron_data.keys()):
#    print enron_data[name]


#Find records with salary
with_salary = dict(filter(lambda (key,val) : val['salary'] != 'NaN', enron_data.items()))
#Find records with email
with_email = dict(filter(lambda (key,val) : val['email_address'] != 'NaN', enron_data.items()))

print 'With email: ', len(with_email)
print 'With Salary: ', len(with_salary)


with_total_payments = dict(filter(lambda (key,val) : val['total_payments'] == 'NaN', enron_data.items()))
print 'without_total_payments:', len(with_total_payments)
print 'without_total_payments %: ', len(with_total_payments)*1.0/len(enron_data.keys()) * 100

with_total_payments = dict(filter(lambda (key,val) : val['total_payments'] == 'NaN' and val['poi'] == True, enron_data.items()))
print 'without_total_payments_poi %: ', len(with_total_payments)*1.0/len(enron_data.keys()) * 100

# When we add 10 more data point with poi==True and Total_payment == NAN
# We willl have 21 + 10 = 31 records with poi==True and Total_payment == NAN and total increases from 146 to 156
# And without_total_payments_poi becomes 21.23%
print "Current length: ", len(enron_data.keys())
print (31.0/len(enron_data.keys()))


#new number of poi: is really 10 more than what is in dataset
poi = dict(filter(lambda (key,val) : val['poi'] == True, enron_data.items()))
print 'New Number of Poi: ', len(poi)+10