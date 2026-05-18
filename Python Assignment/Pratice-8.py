# Generated from: Pratice-8.ipynb
# Converted at: 2026-01-10T09:13:17.899Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Day 8 – Merge, Join, Concat: 10 Questions
# ## Question 1
# ### Create `df_customers` (`customer_id`, `name`) and `df_orders` (`order_id`, `customer_id`).
# #### Perform inner merge on `customer_id`.


import pandas as pd
import numpy as np

df_customers = pd.DataFrame({'customer_id': [1, 2, 3],'name': ['A', 'B', 'C']})
df_orders = pd.DataFrame({'order_id': [101, 102, 103],'customer_id': [1, 2, 2]})

merge=df_customers.merge(df_orders,on='customer_id',how='inner')

merge

# ## Question 2
# ### Perform left and right merge on `customer_id` for these DataFrames.
# #### Compare row counts.


left=df_customers.merge(df_orders,on='customer_id',how='left')
left

right=df_customers.merge(df_orders,on='customer_id',how='right')
right

print(f"Left_Rows:{len(left)},Right_Rows:{len(right)}")

# ## Question 3
# ### Create `df1(id, value1)` and `df2(id, value2)` with partially overlapping `id`.
# #### Perform outer merge and print result.


df1 = pd.DataFrame({'id': [1, 2], 'value1': [10, 20]})
df2 = pd.DataFrame({'id': [2, 3], 'value2': [200, 300]})

merge_overlap=df1.merge(df2,on='id',how='outer')
merge_overlap

# ## Question 4
# ### Create two monthly DataFrames with same columns.
# #### Concatenate vertically and reset index.


m1 = pd.DataFrame({'id': [1, 2, 3],'sales': [100, 150, 200]})
m2 = pd.DataFrame({'id': [4, 5, 6],'sales': [120, 180, 210]})

df=pd.concat([m1,m2],ignore_index=True,axis=0)
df

# ## Question 5
# ### Create two DataFrames with same index but different columns.
# #### Concatenate horizontally (`axis=1`).


m1 = pd.DataFrame({'id': [1, 2, 3],'sales': [100, 150, 200]})
m2 = pd.DataFrame({'customer_id': [4, 5, 6],'customer_sales': [120, 180, 210]})

df=pd.concat([m1,m2],ignore_index=True,axis=1)
df

# ## Question 6
# ### Show how to add a new row to a DataFrame by concatenating with a single-row DataFrame.


m3=pd.DataFrame({'A':[5],'B':[6]})

df3=pd.concat([df,m3],ignore_index=True)

df3

# ## Question 7
# ### Create two DataFrames where one has extra keys.
# #### Left merge with `indicator=True`.
# #### Filter rows available only in left.


df4 = pd.DataFrame({'key': [1, 2], 'A': ['x', 'y']})
df5 = pd.DataFrame({'key': [2, 3], 'B': ['p', 'q']})

merge=df4.merge(df5,on='key',how='left',indicator=True)
merge

filter=merge[merge['_merge']=='left_only']

filter

# ## Question 8
# ### Demonstrate merge on multiple keys, e.g. `['city', 'year']`.


df6 = pd.DataFrame({'city': ['A', 'A'], 'year': [2024, 2025], 'val1': [1, 2]})
df7 = pd.DataFrame({'city': ['A', 'B'], 'year': [2024, 2025], 'val2': [10, 20]})

merge1=df6.merge(df7,how='inner',on=['city','year'])
merge1

merge2=df6.merge(df7,how='left',on=['city','year'])
merge2

# ## Question 9
# ### Create a product DataFrame and discount DataFrame.
# #### Merge and compute final price after discount.


products = pd.DataFrame({'prod_id': [1, 2], 'price': [100, 200]})
disc = pd.DataFrame({'prod_id': [1, 2], 'discount': [0.1, 0.2]})

m=products.merge(disc,how='inner',on='prod_id')
m

m['final_price']=m['price']*(1-m['discount'])
m

# ## Question 10
# ### Use `pd.concat` with `keys` to create a hierarchical index for two DataFrames.


df8 = pd.DataFrame({'A': [10, 20]})
df9 = pd.DataFrame({'A': [30, 40]})

merge=pd.concat({'first':df8,'second':df9})
merge