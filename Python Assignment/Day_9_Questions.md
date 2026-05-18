# Day 9 – NumPy-Pandas Interoperability: 10 Questions

## Question 1
Create a DataFrame of shape `(4, 3)` with integers 0–11.
- Convert to NumPy array with `.to_numpy()`.
- Print `dtype` and `shape`.

---

## Question 2
Create a 2D NumPy array of shape `(3, 4)` and convert to DataFrame with column names `['c1', 'c2', 'c3', 'c4']`.
- Print the DataFrame.

---

## Question 3
For a numeric DataFrame column, compute mean and std using NumPy (`np.mean`, `np.std`) and pandas (`.mean()`, `.std()`).
- Print both results.

---

## Question 4
Extract underlying array from DataFrame using `.to_numpy()`.
- Use `np.sum(axis=0)` and compare with `df.sum()`.

---

## Question 5
Create a DataFrame from a NumPy array.
- Add column that is square of one column using NumPy.
- Add boolean column that checks if another column > threshold.

---

## Question 6
Demonstrate whether modifying array from `.to_numpy()` changes DataFrame (conceptual demonstration).

---

## Question 7
Create a Series from random NumPy array.
- Use `np.where` to create 1s where values > 0, else 0.
- Convert result to Series.

---

## Question 8
Take a DataFrame, get `.to_numpy()`, slice a submatrix.
- Convert submatrix back to DataFrame.

---

## Question 9
Use `np.where` on DataFrame marks column to create a `result` column (`"Pass"` if ≥40 else `"Fail"`).

---

## Question 10
Use NumPy to standardize a numeric column (z-score) and store in new column.

---

**Total Questions: 10**  
**Time Limit: 35–50 minutes**  
**Difficulty: Advanced**
