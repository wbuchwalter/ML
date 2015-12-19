import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from learningcurves import graphLearningCurves

print('reading...')
df = pd.read_csv('./data/train.csv', header = 0)
test_df = pd.read_csv('./data/test.csv', header = 0)
print('ok')

forest = RandomForestClassifier(n_estimators=100)
X = df.values[:,1::]
y = df.values[:,0]

print('fitting...')
forest = forest.fit(X,y)
print('ok')
print('predicting...')
output = forest.predict(test_df.values)
print('ok')

graphLearningCurves(forest, X, y)

'''
print('writing result...')
resultdf = pd.DataFrame(output,columns=['Label'])
resultdf.index += 1
resultdf.to_csv('./result/randForest.csv', index=True,index_label='ImageId',)
print('ok')
'''