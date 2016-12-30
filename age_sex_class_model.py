import random
import pandas as pd
import numpy as np
import csv as csv
from sklearn.tree import DecisionTreeClassifier

# Data cleanup for train data
df = pd.read_csv('train.csv', header=0)

# Create column for gender with numerical values 
df['Gender'] = df['Sex'].map({'male':0, 'female':1}).astype(int)

# Creates a new column with age classifications
df['AgeCat'] = df['Age'].map(lambda x: 0 if x < 18 else 1 if x < 55 else 2).astype(int)

# Calculates median ages for each combination of gender, pclass, and agecat
median_ages = np.zeros((2,3,3))
for i in range(0,2) :
    for j in range(0,3):
        for k in range(0,3):
            median_ages[i,j,k] = df[(df['Gender'] == i) & \
                                    (df['Pclass'] == j+1) & \
                                    (df['AgeCat'] == k)]['Age'].dropna().median()
# Puts in median ages
# Gender and pclass are taken into account but agecat is random
for i in range(0, 2):
    for j in range(0, 3):
        df.loc[ (df.Age.isnull()) & (df.Gender == i) & (df.Pclass == j+1),\
                'Age'] = median_ages[i,j,andom.randrange(0,3)]

# New agecat values are calculated since all people now have a value for age           
df['AgeCat'] = df['Age'].map(lambda x: func(x))

# Drop unneeded categories
df = df.drop(['Name','Sex', 'Ticket', 'Cabin', 'Embarked', 'Age', 'SibSp', 'Parch', 'Fare', 'PassengerId'], axis=1)

data = df.values

# Data cleanup for test data
test_df = pd.read_csv('test.csv', header=0)

# Create column for gender with numerical values 
test_df['Gender'] = test_df['Sex'].map({'male':0, 'female':1}).astype(int)


# Creates a new column with age classifications
test_df['AgeCat'] = test_df['Age'].map(lambda x: 0 if x < 18 else 1 if x < 55 else 2).astype(int)

# Calculates median ages for each combination of gender, pclass, and agecat
median_test_ages = np.zeros((2,3,3))
for i in range(0,2) :
    for j in range(0,3):
        for k in range(0,3):
            median_ages[i,j,k] = test_df[(df['Gender'] == i) & \
                                    (test_df['Pclass'] == j+1) & \
                                    (test_df['AgeCat'] == k)]['Age'].dropna().median()
# Puts in median ages
# Gender and pclass are taken into account but agecat is random
for i in range(0, 2):
    for j in range(0, 3):
        test_df.loc[ (test_df.Age.isnull()) & (test_df.Gender == i) & (test_df.Pclass == j+1),\
                'Age'] = median_test_ages[i,j,random.randrange(0,3)]

# New agecat values are calculated since all people now have a value for age           
test_df['AgeCat'] = test_df['Age'].map(lambda x: func(x))

ids = test_df['PassengerId'].values

# Drop unneeded categories
test_df = test_df.drop(['Name','Sex', 'Ticket', 'Cabin', 'Embarked', 'Age', 'SibSp', 'Parch', 'Fare', 'PassengerId'], axis=1)

data = df.values
test_data = test_df.values

print 'Training'
tree = DecisionTreeClassifier()
tree = tree.fit(data[0::,1::], data[0::,0])
print 'Predicting...'
output = tree.predict(test_data).astype(int)


predictions_file = open("myfirstforest.csv", "wb")
open_file_object = csv.writer(predictions_file)
open_file_object.writerow(["PassengerId","Survived"])
open_file_object.writerows(zip(ids, output))
predictions_file.close()
print 'Done.'
