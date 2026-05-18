# Generated from: Pratice-10.ipynb
# Converted at: 2026-01-10T09:12:47.134Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Day 10 – Mixed Practice (NumPy + Pandas): 10 Questions
# 
# ## Question 1
# ### Using NumPy, create a 5×5 array with values 1–25.
# #### Convert to DataFrame with columns `C1`–`C5`.
# #### Print first and last 2 rows.


import numpy as np
import pandas as pd

arr=np.arange(1,26).reshape(5,5)
arr

df=pd.DataFrame(arr,columns=['C1','C2','C3','C4','C5'])
df

df.head(2)

df.tail(2)

# ## Question 2
# ### Use NumPy random to create 1D array of 10 integers between 0 and 100.
# #### Convert to Series.
# #### Print values greater than the Series mean.


arr=np.random.randint(0,101,size=10)
arr

series=pd.Series(arr)
series

series.mean()

series[series>series.mean()]

# ## Question 3
# ### Create Celsius temperatures `[25, 30, 28, 22, 26]` as NumPy array.
# #### Convert to Fahrenheit using vectorized operations.
# #### Put in DataFrame with `celsius`, `fahrenheit`.


c=np.array([25,30,28,22,26])
c

f=c*9/5+32

df=pd.DataFrame({'celsius':c,'fahrenheit':f})
df

# ## Question 4
# ### Create DataFrame `id`, `maths`, `science`, `english`.
# #### Use NumPy to compute row-wise total and average marks.
# #### Add them as new columns.


df = pd.DataFrame({
    'id': [1, 2, 3],
    'maths': [80, 70, 90],
    'science': [75, 85, 95],
    'english': [78, 88, 92]
})

df['total']=df[['maths','science','english']].sum(axis=1)
df

df['avg']=df['total'].mean()

df

# ## Question 5
# ### Create 3×3 NumPy array of random integers.
# #### Convert to DataFrame with custom row and column labels.
# #### Print DataFrame.


np.random.seed(1)
arr=np.random.randint(1,10,size=(3,3))
arr

df=pd.DataFrame(arr,columns=['c1','c2','c3'],index=['r1','r2','r3'])
df

# ## Question 6
# ### Create DataFrame with `score`.
# #### Use `np.where` to create `grade`: `"A"` (score≥80), `"B"` (50–79), `"C"` (<50).


df=pd.DataFrame({'score': [45, 82, 60, 30]})
df

df['grade']=np.where(df['score']>=80,'A',np.where(df['score']>=50,'B','C'))

df

# ## Question 7
# ### Create 1D NumPy array of 12 values, reshape to 3×4, convert to DataFrame.
# #### Add column with row sum.
# #### Filter rows where sum > 15.


arr=np.arange(0,12).reshape(3,4)

df=pd.DataFrame(arr)
df

df['row_sum']=df.sum(axis=1)
df

filter=df[df['row_sum']>15]
filter

# ## Question 8
# ### Create DataFrame with `age`.
# #### Use `pd.cut` to create age groups.
# #### Use `value_counts` to show counts per group.


df = pd.DataFrame({'age': [15, 22, 35, 42, 67]})
df['age_group'] = pd.cut(
    df['age'],
    bins=[0, 18, 35, 60, 100],
    labels=['0-18', '19-35', '36-60', '60+']
)

df['age_group'].value_counts()

# ## Question 9
# ### Create NumPy array of floats.
# #### Convert to Series.
# #### Round to 2 decimals and store in another Series


arr = np.array([1.2345, 2.3456, 3.9876])

series=pd.Series(arr)

r_series=series.round(2)
r_series

# ## Question 10
# ### Create small DataFrame and NumPy boolean mask for a condition on one column.
# #### Use mask to filter DataFrame.


df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [10, 20, 30, 40]})

mask=np.array(df['y']>=20)
mask

filter=df[mask]
filter