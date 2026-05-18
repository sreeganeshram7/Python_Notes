# Day 8 – Merge, Join, Concat: 10 Questions

## Question 1
Create `df_customers` (`customer_id`, `name`) and `df_orders` (`order_id`, `customer_id`).
- Perform inner merge on `customer_id`.

---

## Question 2
Perform left and right merge on `customer_id` for these DataFrames.
- Compare row counts.

---

## Question 3
Create `df1(id, value1)` and `df2(id, value2)` with partially overlapping `id`.
- Perform outer merge and print result.

---

## Question 4
Create two monthly DataFrames with same columns.
- Concatenate vertically and reset index.

---

## Question 5
Create two DataFrames with same index but different columns.
- Concatenate horizontally (`axis=1`).

---

## Question 6
Show how to add a new row to a DataFrame by concatenating with a single-row DataFrame.

---

## Question 7
Create two DataFrames where one has extra keys.
- Left merge with `indicator=True`.
- Filter rows available only in left.

---

## Question 8
Demonstrate merge on multiple keys, e.g. `['city', 'year']`.

---

## Question 9
Create a product DataFrame and discount DataFrame.
- Merge and compute final price after discount.

---

## Question 10
Use `pd.concat` with `keys` to create a hierarchical index for two DataFrames.

---

**Total Questions: 10**  
**Time Limit: 40–55 minutes**  
**Difficulty: Intermediate to Advanced**
