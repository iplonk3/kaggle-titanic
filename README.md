# Kaggle-titanic

These are my submissions for Kaggle's Titanic: Machine Learning from Disaster competition. For this challenge competitors had to use a dataset of Titanic passengers including survival, age, class, gender, and other pertinent information for each passenger to predict which passengers from another dataset would survive the tragedy.

## My Models

### age\_sex\_class\_model.py

For my first submission, I based my model off of the Kaggle's suggestions. I used gender, age, and class to make my predictions. I broke age into three categories: child (<18), adult(18-55), and senior (>55). Since not every passenger had an age specified for him or her, I calculated medians for each gender, class, and age category. Based on the gender and class of each passenger with null age, then, I chose a random age category and assigned that passenger the corresponding median age. Then, I used a decision tree to make my predictions (*myfirstforest.csv*). From this model, I achieved a **0.74641** success rate.

### age\_sex\_class\_nomedian.py

For my second submission, I decided to eliminate the passengers with null age from my dataset. Assuming these passengers were evenly spread over gender, class, and age categories, this would have no impact on my model and could even improve my predictions. Again, I used a decision tree to make my predictions (*mysecondforest.csv*). From this model, I improved on my score and achieved a **0.76077** success rate.

### age\_sex\_class\_embarked\_model.py

For my third and final submission, I decided to keep with my model that eliminated the null ages and include embarkation as another factor (*mythirdforest.csv*). From this model, I improved on my score again and achieved a **0.76555** success rate.

## Conclusion

The most important thing I learned from this exercise is that one of the biggest problems facing data scientists is getting the data in the correct format for manipulation. In my models, I had to decide what to do when a passenger had a null age. First, I thought it would be best to calculate medians and input those in where the field was empty. However, I learned that since passengers with null ages were spread evenly throughout the gender, class, and age categories that the best solution was to drop these passengers for determining my predictions. Additionally, I came up with the idea to factor in a passenger's home country. However, the dataset provided did not included this informatino, so I extracted datasets (separated by class) from Wikipedia which included this information. However, the datasets had this information labeled as hometown and would include city, province/state, country, and/or commonwealth, making extracting the home country more difficult. Once I was able to do this, however, I soon found out that the names for the passengers were not exactly the same. Thus, when I ran a script which would compare the name of each passenger in the Kaggle dataset to the corresponding Wikipedia class dataset, only, for first class passengers for example, 80 out of the 216 passengers had their names matched exactly and could have their home countries extracted correctly. I am still curious in finding out if home country had any impact on likilihood of survival, so I may go back to this model if I have time. Overall, I am content with my models and my improvements with each model. Additionally, I succeeded in meeting Kaggle's success determinant of having a score of .7 or higher.




