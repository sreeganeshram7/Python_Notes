# Day 3 – NumPy Reshape, Aggregation, Broadcasting: Answer Key

## Answer 1
```python
arr = np.arange(1, 16)
b = arr.reshape(3, 5)
print(b, b.shape)
```

**Output:**
```
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]] (3, 5)
```

---

## Answer 2
```python
a = np.arange(2, 11).reshape(3, 3)
print(a.sum(), a.mean(), a.max(), a.min())
```

**Output:**
```
54 6.0 10 2
```

---

## Answer 3
```python
a = np.arange(16).reshape(4, 4)
print(a.sum(axis=1))  # row-wise
print(a.sum(axis=0))  # col-wise
```

**Output:**
```
[ 6 22 38 54]
[24 28 32 36]
```

---

## Answer 4
```python
A = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
print(A + b)
```

**Output:**
```
[[11 22 33]
 [14 25 36]]
```

---

## Answer 5
```python
c = np.array([[1], [2], [3]])
d = np.array([10, 20, 30, 40])
M = c + d
print(M)
```

**Output:**
```
[[11 21 31 41]
 [12 22 32 42]
 [13 23 33 43]]
```

---

## Answer 6
```python
a = np.arange(12).reshape(2, 6)
b = a.reshape(2, 2, 3)
print(a)
print(b)
```

**Output:**
```
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]
[[[ 0  1  2]
  [ 3  4  5]]

 [[ 6  7  8]
  [ 9 10 11]]]
```

---

## Answer 7
```python
a = np.arange(10).reshape(2, 5)
r = a.ravel()
f = a.flatten()
print(r)
print(f)
```

**Output:**
```
[0 1 2 3 4 5 6 7 8 9]
[0 1 2 3 4 5 6 7 8 9]
```

**Note:** `ravel()` returns a view (when possible), while `flatten()` always returns a copy.

---

## Answer 8
```python
np.random.seed(2)
A = np.random.randint(1, 20, size=(5, 3))
print(A.mean(axis=0))  # per column
print(A.mean(axis=1))  # per row
```

**Output:**
```
[10.6  9.4 11. ]
[10.         10.66666667  9.33333333 14.         11.66666667]
```

---

## Answer 9
```python
arr = np.array([1, 2, 2, 3, 3, 3, 4, 4])
vals, counts = np.unique(arr, return_counts=True)
print(vals, counts)
```

**Output:**
```
[1 2 3 4] [1 2 3 2]
```

---

## Answer 10
```python
arr = np.array([1, 2, 3, 4, 5])
print(arr + 10)
print(arr * 2)
```

**Output:**
```
[11 12 13 14 15]
[ 2  4  6  8 10]
```

---

**Answer Key Complete**  
**Day 3 Difficulty: Intermediate**  
**Topics Covered: Reshape, aggregation (sum/mean/max/min), axis operations, broadcasting**
