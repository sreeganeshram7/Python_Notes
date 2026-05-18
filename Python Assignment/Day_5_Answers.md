# Day 5 – pandas DataFrame Creation & Basic Operations: Answer Key

## Answer 1
```python
df = pd.DataFrame({
    'name': ['A', 'B', 'C', 'D', 'E'],
    'age': [18, 19, 20, 21, 22],
    'maths': [80, 75, 90, 85, 88]
})
print(df)
print(df.info())
print(df.describe())
```

**Output:**
```
  name  age  maths
0    A   18     80
1    B   19     75
2    C   20     90
3    D   21     85
4    E   22     88
```

---

## Answer 2
```python
data = {
    'city': ['A', 'B', 'C', 'D'],
    'temp': [30, 22, 25, 28],
    'humidity': [65, 70, 68, 72]
}
df = pd.DataFrame(data)
print(df.head(3))
print(df[['city', 'temp']])
```

**Output:**
```
  city  temp  humidity
0    A    30        65
1    B    22        70
2    C    25        68

  city  temp
0    A    30
1    B    22
2    C    25
3    D    28
```

---

## Answer 3
```python
df['temp_f'] = df['temp'] * 9/5 + 32
print(df)
```

**Output:**
```
  city  temp  humidity  temp_f
0    A    30        65    86.0
1    B    22        70    71.6
2    C    25        68    77.0
3    D    28        72    82.4
```

---

## Answer 4
```python
df['A_plus_B'] = df['A'] + df['B']
df['C_squared'] = df['C'] ** 2
print(df)
```

---

## Answer 5
```python
df = pd.DataFrame(np.random.randint(1, 100, size=(6, 3)),
                  columns=['c1', 'c2', 'c3'])
print(df[df['c1'] > 50])
print(df[df['c2'].isin([10, 20, 30])])
```

---

## Answer 6
```python
print(df.loc[0])        # Single row by label
print(df.iloc[1])       # Single row by position
print(df.loc[1:3, ['c1', 'c2']])  # Rows 1-3, specific columns
```

---

## Answer 7
```python
df = pd.DataFrame({
    'student_id': [101, 102, 103],
    'name': ['A', 'B', 'C'],
    'marks': [80, 85, 90]
})
df = df.set_index('student_id')
df = df.reset_index()
print(df)
```

---

## Answer 8
```python
print(df['marks'].mean())
idx = df['marks'].idxmax()
print(df.loc[idx])
```

---

## Answer 9
```python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
df = df.rename(columns={'A': 'X'})
df2 = df.drop(columns=['B'])
df3 = df.drop(index=0)
```

---

## Answer 10
```python
df = pd.DataFrame({'text': ['hello', 'world', 'pandas']})
df['upper'] = df['text'].str.upper()
df['length'] = df['text'].str.len()
print(df)
```

**Output:**
```
    text  upper  length
0  hello  HELLO       5
1  world  WORLD       5
2  pandas  PANDAS       6
```

---

**Answer Key Complete**  
**Day 5 Difficulty: Intermediate**  
**Topics Covered: DataFrame creation, column operations, row/column selection, indexing, string operations**
