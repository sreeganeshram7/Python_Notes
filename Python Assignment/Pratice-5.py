# Generated from: Pratice-5.ipynb
# Converted at: 2026-01-10T09:14:02.351Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Day 5 – pandas DataFrame Creation & Basic Operations: 10 Questions
# ## Question 1
# ### Create a DataFrame for 5 students with columns: `name`, `age`, `maths`.
# #### Print the DataFrame.
# #### Print `info()` and `describe()`.


import pandas as pd
import numpy as np

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [20, 21, 19, 22, 20],
    "maths": [85, 78, 92, 88, 76]
}

df=pd.DataFrame(data)
df

df.info()

df.describe()

# ## Question 2
# ### Create a DataFrame from:
# ### ```data = {'city': ['A', 'B', 'C', 'D'],'temp': [30, 22, 25, 28],'humidity': [65, 70, 68, 72]}```
# #### Print first 3 rows.
# #### Print only `city` and `temp`.


data = {
    'city': ['A', 'B', 'C', 'D'],
    'temp': [30, 22, 25, 28],
    'humidity': [65, 70, 68, 72]
}

df=pd.DataFrame(data)
df

df.head(3)

df.city

df.temp

# ## Question 3
# ### Add a new column `temp_f` to convert `temp` from Celsius to Fahrenheit.
# #### Print the DataFrame.


df['temp_f']=df['temp']*9/5+32

df

# ## Question 4
# ### For a DataFrame with numeric columns `A`, `B`, `C`, add:
# #### `A_plus_B = A + B`
# #### `C_squared = C ** 2`.


df = pd.DataFrame({
    'A': [2, 4, 6, 8],
    'B': [1, 3, 5, 7],
    'C': [3, 5, 7, 9]
})

df['A_plus_B']=df['A']+df['B']

df['C_squared']=df['C']**2

df

# ## Question 5
# ### Create a DataFrame with at least 6 rows and 3 numeric columns.
# #### Select rows where one column is greater than 50.
# #### Select rows where another column is in `[10, 20, 30]`.


df = pd.DataFrame({
    'A': [45, 60, 75, 30, 90, 55],
    'B': [10, 20, 40, 30, 50, 20],
    'C': [5, 15, 25, 35, 45, 55]
})

df[df['A']>50]

df.isin([10,20,30])

df[df['B'].isin([10,20,30])]

# ## Question 6
# ### Demonstrate row and column selection:
# #### Select a single row by `.loc`.
# #### Select a single row by `.iloc`.
# #### Select a subset of rows and columns using `.loc`.


df.loc[0]

df.iloc[-1]

df.loc[1:3,'A':'C']

df.loc[1:3,'C']

# ## Question 7
# ### Create a DataFrame with a `student_id` column.
# #### Set `student_id` as index.
# #### Reset the index back.


df = pd.DataFrame({
    'student_id': [101, 102, 103],
    'name': ['Alice', 'Bob', 'Charlie'],
    'marks': [85, 90, 78]
})

df.set_index('student_id')

df.reset_index()

# ## Question 8
# ### Given a DataFrame with `marks` column, compute and print:
# #### Mean marks
# #### Row with maximum marks.
# 


df=pd.DataFrame({'marks': [85, 90, 78, 50, 67]})

df.mean()

df.loc[df['marks'].idxmax()]

# ## Question 9
# ### Create a DataFrame and demonstrate:
# #### Renaming a column.
# #### Dropping a column.
# #### Dropping a row by index.


df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
df

df.rename(columns={'A':'G'})

df.drop(columns='C')

df.drop(index=2)

# ## Question 10
# ### Create a DataFrame with a column of strings.
# #### Convert the column to uppercase.
# #### Create a new column with the length of each string.


df = pd.DataFrame({'text': ['hello', 'world', 'pandas','oops']})

df

df['upper']=df['text'].str.upper()
df

df['length']=df['text'].str.len()
df