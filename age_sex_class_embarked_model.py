import pandas as pd
import numpy as np
import random as rand
import csv as csv
from sklearn.tree import DecisionTreeClassifier

# Data clean up for train data
df = pd.read_csv('train.csv', header=0)

# Create column for gender with numerical values
df['Gender'] = df['Sex'].map({'male':0, 'female':1}).astype(int)

# Create column for embarked with numerical values
# If no value is originally given, a random value is assigned
df['EmbarkedCat'] = df['Embarked'].map({'C':0, 'S':1, 'Q':2, 'Na': rand.randrange(0,3) - 1}).astype(int)

# Creates a new column with age classifications
df['AgeCat'] = df['Age'].map(lambda x: 0 if x < 18 else 1 if x < 55 else 2).astype(int)

# Remove elements with null value for age
df = df[df['Age'].notnull()][['Survived', 'Gender', 'Pclass', 'AgeCat', 'EmbarkedCat']]

# Get data for prediction
data = df.values

# Data clean up for train data
test_df = pd.read_csv('test.csv', header=0)

# Create colum for gender with numerical values
test_df['Gender'] = test_df['Sex'].map({'male':0, 'female':1}).astype(int)

# Creates a new column with age classifications
test_df['AgeCat'] = test_df['Age'].map(lambda x: 0 if x < 18 else 1 if x < 55 else 2).astype(int)

# Create column for embarked with numerical values
# If no value is originally given, a random value is assigned
test_df['EmbarkedCat'] = test_df['Embarked'].map({'C':0, 'S':1, 'Q':2, 'Na': rand.randrange(0,3) - 1}).astype(int)

# Extract passenger ids before dropping those values
ids = test_df['PassengerId'].values

# Remove elements with null value for age
test_df = test_df[['Gender', 'Pclass', 'AgeCat', 'EmbarkedCat']]

# Get data for prediction
test_data = test_df.values

print 'Training'
tree = DecisionTreeClassifier()
tree = tree.fit(data[0::,1::], data[0::,0])
print 'Predicting...'
output = tree.predict(test_data).astype(int)


predictions_file = open("mythirdforest.csv", "wb")
open_file_object = csv.writer(predictions_file)
open_file_object.writerow(["PassengerId","Survived"])
open_file_object.writerows(zip(ids, output))
predictions_file.close()
print 'Done.'


                

        
