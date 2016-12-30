import pandas as pd
import numpy as np
import csv as csv
from sklearn.tree import DecisionTreeClassifier

# Data clean up for train data
df = pd.read_csv('train.csv', header=0)

# Create colum for gender with numerical values
df['Gender'] = df['Sex'].map({'male':0, 'female':1}).astype(int)

# Determines if person is classified as a child, adult, or senior
def func(x):
    if x < 18: # Child
        return 0
    elif x < 55: # Adult
        return 1
    else: # Senior
        return 2

# Creates a new column with age classifications
df['AgeCat'] = df['Age'].map(lambda x: func(x))

# Remove elements with null value for age
df = df[df['Age'].notnull()][['Survived', 'Gender', 'Pclass', 'AgeCat']]

# Get data for prediction
data = df.values

# Data clean up for train data
test_df = pd.read_csv('test.csv', header=0)

# Create colum for gender with numerical values
test_df['Gender'] = test_df['Sex'].map({'male':0, 'female':1}).astype(int)

# Creates a new column with age classifications
test_df['AgeCat'] = test_df['Age'].map(lambda x: func(x))

# Extract passenger ids before dropping those values
ids = test_df['PassengerId'].values

# Remove elements with null value for age
test_df = test_df[['Gender', 'Pclass', 'AgeCat']]

# Get data for prediction
test_data = test_df.values

print 'Training'
tree = DecisionTreeClassifier()
tree = tree.fit(data[0::,1::], data[0::,0])
print 'Predicting...'
output = tree.predict(test_data).astype(int)


predictions_file = open("mysecondforest.csv", "wb")
open_file_object = csv.writer(predictions_file)
open_file_object.writerow(["PassengerId","Survived"])
open_file_object.writerows(zip(ids, output))
predictions_file.close()
print 'Done.'
