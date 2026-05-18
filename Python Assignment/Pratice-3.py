# Generated from: Pratice-3.ipynb
# Converted at: 2026-01-10T09:14:29.110Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Day 3 – NumPy Reshape, Aggregation, Broadcasting: 10 Questions
# ## Question 1
# ### Create a 1D array of numbers from 1 to 15.
# #### Reshape it to 3×5.
# #### Print the reshaped array and its shape.
# 


import numpy as np

arr=np.arange(1,16).reshape(3,5)
arr

arr.shape

# ## Question 2
# ### Create a 3×3 array with values from 2 to 10 (inclusive).
# #### Compute and print the overall sum, mean, max, and min.


arr=np.arange(2,11).reshape(3,3)
arr

arr.mean()

arr.sum()

arr.max()

arr.min()

# ## Question 3
# ### Create a 4×4 array with values from 0 to 15.
# #### Compute the sum along rows.
# #### Compute the sum along columns.


arr=np.arange(0,16).reshape(4,4)
arr

arr.sum(axis=1)

arr.sum(axis=0)

# ## Question 4
# ### Create a 2×3 array `A = [[1, 2, 3], [4, 5, 6]]` and a 1D array `b = [10, 20, 30]`.
# #### Use broadcasting to add `b` to each row of `A`.
# #### Print the result.


A=np.array([[1,2,3],[4,5,6]])
b=np.array([10,20,30])

A+b

# ## Question 5
# ### Create a column vector `c = [[1], [2], [3]]` and row vector `[10, 20, 30, 40]`.
# #### Use broadcasting to create a 3×4 matrix `M = c + row_vector`.
# #### Print `M`.


c=np.array([[1],[2],[3]])
d=np.array([10,20,30,40])

M=c+d
M

# ## Question 6
# ### Create a 2×6 array and reshape it into a 3D array of shape `(2, 2, 3)`.
# #### Print the original and reshaped arrays.


arr=np.arange(12).reshape(2,6)
arr

arr.reshape(2,2,3)

# ## Question 7
# ### Create a 2×5 array with values from 0 to 9.
# #### Flatten it back to 1D using `ravel` and `flatten`.
# #### Print both and note the difference (view vs copy conceptually).


arr=np.arange(0,10).reshape(2,5)
arr

r=arr.ravel()
r

f=arr.flatten()
f

# ## Question 8
# ### Create an array of shape `(5, 3)` with random integers.
# ####  Compute mean of each column.
# ####  Compute mean of each row.


np.random.seed(1)
arr1=np.random.randint(1,20,size=(5,3))
arr1

np.random.seed(2)
arr2=np.random.randint(1,20,size=(5,3))
arr2

arr1.mean(axis=0)

arr1.mean(axis=1)

arr2.mean(axis=0)

arr2.mean(axis=1)

# ## Question 9
# ### Create a 1D array with elements `[1, 2, 2, 3, 3, 3, 4, 4]`.
# #### Find unique values and their counts.


arr=np.array([1,2,2,3,3,3,4,4])
arr

vals,counts=np.unique(arr,return_counts=True)
vals,counts

# ## Question 10
# ### Create a 1D array of 5 elements and a scalar value 10.
# ### Use broadcasting to add the scalar to the array.
# #### Multiply the array by 2.
# #### Print the results.


arr=np.array([1,2,3,4,5])
arr

scalar=10
arr+scalar

arr*2