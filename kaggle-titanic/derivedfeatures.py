import re

def deriveFeatures(df):
    extractTitle(df)
    extractCabin(df)
    groupFares(df)
    groupAges(df)
    extractFamilySize(df)


def extractTitle(df):
    df['Title'] = df.Name.map(lambda x: mapTitle(x))

def mapTitle(name):
    if re.match('.*mr\.', name, re.IGNORECASE):
        return 1
    if re.match('.*miss\.', name, re.IGNORECASE):
        return 1
    if re.match('.*mrs\.', name, re.IGNORECASE):
        return 1
    if re.match('.*master\.', name, re.IGNORECASE):
        return 1
    if re.match('.*mme\.', name, re.IGNORECASE):
        return 2
    if re.match('.*dr\.', name, re.IGNORECASE):
        return 3
    if re.match('.*major\.', name, re.IGNORECASE):
        return 3
    if re.match('.*rev\.', name, re.IGNORECASE):
        return 4
    if re.match('.*col\.', name, re.IGNORECASE):
        return 3
    if re.match('.*sir\.', name, re.IGNORECASE):
        return 2
    if re.match('.*ms\.', name, re.IGNORECASE):
        return 1
    if re.match('.*lady\.', name, re.IGNORECASE):
        return 2
    if re.match('.*capt\.', name, re.IGNORECASE):
        return 3
    if re.match('.*mlle\.', name, re.IGNORECASE):
        return 2
    return 4

def extractCabin(df):
    df['Cabin'] = df.Cabin.map(lambda x: mapCabin(x))

def mapCabin(cabin):
    if 'A' in cabin:
        return 1
    if 'B' in cabin:
        return 1
    if 'C' in cabin:
        return 1
    if 'D' in cabin:
        return 1
    if 'E' in cabin:
        return 2
    if 'F' in cabin:
        return 2
    if 'G' in cabin:
        return 2
    if 'U' in cabin:
        return 2

    return 2

def groupAges(df):
    df['AgeGroup'] = df.Age.map(lambda x: getAgeGroup(x))

def groupFares(df):
    df['FareGroup'] = df.Fare.map(lambda x: getFareGroup(x))

def getAgeGroup(age):
    if age < 15 :
        return 1
    if age < 35 :
        return 2

    return 3

def getFareGroup(fare):
    if fare < 20:
        return 1
    if fare < 40:
        return 2
    if fare < 100:
        return 3
    return 4


def extractFamilySize(df):
    df['FamilySize'] = df.SibSp + df.Parch
