import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None

def importData(filename):
    from numpy import float32
    df = pd.read_csv('./data/' + filename + '.csv', header = 0)

    #data cleaning
    mapSex(df)
    mapOrigin(df)
    cleanFare(df)
    cleanAge(df)
    cleanCabin(df)

    return df


def mapSex(df):
    df['Gender'] = df.Sex.map({'female': 0, 'male': 1})

def mapOrigin(df):
    #fill missing origin
    df.Embarked[df.Embarked.isnull()] = df.Embarked.dropna().mode().values

    #map origin
    df['EmbarkedInt'] = df.Embarked.map({'C': 0, 'Q': 1, 'S': 2})

def cleanFare(df):
    #fill missing fares
    df.Fare[np.isnan(df.Fare)] = df.Fare.median()

def cleanAge(df):
    #fill missing ages
    median_ages = np.zeros((2,3))
    for i in range(0, 2):
        for j in range(0, 3):
            median_ages[i,j] = df[(df['Gender'] == i) & (df['Pclass'] == j+1)]['Age'].dropna().median()

    df['AgeFill'] = df.Age
    for i in range(0, 2):
        for j in range(0, 3):
            df.loc[ (df.Age.isnull()) & (df.Gender == i) & (df.Pclass == j+1),                    'AgeFill'] = median_ages[i,j]

def cleanAgeSimple(df):
    df.Age[np.isnan(df.Age)] = df.Age.median()


def cleanCabin(df):
    #fill missing cabin
    df.Cabin[df.Cabin.isnull()] = 'U0'
