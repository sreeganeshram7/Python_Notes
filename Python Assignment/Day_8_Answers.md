# Day 8 – Merge, Join, Concat: Answer Key

## Answer 1
```python
df_customers = pd.DataFrame({'customer_id': [1, 2, 3],
                            'name': ['A', 'B', 'C']})
df_orders = pd.DataFrame({'order_id': [101, 102, 103],
                         'customer_id': [1, 2, 2]})
inner = pd.merge(df_customers, df_orders, on='customer_id', how='inner')
print(inner)
```

---

## Answer 2
```python
left = pd.merge(df_customers, df_orders, on='customer_id', how='left')
right = pd.merge(df_customers, df_orders, on='customer_id', how='right')
print(f"Left rows: {len(left)}, Right rows: {len(right)}")
```

---

## Answer 3
```python
df1 = pd.DataFrame({'id': [1, 2], 'value1': [10, 20]})
df2 = pd.DataFrame({'id': [2, 3], 'value2': [200, 300]})
outer = pd.merge(df1, df2, on='id', how='outer')
print(outer)
```

**Output:**
```
   id  value1  value2
0   1    10.0     NaN
1   2    20.0   200.0
2   3     NaN   300.0
```

---

## Answer 4
```python
m1 = pd.DataFrame({'month': ['Jan', 'Jan'], 'sales': [10, 20]})
m2 = pd.DataFrame({'month': ['Feb', 'Feb'], 'sales': [15, 25]})
df_all = pd.concat([m1, m2], ignore_index=True)
print(df_all)
```

---

## Answer 5
```python
a = pd.DataFrame({'A': [1, 2]}, index=[0, 1])
b = pd.DataFrame({'B': [3, 4]}, index=[0, 1])
res = pd.concat([a, b], axis=1)
print(res)
```

---

## Answer 6
```python
new_row = pd.DataFrame({'A': [5], 'B': [6]})
df = pd.concat([res, new_row], ignore_index=True)
print(df)
```

---

## Answer 7
```python
df1 = pd.DataFrame({'key': [1, 2], 'A': ['x', 'y']})
df2 = pd.DataFrame({'key': [2, 3], 'B': ['p', 'q']})
merged = pd.merge(df1, df2, on='key', how='left', indicator=True)
only_left = merged[merged['_merge'] == 'left_only']
print(only_left)
```

---

## Answer 8
```python
df1 = pd.DataFrame({'city': ['A', 'A'], 'year': [2024, 2025], 'val1': [1, 2]})
df2 = pd.DataFrame({'city': ['A', 'B'], 'year': [2024, 2025], 'val2': [10, 20]})
m = pd.merge(df1, df2, on=['city', 'year'], how='inner')
print(m)
```

---

## Answer 9
```python
products = pd.DataFrame({'prod_id': [1, 2], 'price': [100, 200]})
disc = pd.DataFrame({'prod_id': [1, 2], 'discount': [0.1, 0.2]})
m = pd.merge(products, disc, on='prod_id')
m['final_price'] = m['price'] * (1 - m['discount'])
print(m)
```

---

## Answer 10
```python
df_a = pd.DataFrame({'A': [1, 2]})
df_b = pd.DataFrame({'A': [3, 4]})
res = pd.concat({'first': df_a, 'second': df_b})
print(res)
```

**Output:**
```
        A
first  0  1
       1  2
second 0  3
       1  4
```

---

**Answer Key Complete**  
**Day 8 Difficulty: Intermediate to Advanced**  
**Topics Covered: Merge (inner, left, right, outer), concat, hierarchical indexing**
