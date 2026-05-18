# Day 6 – Filtering, Sorting, Missing Data: 10 Questions

## Question 1
Create a DataFrame of 6 employees: `emp_id`, `name`, `age`, `salary`, `dept`.
- Filter employees with salary > 40000.
- Filter employees from a given department with age < 30.

---

## Question 2
Demonstrate sorting:
- Sort by `salary` ascending.
- Sort by `dept` ascending and `salary` descending.

---

## Question 3
Create a DataFrame with missing values in both numeric and string columns.
- Detect missing values.
- Count missing values per column.

---

## Question 4
Handle missing values:
- Drop rows with any missing value.
- Fill missing numeric values with column mean and string values with `"Unknown"`.

---

## Question 5
Create a DataFrame with column `score`.
- Replace scores < 35 with 35.
- Replace scores > 90 with 90.

---

## Question 6
Use `.query()` to filter rows where `salary > 45000` and `dept == "IT"`.
- Achieve the same using boolean indexing.

---

## Question 7
Use `.isin()` to filter rows where `dept` is in `['IT', 'HR']`.

---

## Question 8
Create a DataFrame with duplicate `emp_id`.
- Use `.drop_duplicates` on `emp_id` with `keep='first'` and `keep='last'`.

---

## Question 9
Create a DataFrame with a categorical-like column (`"Low"`, `"Medium"`, `"High"`).
- Convert it to `category` dtype and display categories.

---

## Question 10
Create a DataFrame with 2 numeric columns.
- Use `.clip` to keep values between 10 and 50.

---

**Total Questions: 10**  
**Time Limit: 35–50 minutes**  
**Difficulty: Intermediate to Advanced**
