# Generated from: Pratice-2.ipynb
# Converted at: 2026-01-10T09:14:42.718Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Day 2 – NumPy Indexing & Slicing: 10 Questions
# 
# ## Question 1
# ### Create a 1D NumPy array with values 0 to 19.
# #### Print elements from index 4 to 10 (inclusive).
# #### Print every third element from the array.
# 


import numpy as np

arr=np.arange(0,20)
arr

arr[4:11]

arr[::3]

# ## Question 2
# ### Create a 3×4 array with values from 0 to 11.
# #### Print the second row.
# #### Print the last column.
# #### Print the element at row index 2, column index 1.


arr=np.arange(0,12).reshape(3,4)
arr

arr[1,:]

arr[:,3]

arr[2,1]

# ## Question 3
# ### Create a 1D array from 1 to 12.
# #### Extract elements at indices `[0, 3, 5, 7, 11]` using fancy indexing.
# #### Print the result.


arr=np.arange(1,13)
arr

idx=[0,3,5,7,11]
print(arr[idx])

# ## Question 4
# ### Create a 4×4 array with values from 1 to 16.
# #### Print the 2×2 subarray from the middle.
# #### Print the diagonal elements.


arr=np.arange(1,17).reshape(4,4)
arr

arr[1:3,1:3]

np.diag(arr)

# ## Question 5
# ### Create a 1D array with values from 10 to 19.
# #### Reverse the array using slicing.
# #### Reverse the array using `np.flip`.


arr=np.arange(10,20)
arr

arr[::-1]

np.flip(arr)

# ## Question 6
# ### Create a 5×5 array with values from 0 to 24.
# #### Print all elements in the first two rows.
# #### Print all elements in the last two columns.


arr=np.arange(0,25).reshape(5,5)
arr

arr[:2,:]

arr[:,-2:]

# ## Question 7
# ### Create a 3×3 array with values from 1 to 9.
# #### Replace all elements greater than 5 with 0.
# #### Print the modified array.


arr=np.arange(1,10).reshape(3,3)
arr

arr[arr>5]=0

arr

# ## Question 8
# ### Create a 1D array of size 10 with random integers between 1 and 50.
# #### Use boolean indexing to print all elements greater than 30.
# #### Use boolean indexing to print all elements that are even.


np.random.seed(1)
arr=np.random.randint(1,51,size=10)
arr

arr[arr>30]

arr[arr%2==0]

# ## Question 9
# ### Create a 4×3 array with values from 1 to 12.
# #### Print the first column as a 1D array.
# #### Print the last row.


arr=np.arange(1,13).reshape(4,3)
arr

arr[:,0]

arr[-1,:]

# ## Question 10
# ### Create a 1D array from 0 to 9.
# #### Set elements at indices `[1, 3, 5, 7, 9]` to -1 using fancy indexing.
# #### Print the final array.


arr=np.arange(0,10)
arr

idx=[1,3,5,7,9]
arr[idx]=-1
arr