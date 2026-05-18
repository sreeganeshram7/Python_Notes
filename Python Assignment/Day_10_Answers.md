# Day 10 – Mixed Practice (NumPy + Pandas): Answer Key

## Answer 1
```python
arr = np.arange(1, 26).reshape(5, 5)
df = pd.DataFrame(arr, columns=['C1', 'C2', 'C3', 'C4', 'C5'])
print(df.head(2))
print(df.tail(2))
```

**Output:**
```
   C1  C2  C3  C4  C5
0   1   2   3   4   5
1   6   7   8   9  10
   C1  C2  C3  C4  C5
3  16  17  18  19  20
4  21  22  23  24  25
```

---

## Answer 2
```python
np.random.seed(0)
arr = np.random.randint(0, 101, size=10)
s = pd.Series(arr)
print(s[s > s.mean()])
```

---

## Answer 3
```python
c = np.array([25, 30, 28, 22, 26])
f = c * 9/5 + 32
df = pd.DataFrame({'celsius': c, 'fahrenheit': f})
print(df)
```

**Output:**
```
   celsius  fahrenheit
0       25       77.0
1       30       86.0
2       28       82.4
3       22       71.6
4       26       78.8
```

---

## Answer 4
```python
df = pd.DataFrame({
    'id': [1, 2, 3],
    'maths': [80, 70, 90],
    'science': [75, 85, 95],
    'english': [78, 88, 92]
})
df['total'] = df[['maths', 'science', 'english']].sum(axis=1)
df['avg'] = df['total'] / 3
print(df)
```

---

## Answer 5
```python
np.random.seed(1)
arr = np.random.randint(1, 10, size=(3, 3))
df = pd.DataFrame(arr,
                  columns=['Col1', 'Col2', 'Col3'],
                  index=['Row1', 'Row2', 'Row3'])
print(df)
```

---

## Answer 6
```python
df = pd.DataFrame({'score': [45, 82, 60, 30]})
df['grade'] = np.where(
    df['score'] >= 80, 'A',
    np.where(df['score'] >= 50, 'B', 'C')
)
print(df)
```

**Output:**
```
   score grade
0     45     C
1     82     A
2     60     B
3     30     C
```

---

## Answer 7
```python
arr = np.arange(12).reshape(3, 4)
df = pd.DataFrame(arr, columns=['A', 'B', 'C', 'D'])
df['row_sum'] = df[['A', 'B', 'C', 'D']].sum(axis=1)
print(df[df['row_sum'] > 15])
```

**Output:**
```
   A  B   C   D  row_sum
1   4  5   6   7       22
2   8  9  10  11       38
```

---

## Answer 8
```python
df = pd.DataFrame({'age': [15, 22, 35, 42, 60]})
df['age_group'] = pd.cut(
    df['age'],
    bins=[0, 18, 35, 60, 100],
    labels=['0-18', '19-35', '36-60', '60+']
)
print(df['age_group'].value_counts())
```

**Output:**
```
age_group
19-35    2
0-18     1
36-60    1
60+      1
Name: count, dtype: int64
```

---

## Answer 9
```python
arr = np.array([1.2345, 2.3456, 3.9876])
s = pd.Series(arr)
s_round = s.round(2)
print(s_round)
```

**Output:**
```
0    1.23
1    2.35
2    3.99
dtype: float64
```

---

## Answer 10
```python
df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [10, 20, 30, 40]})
mask = df['x'] % 2 == 0
print(df[mask])
```

**Output:**
```
   x   y
1  2  20
3  4  40
```

---

**Answer Key Complete**  
**Day 10 Difficulty: Advanced**  
**Topics Covered: All NumPy and pandas fundamentals combined, practical applications**
