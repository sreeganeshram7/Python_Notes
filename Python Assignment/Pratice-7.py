# Generated from: Pratice-7.ipynb
# Converted at: 2026-01-10T09:13:35.601Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Day 7 – GroupBy & Aggregation: 10 Questions
# 
# ## Question 1
# ### Create a sales DataFrame with columns: `region`, `product`, `units`, `price`.
# #### Add `revenue = units * price`.
# #### Group by `region` to find total revenue per region.


import numpy as np
import pandas as pd

df = pd.DataFrame({
    'region': ['North', 'South', 'East', 'West'],
    'product': ['A', 'B', 'C', 'D'],
    'units': [10, 20, 15, 5],
    'price': [100, 300, 200, 150]})

df['revenue']=df['units']*df['price']

df

data=df.groupby('region')['revenue'].sum()

data

# ## Question 2
# ### Group the same DataFrame by `product` and compute:
# #### Total units sold.
# #### Average price.


data_pro=df.groupby('product')['units'].sum()
data_pro

data_avg=df.groupby('product')['price'].mean()
data_avg

# ## Question 3
# ### Create a student DataFrame: `class`, `student`, `marks`.
# #### Group by `class` and find mean and max marks.


df4 = pd.DataFrame({
    'class': ['X', 'X', 'Y', 'Y'],
    'student': ['A', 'B', 'C', 'D'],
    'marks': [80, 90, 70, 75]})

df4.groupby('class')['marks'].mean()

df4.groupby('class')['marks'].max()

# ## Question 4
# ### Use `.agg()` to calculate `min`, `max`, `mean`, `count` for `marks` per `class`.


stats=df4.groupby('class')['marks'].agg(['min','max','mean','count'])

stats

# ## Question 5
# ### Create a DataFrame with `category`, `sub_category`, `value`.
# #### Group by both columns and calculate sum of `value`.
# #### Reset index.


df_cat = pd.DataFrame({
    'category': ['Cat1', 'Cat1', 'Cat2'],
    'sub_category': ['S1', 'S2', 'S1'],
    'value': [10, 20, 30]
})

df_cat

df_cat.groupby(['category','sub_category'])['value'].sum().reset_index()

# ## Question 6
# ### Create `customer_id`, `order_id`, `amount` DataFrame.
# #### Group by `customer_id` to get total and average `amount`.
# #### Sort by total amount descending.


orders = pd.DataFrame({
    'customer_id': [1, 1, 2, 3],
    'order_id': [101, 102, 103, 104],
    'amount': [100, 150, 200, 300]
})

orders

g=orders.groupby('customer_id')['amount'].agg(['sum','mean'])
g

sort=g.sort_values('sum',ascending=False)
sort

# ## Question 7
# #### Use `value_counts()` on a categorical column and convert result to DataFrame with columns `value`, `count`.


df5 = pd.DataFrame({
    "priority": ["Low", "Medium", "High", "Low", "High", "Low"]})
df5

counts_df = df5["priority"].value_counts().reset_index()
counts_df

# ## Question 8
# ### Create a DataFrame with a `date` column and `sales`.
# #### Convert `date` to datetime.
# #### Group by month and sum sales.
# 


d = pd.DataFrame({
    'date': ['2025-01-01', '2025-01-10', '2025-02-05'],
    'sales': [100, 200, 300]
})

d['date']=pd.to_datetime(d['date'])
d['date']

d['month']=d['date'].dt.to_period('M')

d

res=d.groupby('month')['sales'].sum()

res

# ## Question 9
# ### Create `team`, `player`, `score` DataFrame.
# #### Find player with highest score in each team (using `idxmax`).


df = pd.DataFrame({
    "team": ["A", "A", "B", "B", "C", "C"],
    "player": ["P1", "P2", "P3", "P4", "P5", "P6"],
    "score": [50, 80, 60, 90, 70, 85]
})

df

t=df.groupby('team')['score'].idxmax()
t

best=df.loc[t]
best

# ## Question 10
# ### Use `groupby` and `filter` to keep only groups where mean `marks` > 70.


mark=df4.groupby('class').filter(lambda x:x['marks'].mean()>70)

mark