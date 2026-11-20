'''
1. A boolean filter checks every row in a DataFrame agaisnt a condition 
(producing True or False for each row) and keeps only the rows where the condition evaluates to True. 

2. df['revenue'] returns a 1-dimensional pandas Series, while [['revenue']] returns a 2-dimensional pandas DataFrame.
This distinction matters when passing data into function or mehtods that strictly expect a 2D DataFrame versus 1D Series operations. 

3. Reproducibility and automation: in pandas, every filtering, calculation, and cleaning step is saved in a script that can be re-run instantly 
on updated or massive datasets with zero manual clicking or risk of accidental cell edits. 
'''

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


print('--- Exercise 3 ---')
print(df.sort_values('revenue', ascending = False).head(5))


print('--- Exercise 4 ---')
big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]
print(len(big_south))
print(big_south.head())


print('--- Exercise 5 ---')

df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print(df['per_unit'].mean())


print('--- Exercise 6 ---')
print(df['region'].unique())
print(df['region'].value_counts())


print('--- Exercise 7 ---')
subset_df = df[['region', 'product', 'revenue']]
print(subset_df.shape)


print('--- Exercise 8 ---')
df.to_csv('data/explored.csv', index = False)
print('Saved data/explored.csv successfully')