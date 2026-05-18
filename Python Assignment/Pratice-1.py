# Generated from: Pratice-1.ipynb
# Converted at: 2026-01-10T09:14:55.415Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# ## Day 1 – NumPy Basics: 10 Questions
# ## Question 1


# ### Write a NumPy program to:
# #### Create a 1D array of integers from 5 to 14 (inclusive).
# #### Print the array, its `dtype`, `ndim`, and `shape`.


import numpy as np

arr=np.arange(5,15)
arr

arr.dtype

arr.ndim

arr.shape

print(arr,arr.dtype,arr.ndim,arr.shape)

# ## Question 2
# ### Convert the list `[2, 4, 6, 8, 10]` to a NumPy array and:
# #### Multiply all elements by 3.
# #### Subtract 2 from each element.`
# #### Print the final array


lst=[2,4,6,8,10]
arr=np.array(lst)
arr

arr=arr*3
arr

arr=arr-2
arr

# ## Question 3
# ### Create a 2D NumPy array of shape `(3, 3)` containing numbers from 1 to 9.
# #### Print the array.
# #### Print its `size` and `shape`.


arr=np.arange(1,10).reshape(3,3)
arr

print(arr.size,arr.shape)

# ## Question 4
# ### Create a 1D array of 10 zeros and then:
# #### Set the 1st, 5th, and 10th elements to 7.
# #### Print the array.
# 


arr=np.zeros(10,dtype=int)
arr

arr[0]=arr[4]=arr[6]=7

arr

# ## Question 5
# ### Use `np.arange` to create an array of odd numbers from 1 to 19.
# #### Print the array and its sum.
# 


arr=np.arange(1,20,2)
arr

arr.sum()

# ## Question 6
# ### Create a 4×4 identity matrix using NumPy and print it.


arr=np.eye(4)
arr

# ## Question 7
# ### Using NumPy random module, generate a 1D array of 6 random integers between 0 and 20.
# #### Use a fixed seed of 10.
# #### Print the array, the maximum value, and the index of the maximum.


np.random.seed(10)

arr=np.random.randint(0,21,size=6)
arr

arr.max()

arr.argmax()

# ## Question 8
# ### Given `a = np.array([1, 3, 5, 7])` and `b = np.array([2, 4, 6, 8])`, compute and print: `a + b``a * b``b - a``b / a`


a=np.array([1,3,5,7])
b=np.array([2,4,6,8])

a+b

b-a

a*b

b/a

# ## Question 9
# ### Create a 2D array of shape `(2, 5)` with values from 10 to 19.
# #### Print the first row.
# #### Print the second column of this array.


arr=np.arange(10,20).reshape(2,5)
arr

arr[0,:]

arr[:,1]

# ## Question 10
# ### Use `np.linspace` to create 15 values between 0 and 5 (inclusive).
# #### Print the array, its first 3 elements, and last 3 elements.


arr=np.linspace(0,5,15)
arr

arr[:3]

arr[-3:]