# Day 4 – pandas Series: Answer Key

## Answer 1
```python
import pandas as pd
import numpy as np

s = pd.Series([5, 10, 15, 20], index=['p', 'q', 'r', 's'])
print(s)
print(s['r'])
```

**Output:**
```
p     5
q    10
r    15
s    20
dtype: int64
15
```

---

## Answer 2
```python
arr = np.array([2, 4, 6, 8, 10])
s = pd.Series(arr)
print(s.head(2))
print(s.tail(2))
```

**Output:**
```
0    2
1    4
dtype: int64
3     8
4    10
dtype: int64
```

---

## Answer 3
```python
names = ['Ankit', 'Bhavna', 'Chetan', 'Deepa']
marks = [65, 82, 74, 91]
s = pd.Series(marks, index=names)
print(s.mean())
print(s[s > 80])
```

**Output:**
```
78.0
Bhavna    82
Deepa     91
dtype: int64
```

---

## Answer 4
```python
s = pd.Series({'Delhi': 35, 'Mumbai': 32, 'Pune': 28})
print(s[['Delhi', 'Pune']])
print(s[s > 30])
```

**Output:**
```
Delhi    35
Pune     28
dtype: int64
Delhi    35
Mumbai   32
dtype: int64
```

---

## Answer 5
```python
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([10, 20, 30], index=['b', 'c', 'd'])
print(s1 + s2)
# Non-common indices get NaN
```

**Output:**
```
a     NaN
b    22.0
c    33.0
d     NaN
dtype: float64
```

---

## Answer 6
```python
s = pd.Series([1, np.nan, 3, np.nan, 5])
print(s.isna())
print(s.dropna())
```

**Output:**
```
0    False
1     True
2    False
3     True
4    False
dtype: bool
0    1.0
2    3.0
4    5.0
dtype: float64
```

---

## Answer 7
```python
prices = {'pen': 10, 'pencil': 5, 'notebook': 50}
s = pd.Series(prices)
s = s * 1.05
print(s)
```

**Output:**
```
pen          10.5
pencil        5.25
notebook     52.5
dtype: float64
```

---

## Answer 8
```python
np.random.seed(3)
s = pd.Series(np.random.randint(10, 101, size=8))
print(s[s > 50])
print(s.max(), s.min(), s.mean())
```

**Output:**
```
0    52
3    77
4    76
5    73
dtype: int64
77 12 54.875
```

---

## Answer 9
```python
s = pd.Series([1, 2, 3, 4])
print(s.apply(lambda x: x**3))
print(s.apply(lambda x: f"num_{x}"))
```

**Output:**
```
0     1
1     8
2    27
3    64
dtype: int64
0    num_1
1    num_2
2    num_3
3    num_4
dtype: object
```

---

## Answer 10
```python
s = pd.Series([1, 2, 2, 3, 3, 3])
print(s.value_counts())
```

**Output:**
```
3    3
2    2
1    1
dtype: int64
```

---

**Answer Key Complete**  
**Day 4 Difficulty: Intermediate**  
**Topics Covered: Series creation, indexing, slicing, apply, value_counts, missing data**
