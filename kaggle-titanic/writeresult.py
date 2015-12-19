import numpy as np
import pandas as pd

def writeResultToCSV(output):
    passengerIds = pd.read_csv('./data/test.csv', header = 0).PassengerId.values
    finaldf = pd.DataFrame(np.int_(np.array(output)), index = passengerIds, columns=['Survived'])
    finaldf.index.name = 'PassengerId'
    finaldf.to_csv('./result/out.csv')
