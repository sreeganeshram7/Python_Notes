# Generated from: Pratice-6.ipynb
# Converted at: 2026-01-10T09:13:50.839Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Day 6 – Filtering, Sorting, Missing Data: 10 Questions
# 
# ## Question 1
# ### Create a DataFrame of 6 employees: `emp_id`, `name`, `age`, `salary`, `dept`.
# #### Filter employees with salary > 40000.
# #### Filter employees from a given department with age < 30.


import pandas as pd
import numpy as np

df = pd.DataFrame({
    'emp_id': [1, 2, 3, 4, 5, 6],
    'name': ['A', 'B', 'C', 'D', 'E', 'F'],
    'age': [25, 32, 28, 29, 24, 35],
    'salary': [30000, 50000, 40000, 45000, 28000, 60000],
    'dept': ['HR', 'IT', 'IT', 'Sales', 'HR', 'IT']
})
df

df[df['salary']>40000]

print(df[(df['dept']=='IT') & (df['age']<30)])

# ## Question 2
# ### Demonstrate sorting:
# #### Sort by `salary` ascending.
# #### Sort by `dept` ascending and `salary` descending.


df=df.sort_values(by='salary',ascending=True)
df

df=df.sort_values(by=['dept','salary'],ascending=[True,False])
df

# ## Question 3
# ### Create a DataFrame with missing values in both numeric and string columns.
# #### Detect missing values.
# #### Count missing values per column.


df2 = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': ['x', None, 'z']
})

df2.isna()

df2.isna().sum()

# ## Question 4
# ### Handle missing values:
# #### Drop rows with any missing value.
# #### Fill missing numeric values with column mean and string values with `"Unknown"`.


data=df2.dropna(axis=1)
data

filter=df2['A'].fillna(df2['A'].mean())
filter

filtered=df2['B'].fillna('Unknown')
filtered

# ## Question 5
# ### Create a DataFrame with column `score`.
# #### Replace scores < 35 with 35.
# #### Replace scores > 90 with 90.


df = pd.DataFrame({'score': [20, 40, 95, 88]})
df['score'] = df['score'].clip(lower=35, upper=90)
print(df)

# ## Question 6
# ### Use `.query()` to filter rows where `salary > 45000` and `dept == "IT"`.
# #### Achieve the same using boolean indexing.


print(df.query('salary>45000 and dept=="IT"'))

print(df[(df['salary']>45000) & (df['dept']=='IT')])

# ## Question 7
# ### Use `.isin()` to filter rows where `dept` is in `['IT', 'HR']`.


print(df['dept'].isin(['IT','HR']))

# ## Question 8
# ### Create a DataFrame with duplicate `emp_id`.
# #### Use `.drop_duplicates` on `emp_id` with `keep='first'` and `keep='last'`.
# 


df3 = pd.DataFrame({'emp_id': [1, 2, 3, 4, 5, 6, 5, 4, 6],'name': ['A', 'B', 'C', 'D', 'E', 'F','G','H','I']})

df3.drop_duplicates(subset='emp_id',keep='first')

df3.drop_duplicates(subset='emp_id',keep='last')

# ## Question 9
# ### Create a DataFrame with a categorical-like column (`"Low"`, `"Medium"`, `"High"`).
# #### Convert it to `category` dtype and display categories.


df=pd.DataFrame({'level':['Low','Medium','High','Low','High']})
df

df['level']=df['level'].astype('category')
df

df['level'].cat.categories

# ## Question 10
# ### Create a DataFrame with 2 numeric columns.
# #### Use `.clip` to keep values between 10 and 50.


df = pd.DataFrame({'x': [5, 20, 60], 'y': [0, 30, 100]})
df.clip(lower=10,upper=50)