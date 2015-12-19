from importdata import importData
from derivedfeatures import deriveFeatures
from writeresult import writeResultToCSV
from sklearn.ensemble import RandomForestClassifier
from learningcurves import graphLearningCurves
import numpy as np

#import data
train_data = importData('train')
test_data = importData('test')

#add new features
deriveFeatures(train_data)
deriveFeatures(test_data)

#drop unused columns
train_data = train_data.drop(['Name', 'Fare', 'SibSp', 'Parch', 'AgeFill', 'Sex', 'Ticket', 'Embarked', 'Age', 'PassengerId'], axis=1)
test_data = test_data.drop(['Name', 'Fare', 'SibSp', 'Parch', 'AgeFill', 'Sex', 'Ticket', 'Embarked', 'Age', 'PassengerId'], axis=1)


X = train_data.astype(np.float32).values[:,1::]
y = train_data.astype(np.float32).values[:,0]

forest = RandomForestClassifier(n_estimators = 100, max_depth=7, min_samples_split=4, n_jobs=-1, random_state=115)
forest = forest.fit(X,y)

print(forest.score(X,y))


#output = forest.predict(test_data.astype(np.float32).values)
#writeResultToCSV(output)

graphLearningCurves(forest,X,y)