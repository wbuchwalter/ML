import pandas as pd

df = pd.read_csv('./data/train.csv', header = 0)
df[0:10000].to_csv('./data/train10k.csv', header = 1)