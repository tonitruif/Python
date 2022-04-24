import pandas as pd

df = pd.read_csv("9_6.csv")
count = 0
for index, row in df.iterrows():
    if row['a'] + row['b'] > row['c'] and row['a'] + row['c'] > row['b'] and row['b'] + row['c'] > row['a']:
        count += 1
print(count)