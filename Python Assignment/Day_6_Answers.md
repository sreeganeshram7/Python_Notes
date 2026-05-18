# Day 6 – Filtering, Sorting, Missing Data: Answer Key

## Answer 1
```python
df = pd.DataFrame({
    'emp_id': [1, 2, 3, 4, 5, 6],
    'name': ['A', 'B', 'C', 'D', 'E', 'F'],
    'age': [25, 32, 28, 29, 24, 35],
    'salary': [30000, 50000, 40000, 45000, 28000, 60000],
    'dept': ['HR', 'IT', 'IT', 'Sales', 'HR', 'IT']
})
print(df[df['salary'] > 40000])
print(df[(df['dept'] == 'IT') & (df['age'] < 30)])
```

---

## Answer 2
```python
print(df.sort_values('salary'))
print(df.sort_values(['dept', 'salary'], ascending=[True, False]))
```

---

## Answer 3
```python
df2 = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': ['x', None, 'z']
})
print(df2.isna())
print(df2.isna().sum())
```

---

## Answer 4
```python
print(df2.dropna())
df_filled = df2.copy()
df_filled['A'] = df2['A'].fillna(df2['A'].mean())
df_filled['B'] = df2['B'].fillna('Unknown')
print(df_filled)
```

---

## Answer 5
```python
df = pd.DataFrame({'score': [20, 40, 95, 88]})
df['score'] = df['score'].clip(lower=35, upper=90)
print(df)
```

**Output:**
```
   score
0     35
1     40
2     90
3     88
```

---

## Answer 6
```python
print(df.query('salary > 45000 and dept == "IT"'))
print(df[(df['salary'] > 45000) & (df['dept'] == 'IT')])
```

---

## Answer 7
```python
print(df[df['dept'].isin(['IT', 'HR'])])
```

---

## Answer 8
```python
df_dup = pd.DataFrame({'emp_id': [1, 1, 2, 2], 'name': ['A', 'A2', 'B', 'B2']})
print(df_dup.drop_duplicates(subset=['emp_id'], keep='first'))
print(df_dup.drop_duplicates(subset=['emp_id'], keep='last'))
```

**Output:**
```
   emp_id name
0       1    A
2       2    B

   emp_id name
1       1   A2
3       2   B2
```

---

## Answer 9
```python
df = pd.DataFrame({'level': ['Low', 'High', 'Medium', 'Low']})
df['level'] = df['level'].astype('category')
print(df['level'].cat.categories)
```

**Output:**
```
Index(['High', 'Low', 'Medium'], dtype='object')
```

---

## Answer 10
```python
df = pd.DataFrame({'x': [5, 20, 60], 'y': [0, 30, 100]})
print(df.clip(lower=10, upper=50))
```

**Output:**
```
    x   y
0  10  10
1  20  30
2  50  50
```

---

**Answer Key Complete**  
**Day 6 Difficulty: Intermediate to Advanced**  
**Topics Covered: Filtering, sorting, missing data handling, categorical data, clipping**
