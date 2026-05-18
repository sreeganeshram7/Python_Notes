# NumPy and Pandas Intermediate Test
**Duration: 1 Hour 15 Minutes (75 minutes)**

---

## SECTION A: MULTIPLE CHOICE QUESTIONS (5 Questions)
**Time Suggested: 20 minutes | Total Marks: 25**

---

### MCQ 1: NumPy Array Operations
What will be the output of the following code?

```python
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
result = np.dot(a, b.T)
print(result.shape)
```

**Options:**
- A) (2, 2)
- B) (3, 3)
- C) (2, 3)
- D) (3, 2)

---

### MCQ 2: Pandas DataFrame Filtering
Given the following code, what will be printed?

```python
import pandas as pd
df = pd.DataFrame({
    'A': [10, 20, 30, 40],
    'B': [100, 200, 150, 120]
})
result = df[(df['A'] > 15) & (df['B'] < 200)]
print(len(result))
```

**Options:**
- A) 1
- B) 2
- C) 3
- D) 0

---

### MCQ 3: NumPy Broadcasting
Which of the following correctly describes NumPy broadcasting?

```python
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])  # Shape: (2, 3)
b = np.array([10, 20, 30])             # Shape: (3,)
result = a + b
```

**Options:**
- A) This will raise a ValueError because shapes are incompatible
- B) Broadcasting will expand b to shape (2, 3) and add it to a, resulting in [[11, 22, 33], [14, 25, 36]]
- C) The operation will only add b to the first row of a
- D) Broadcasting will expand a to match b's shape

---

### MCQ 4: Pandas GroupBy and Aggregation
What will be the output of this code?

```python
import pandas as pd
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Value': [10, 20, 30, 15, 25]
})
result = df.groupby('Category')['Value'].agg(['sum', 'mean'])
print(result.loc['A', 'mean'])
```

**Options:**
- A) 21.67 (approximately)
- B) 65
- C) 30
- D) 20

---

### MCQ 5: NumPy Array Manipulation
What will be the output?

```python
import numpy as np
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
indices = np.argsort(arr)
sorted_arr = arr[indices]
print(sorted_arr[-2])
```

**Options:**
- A) 1
- B) 5
- C) 6
- D) 8

---

---

## SECTION B: CODING QUESTIONS (5 Questions)
**Time Suggested: 55 minutes | Total Marks: 75**

---

### Coding Question 1: Array Reshaping and Axis Operations
**Marks: 15**

Write a Python program using NumPy to:
1. Create a 1D array with values from 1 to 12
2. Reshape it into a 3x4 matrix
3. Calculate the sum along axis 0 (column-wise)
4. Calculate the mean along axis 1 (row-wise)
5. Find the standard deviation of the entire array
6. Print all results with appropriate labels

**Expected Output Format:**
```
Array shape: (3, 4)
Sum along columns: [... ... ... ...]
Mean along rows: [... ... ...]
Standard Deviation: ...
```

---

### Coding Question 2: NumPy Advanced Indexing and Masking

Write a NumPy program to:
1. Create a 2D array of shape (5, 4) with random integers between 1 and 100
2. Create a boolean mask to identify elements greater than 50
3. Replace all elements greater than 50 with their squared values
4. Replace all elements less than or equal to 50 with 0
5. Calculate what percentage of elements were greater than 50 in the original array
6. Print the modified array and the percentage

---

### Coding Question 3: Pandas DataFrame Merging and Joining
**Marks: 15**

Create two DataFrames and perform the following operations:

**DataFrame 1 (Sales):**
- Columns: `emp_id`, `emp_name`, `sales_amount`
- Data: 5 employees with their sales data

**DataFrame 2 (Bonus):**
- Columns: `emp_id`, `bonus_rate`
- Data: 5 employees with their bonus rates

Write code to:
1. Merge the two DataFrames on `emp_id`
2. Create a new column `bonus_amount` = `sales_amount * bonus_rate`
3. Sort the result by `bonus_amount` in descending order
4. Display employees with bonus_amount > 500
5. Calculate the total bonus for all employees

---

### Coding Question 4: Pandas DataFrame Filtering and Aggregation 
**Marks: 15**

Create a pandas DataFrame programmatically with the following structure:
- Columns: `product_id`, `product_name`, `category`, `price`, `quantity_sold`
- Data: 10 products across 3 categories (Electronics, Clothing, Food)

Write code to:
1. Create the DataFrame with sample data
2. Filter products where `price > 500` and `quantity_sold > 20`
3. Group by `category` and calculate:
   - Total revenue per category (price × quantity_sold)
   - Average price per category
   - Total quantity sold per category
4. Create a new column `total_revenue` = `price * quantity_sold`
5. Find the top 3 products by total revenue
6. Calculate the percentage contribution of each category to overall revenue

---

### Coding Question 5: NumPy Operations with Pandas Integration 

Write a program that:
1. Creates a NumPy array of shape (10, 5) with random values between 0 and 100
2. Converts this array to a pandas DataFrame with columns named `A`, `B`, `C`, `D`, `E`
3. Perform the following operations:
   - Calculate the correlation matrix between all columns
   - Identify which two columns have the highest correlation
   - Create a new column `Average` = mean of all numeric columns
   - Normalize all columns (subtract mean, divide by std dev)
   - Find rows where the `Average` is in the top 20% (highest 2 rows out of 10)
4. Print:
   - The correlation matrix
   - The two columns with highest correlation and their correlation value
   - The normalized DataFrame
   - The top 20% rows with their average values

---

---

## Instructions for Students:

1. **Section A (MCQs):** Choose the most appropriate answer for each multiple-choice question. You may use a calculator if needed.

2. **Section B (Coding Questions):** Write complete, well-documented Python code. Your code should:
   - Include clear comments explaining each step
   - Handle any potential errors gracefully
   - Follow PEP 8 naming conventions
   - Display output clearly with appropriate labels

3. **Time Management:** 
   - MCQs: ~20 minutes
   - Coding: ~55 minutes
4. **Allowed Resources:** Python IDE/Jupyter Notebook, Python documentation

5. **Submission:** Provide all code files and output screenshots/results

---
