# Day 1 – NumPy Basics: Answer Key

## Answer 1
```python
import numpy as np

arr = np.arange(5, 15)
print(arr, arr.dtype, arr.ndim, arr.shape)
```

**Output:**
```
[ 5  6  7  8  9 10 11 12 13 14] int64 1 (10,)
```

---

## Answer 2
```python
lst = [2, 4, 6, 8, 10]
arr = np.array(lst)
arr = arr * 3
arr = arr - 2
print(arr)
```

**Output:**
```
[ 4 10 16 22 28]
```

---

## Answer 3
```python
a = np.arange(1, 10).reshape(3, 3)
print(a)
print(a.size, a.shape)
```

**Output:**
```
[[1 2 3]
 [4 5 6]
 [7 8 9]]
9 (3, 3)
```

---

## Answer 4
```python
z = np.zeros(10, dtype=int)
z[0] = 7
z[4] = 7
z[9] = 7
print(z)
```

**Output:**
```
[7 0 0 0 7 0 0 0 0 7]
```

---

## Answer 5
```python
arr = np.arange(1, 20, 2)
print(arr, arr.sum())
```

**Output:**
```
[ 1  3  5  7  9 11 13 15 17 19] 100
```

---

## Answer 6
```python
I = np.eye(4)
print(I)
```

**Output:**
```
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
```

---

## Answer 7
```python
np.random.seed(10)
r = np.random.randint(0, 21, size=6)
print(r)
print(r.max(), r.argmax())
```

**Output:**
```
[ 9 15 12 14 17  4]
17 4
```

---

## Answer 8
```python
a = np.array([1, 3, 5, 7])
b = np.array([2, 4, 6, 8])
print(a + b)
print(a * b)
print(b - a)
print(b / a)
```

**Output:**
```
[ 3  7 11 15]
[ 2 12 30 56]
[1 1 1 1]
[2.         1.33333333 1.2        1.14285714]
```

---

## Answer 9
```python
arr = np.arange(10, 20).reshape(2, 5)
print(arr[0, :])
print(arr[:, 1])
```

**Output:**
```
[10 11 12 13 14]
[11 16]
```

---

## Answer 10
```python
x = np.linspace(0, 5, 15)
print(x, x[:3], x[-3:])
```

**Output:**
```
[0.         0.35714286 0.71428571 1.07142857 1.42857143 1.78571429
 2.14285714 2.5        2.85714286 3.21428571 3.57142857 3.92857143
 4.28571429 4.64285714 5.        ] [0.         0.35714286 0.71428571] [3.92857143 4.64285714 5.        ]
```

---

**Answer Key Complete**  
**Day 1 Difficulty: Beginner**  
**Topics Covered: Array creation, dtype, shape, basic operations, indexing**
