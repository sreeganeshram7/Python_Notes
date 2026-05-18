# Day 7 – GroupBy & Aggregation: 10 Questions

## Question 1
Create a sales DataFrame with columns: `region`, `product`, `units`, `price`.
- Add `revenue = units * price`.
- Group by `region` to find total revenue per region.

---

## Question 2
Group the same DataFrame by `product` and compute:
- Total units sold.
- Average price.

---

## Question 3
Create a student DataFrame: `class`, `student`, `marks`.
- Group by `class` and find mean and max marks.

---

## Question 4
Use `.agg()` to calculate `min`, `max`, `mean`, `count` for `marks` per `class`.

---

## Question 5
Create a DataFrame with `category`, `sub_category`, `value`.
- Group by both columns and calculate sum of `value`.
- Reset index.

---

## Question 6
Create `customer_id`, `order_id`, `amount` DataFrame.
- Group by `customer_id` to get total and average `amount`.
- Sort by total amount descending.

---

## Question 7
Use `value_counts()` on a categorical column and convert result to DataFrame with columns `value`, `count`.

---

## Question 8
Create a DataFrame with a `date` column and `sales`.
- Convert `date` to datetime.
- Group by month and sum sales.

---

## Question 9
Create `team`, `player`, `score` DataFrame.
- Find player with highest score in each team (using `idxmax`).

---

## Question 10
Use `groupby` and `filter` to keep only groups where mean `marks` > 70.

---

**Total Questions: 10**  
**Time Limit: 40–55 minutes**  
**Difficulty: Intermediate to Advanced**
