# Generated from: Pratice-9.ipynb
# Converted at: 2026-01-10T09:13:05.048Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Day 9 – NumPy-Pandas Interoperability: 10 Questions
# ## Question 1
# ### Create a DataFrame of shape `(4, 3)` with integers 0–11.
# #### Convert to NumPy array with `.to_numpy()`.
# #### Print `dtype` and `shape`.


import numpy as np
import pandas as pd

df=pd.DataFrame(np.arange(0,12).reshape(4,3))
df

arr=df.to_numpy()
arr

arr.dtype

arr.shape

# ## Question 2
# ### Create a 2D NumPy array of shape `(3, 4)` and convert to DataFrame with column names `['c1', 'c2', 'c3', 'c4']`.
# #### Print the DataFrame.


arr=np.arange(12).reshape(3,4)
arr

df=pd.DataFrame(arr,columns=['c1','c2','c3','c4'])
df

# ## Question 3
# ### For a numeric DataFrame column, compute mean and std using NumPy (`np.mean`, `np.std`) and pandas (`.mean()`, `.std()`).
# #### Print both results.


df=pd.DataFrame({'marks':[20,40,60,80]})
df

#numpy
mean=np.mean(df['marks'])
mean

std=np.std(df['marks'])
std

#pandas
mean=df['marks'].mean()
mean

std=df['marks'].std()
std

# ## Question 4
# ### Extract underlying array from DataFrame using `.to_numpy()`.
# #### Use `np.sum(axis=0)` and compare with `df.sum()`.


df = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [40, 50, 60]
})

arr=df.to_numpy()
arr

sum=np.sum(arr,axis=0)
sum

sum=df.sum(axis=0)
sum

# ## Question 5
# ### Create a DataFrame from a NumPy array.
# #### Add column that is square of one column using NumPy.
# #### Add boolean column that checks if another column > threshold.


arr = np.array([[2, 5],[4, 8],[6, 3]])

df = pd.DataFrame(arr, columns=['A', 'B'])

df['A_square']=np.square(df['A'])

threshold=5
df['threshold']=np.array(df['B'])>threshold

df

# ## Question 6
# ### Demonstrate whether modifying array from `.to_numpy()` changes DataFrame (conceptual demonstration).


df = pd.DataFrame({'A': [1, 2, 3]})
arr = df.to_numpy()
arr[0, 0] = 100
arr

# ## Question 7
# ### Create a Series from random NumPy array.
# ### Use `np.where` to create 1s where values > 0, else 0.
# ### Convert result to Series.


arr=np.random.randn(5)

result=np.where(arr>0,1,0)

series=pd.Series(result)
series

# ## Question 8
# ### Take a DataFrame, get `.to_numpy()`, slice a submatrix.
# #### Convert submatrix back to DataFrame.


df = pd.DataFrame({
    'A': [10, 20, 30, 40],
    'B': [50, 60, 70, 80],
    'C': [90, 100, 110, 120]
})

arr=df.to_numpy()
arr

sub_arr=arr[1:3,0:2]
sub_arr

sub_df=pd.DataFrame(sub_arr,columns=['A','B'])
sub_df

# ## Question 9
# ### Use `np.where` on DataFrame marks column to create a `result` column (`"Pass"` if ≥40 else `"Fail"`).


df = pd.DataFrame({'marks': [35, 45, 60, 30, 80]})

df['result']=np.where(df['marks']>=40,'Pass','Fail')

df

# ## Question 10
# ## Use NumPy to standardize a numeric column (z-score) and store in new column.


df['z-score']=(df['marks']-np.mean(df['marks']))/np.std(df['marks'])

df