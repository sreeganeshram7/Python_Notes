# Day 7 – GroupBy & Aggregation: Answer Key

## Answer 1
```python
df = pd.DataFrame({
    'region': ['North', 'South', 'North', 'West'],
    'product': ['A', 'A', 'B', 'B'],
    'units': [10, 20, 15, 5],
    'price': [100, 100, 200, 150]
})
df['revenue'] = df['units'] * df['price']
print(df.groupby('region')['revenue'].sum())
```

**Output:**
```
region
North    4000
South    2000
West     750
Name: revenue, dtype: int64
```

---

## Answer 2
```python
print(df.groupby('product')['units'].sum())
print(df.groupby('product')['price'].mean())
```

---

## Answer 3
```python
s_df = pd.DataFrame({
    'class': ['X', 'X', 'Y', 'Y'],
    'student': ['A', 'B', 'C', 'D'],
    'marks': [80, 90, 70, 75]
})
print(s_df.groupby('class')['marks'].mean())
print(s_df.groupby('class')['marks'].max())
```

**Output:**
```
class
X    85.0
Y    72.5
Name: marks, dtype: float64

class
X    90
Y    75
Name: marks, dtype: int64
```

---

## Answer 4
```python
print(s_df.groupby('class')['marks'].agg(['min', 'max', 'mean', 'count']))
```

**Output:**
```
      min  max   mean  count
class
X      80   90  85.0      2
Y      70   75  72.5      2
```

---

## Answer 5
```python
df2 = pd.DataFrame({
    'category': ['Cat1', 'Cat1', 'Cat2'],
    'sub_category': ['S1', 'S2', 'S1'],
    'value': [10, 20, 30]
})
res = df2.groupby(['category', 'sub_category'])['value'].sum().reset_index()
print(res)
```

---

## Answer 6
```python
orders = pd.DataFrame({
    'customer_id': [1, 1, 2, 3],
    'order_id': [101, 102, 103, 104],
    'amount': [100, 150, 200, 300]
})
g = orders.groupby('customer_id')['amount'].agg(['sum', 'mean'])
g_sorted = g.sort_values('sum', ascending=False)
print(g_sorted)
```

---

## Answer 7
```python
vc = df['region'].value_counts()
vc_df = vc.reset_index()
vc_df.columns = ['value', 'count']
print(vc_df)
```

---

## Answer 8
```python
d = pd.DataFrame({
    'date': ['2025-01-01', '2025-01-10', '2025-02-05'],
    'sales': [100, 200, 300]
})
d['date'] = pd.to_datetime(d['date'])
res = d.groupby(d['date'].dt.to_period('M'))['sales'].sum()
print(res)
```

---

## Answer 9
```python
tdf = pd.DataFrame({
    'team': ['T1', 'T1', 'T2', 'T2'],
    'player': ['A', 'B', 'C', 'D'],
    'score': [10, 20, 15, 25]
})
idx = tdf.groupby('team')['score'].idxmax()
best = tdf.loc[idx]
print(best)
```

---

## Answer 10
```python
grouped = s_df.groupby('class')
filtered = grouped.filter(lambda g: g['marks'].mean() > 70)
print(filtered)
```

---

**Answer Key Complete**  
**Day 7 Difficulty: Intermediate to Advanced**  
**Topics Covered: GroupBy, aggregation functions, agg(), value_counts, filtering groups**
