import pandas as pd

df = pd.read_csv("9_3.csv")


pos = df.mean(axis=0).values.argmax()
print(df.columns[pos])