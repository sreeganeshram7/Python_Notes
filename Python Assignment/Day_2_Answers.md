# Day 2 – NumPy Indexing & Slicing: Answer Key

## Answer 1
```python
arr = np.arange(20)
print(arr[4:11])
print(arr[::3])
```

**Output:**
```
[ 4  5  6  7  8  9 10]
[ 0  3  6  9 12 15 18]
```

---

## Answer 2
```python
a = np.arange(12).reshape(3, 4)
print(a[1, :])
print(a[:, -1])
print(a[2, 1])
```

**Output:**
```
[4 5 6 7]
[ 3  7 11]
9
```

---

## Answer 3
```python
arr = np.arange(1, 13)
idx = [0, 3, 5, 7, 11]
print(arr[idx])
```

**Output:**
```
[ 1  4  6  8 12]
```

---

## Answer 4
```python
a = np.arange(1, 17).reshape(4, 4)
print(a[1:3, 1:3])
print(np.diag(a))
```

**Output:**
```
[[ 6  7]
 [10 11]]
[ 1  6 11 16]
```

---

## Answer 5
```python
arr = np.arange(10, 20)
print(arr[::-1])
print(np.flip(arr))
```

**Output:**
```
[19 18 17 16 15 14 13 12 11 10]
[19 18 17 16 15 14 13 12 11 10]
```

---

## Answer 6
```python
a = np.arange(25).reshape(5, 5)
print(a[0:2, :])
print(a[:, -2:])
```

**Output:**
```
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]]
[[ 3  4]
 [ 8  9]
 [13 14]
 [18 19]
 [23 24]]
```

---

## Answer 7
```python
a = np.arange(1, 10).reshape(3, 3)
a[a > 5] = 0
print(a)
```

**Output:**
```
[[1 2 3]
 [4 5 0]
 [0 0 0]]
```

---

## Answer 8
```python
np.random.seed(1)
arr = np.random.randint(1, 51, size=10)
print(arr[arr > 30])
print(arr[arr % 2 == 0])
```

**Output:**
```
[37 47 33 44]
[38 44 44 28]
```

---

## Answer 9
```python
a = np.arange(1, 13).reshape(4, 3)
print(a[:, 0])
print(a[-1, :])
```

**Output:**
```
[ 1  4  7 10]
[10 11 12]
```

---

## Answer 10
```python
arr = np.arange(10)
idx = [1, 3, 5, 7, 9]
arr[idx] = -1
print(arr)
```

**Output:**
```
[ 0 -1  2 -1  4 -1  6 -1  8 -1]
```

---

**Answer Key Complete**  
**Day 2 Difficulty: Beginner to Intermediate**  
**Topics Covered: Indexing, slicing, boolean masking, fancy indexing**
