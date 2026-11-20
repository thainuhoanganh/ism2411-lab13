import pandas as pd

print('--- Exercise 1 ---')
df = pd.read_csv('data/retail_sales.csv')
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)


print('--- Exercise 2 ---')
south = df[df['region'] == 'South']
print(len(south))
print(south.head())