# Generated from: Pratice-4.ipynb
# Converted at: 2026-01-10T09:14:16.890Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Day 4 – pandas Series: 10 Questions
# ## Question 1
# ### Create a pandas Series from `[5, 10, 15, 20]` with index `['p', 'q', 'r', 's']`.
# #### Print the Series.
# #### Access and print the element with index `'r'`.


import pandas as pd
import numpy as np

s=pd.Series([5,10,15,20],index=['p','q','r','s'])
s

s['r']

# ## Question 2
# ### Create a Series from a NumPy array `[2, 4, 6, 8, 10]`.
# #### Print the first 2 elements.
# #### Print the last 2 elements.


a=pd.Series([2,4,6,8,10])
a

a.head(2)

a.tail(2)

# ## Question 3
# ### Create a Series for students' English marks:
# ### Names: `['Ankit', 'Bhavna', 'Chetan', 'Deepa']`
# ### Marks: `[65, 82, 74, 91]`
# 
# ### Find and print:
# #### Average marks
# #### Students scoring more than 80.


names=['Ankit', 'Bhavna', 'Chetan', 'Deepa']
marks=[65,82,74,91]
s=pd.Series(marks,index=names)
s.mean()

s[s>80]

# ## Question 4
# ### Given a Series with cities as index and temperatures as values, show how to:
# #### Select temperatures for a list of cities.
# #### Use boolean indexing to find cities with temperature above 30.


temps = pd.Series([28, 35, 32, 25, 40],index=["Chennai", "Delhi", "Mumbai", "Bangalore", "Jaipur"])

temps[["Chennai","Mumbai","Bangalore"]]

temps[temps>30]

# ## Question 5 
# ### Create two Series `s1` and `s2` with partial overlapping indices and numeric values.
# #### Add them and print the result.
# #### Explain what happens to non-common indices (in comments).


s1 = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
s2 = pd.Series([5, 15, 25], index=["b", "c", "e"])

s1+s2

# ## Question 6
# ### Create a Series with some `np.nan` values.
# #### Show how to check missing values.
# #### Drop missing values and print the result.
# 


s = pd.Series([10, np.nan, 25, np.nan, 40])

s.isna()

s.dropna()

# ## Question 7
# ### Create a Series from a dictionary of product:price.
# #### Increase all prices by 5%.
# #### Print the updated Series.


prices = pd.Series({"Laptop": 50000,"Mobile": 20000,"Tablet": 15000,"Headphones": 3000})

prices*1.05

# ## Question 8
# ### Create a Series of 8 random integers between 10 and 100 (fixed seed).
# #### Print values greater than 50.
# #### Print `max`, `min`, and `mean`


np.random.seed(42)
s = pd.Series(np.random.randint(10, 101, size=8))
s

s[s>50]

s.max()

s.min()

s.mean()

# ## Question 9
# ### Use `apply` on a Series of `[1, 2, 3, 4]` to:
# #### Cube each value.
# #### Convert each value to a string with prefix `'num_'`.


s=pd.Series([1,2,3,4])

s.apply(lambda x:x**3)

s.apply(lambda x:f"num_{x}")

# ## Question 10
# ### Create a Series with duplicate values.
# #### Use `value_counts` to show frequency of each unique value.


s = pd.Series([10, 20, 10, 30, 20, 10, 40, 30])

s.value_counts()