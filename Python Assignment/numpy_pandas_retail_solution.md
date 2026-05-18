# NumPy and Pandas Retail Sales Analysis Project
## Complete Solution with Python Code

---

## Project Overview

**Dataset:** Retail Sales Transaction Data (50 transactions)
**Goal:** Analyze retail revenue, customer segments, and sales patterns using NumPy and Pandas
**Time Period:** January 2024
**Tools:** Python, NumPy, Pandas

---

## Complete Python Solution

### Import Libraries and Load Data

```python
import pandas as pd
import numpy as np
from io import StringIO

# Create dataset from CSV string
csv_data = '''TransactionID,Date,CustomerID,Gender,Age,ProductCategory,Quantity,PricePerUnit,TotalAmount
T0001,2024-01-03,C001,Male,28,Electronics,1,45000,45000
T0002,2024-01-03,C002,Female,35,Clothing,3,1200,3600
T0003,2024-01-04,C003,Female,22,Grocery,15,80,1200
T0004,2024-01-04,C001,Male,28,Electronics,2,1500,3000
T0005,2024-01-05,C004,Male,42,Furniture,1,18000,18000
T0006,2024-01-05,C005,Female,30,Clothing,2,1500,3000
T0007,2024-01-06,C006,Female,26,Beauty,4,600,2400
T0008,2024-01-06,C007,Male,33,Grocery,10,90,900
T0009,2024-01-07,C008,Male,39,Electronics,1,52000,52000
T0010,2024-01-07,C009,Female,24,Clothing,5,900,4500
T0011,2024-01-08,C010,Male,31,Sports,2,2500,5000
T0012,2024-01-08,C011,Female,29,Beauty,3,700,2100
T0013,2024-01-09,C012,Female,41,Furniture,1,22000,22000
T0014,2024-01-09,C002,Female,35,Grocery,8,95,760
T0015,2024-01-10,C003,Female,22,Clothing,2,1100,2200
T0016,2024-01-10,C004,Male,42,Electronics,1,38000,38000
T0017,2024-01-11,C005,Female,30,Home Decor,3,1600,4800
T0018,2024-01-11,C006,Female,26,Grocery,12,85,1020
T0019,2024-01-12,C007,Male,33,Sports,1,3200,3200
T0020,2024-01-12,C008,Male,39,Clothing,4,1300,5200
T0021,2024-01-13,C009,Female,24,Beauty,6,550,3300
T0022,2024-01-13,C010,Male,31,Electronics,1,41000,41000
T0023,2024-01-14,C011,Female,29,Home Decor,2,1900,3800
T0024,2024-01-14,C012,Female,41,Grocery,20,70,1400
T0025,2024-01-15,C001,Male,28,Clothing,1,1500,1500
T0026,2024-01-15,C002,Female,35,Furniture,1,25000,25000
T0027,2024-01-16,C003,Female,22,Beauty,2,800,1600
T0028,2024-01-16,C004,Male,42,Sports,1,2800,2800
T0029,2024-01-17,C005,Female,30,Grocery,18,75,1350
T0030,2024-01-17,C006,Female,26,Electronics,1,46000,46000
T0031,2024-01-18,C007,Male,33,Home Decor,4,1400,5600
T0032,2024-01-18,C008,Male,39,Clothing,3,1250,3750
T0033,2024-01-19,C009,Female,24,Grocery,9,85,765
T0034,2024-01-19,C010,Male,31,Furniture,1,19500,19500
T0035,2024-01-20,C011,Female,29,Electronics,1,50000,50000
T0036,2024-01-20,C012,Female,41,Beauty,5,650,3250
T0037,2024-01-21,C001,Male,28,Grocery,14,80,1120
T0038,2024-01-21,C002,Female,35,Clothing,4,1400,5600
T0039,2024-01-22,C003,Female,22,Home Decor,2,1700,3400
T0040,2024-01-22,C004,Male,42,Sports,3,2600,7800
T0041,2024-01-23,C005,Female,30,Furniture,1,23000,23000
T0042,2024-01-23,C006,Female,26,Clothing,2,1350,2700
T0043,2024-01-24,C007,Male,33,Electronics,1,37000,37000
T0044,2024-01-24,C008,Male,39,Beauty,4,720,2880
T0045,2024-01-25,C009,Female,24,Grocery,11,90,990
T0046,2024-01-25,C010,Male,31,Home Decor,3,1500,4500
T0047,2024-01-26,C011,Female,29,Clothing,5,1000,5000
T0048,2024-01-26,C012,Female,41,Sports,2,3000,6000
T0049,2024-01-27,C001,Male,28,Furniture,1,21000,21000
T0050,2024-01-27,C002,Female,35,Electronics,1,49000,49000'''

# Load into DataFrame
df = pd.read_csv(StringIO(csv_data))

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create Age Groups
bins = [0, 18, 25, 35, 50, 100]
labels = ['<18', '18-25', '26-35', '36-50', '50+']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

# Extract time features
df['Month'] = df['Date'].dt.to_period('M')
df['Weekday'] = df['Date'].dt.day_name()

print("Dataset loaded successfully!")
print(f"Shape: {df.shape}")
print(f"\nFirst 5 rows:\n{df.head()}")
```

---

## Section A: Basic Exploration

```python
# Q1: Rows and Columns
print("=" * 60)
print("Q1: Dataset Dimensions")
print("=" * 60)
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# Q2: Data Types
print("\n" + "=" * 60)
print("Q2: Data Types")
print("=" * 60)
print(df.dtypes)

# Q3: Missing Values
print("\n" + "=" * 60)
print("Q3: Missing Values")
print("=" * 60)
print(df.isnull().sum())

# Q4: Basic Statistics
print("\n" + "=" * 60)
print("Q4: Basic Statistics")
print("=" * 60)
print("Age Statistics:")
print(df['Age'].describe())
print("\nQuantity Statistics:")
print(df['Quantity'].describe())
print("\nPrice Per Unit Statistics:")
print(df['PricePerUnit'].describe())
print("\nTotal Amount Statistics:")
print(df['TotalAmount'].describe())

# Q5: Unique Counts
print("\n" + "=" * 60)
print("Q5: Unique Counts")
print("=" * 60)
print(f"Unique Customers: {df['CustomerID'].nunique()}")
print(f"Unique Categories: {df['ProductCategory'].nunique()}")
print(f"\nCategories: {df['ProductCategory'].unique()}")
```

### Answers to Section A

**Q1:** 50 rows, 12 columns

**Q2:** TransactionID (object), Date (datetime64), CustomerID (object), Gender (object), Age (int64), ProductCategory (object), Quantity (int64), PricePerUnit (int64), TotalAmount (int64), AgeGroup (category), Month (period[M]), Weekday (object)

**Q3:** No missing values in any column

**Q4:** Age: min 22, max 42, mean 31.32; Quantity: min 1, max 20, mean 5.42; PricePerUnit: min 70, max 52000; TotalAmount: min 765, max 52000

**Q5:** 12 unique customers, 7 unique categories

---

## Section B: Revenue and Product Analysis

```python
# Q6: Total Revenue
total_revenue = df['TotalAmount'].sum()
print(f"Total Revenue: ₹{total_revenue:,.2f}")

# Q7: Top 3 Categories by Revenue
rev_by_cat = df.groupby('ProductCategory')['TotalAmount'].sum().sort_values(ascending=False)
print(rev_by_cat.head(3))

# Q8: Per-Category Metrics
metrics_by_cat = df.groupby('ProductCategory').agg(
    total_revenue=('TotalAmount', 'sum'),
    avg_revenue=('TotalAmount', 'mean'),
    total_qty=('Quantity', 'sum'),
    txn_count=('TransactionID', 'count')
).sort_values('total_revenue', ascending=False)
print(metrics_by_cat)

# Q9: Highest Average Price Per Unit
avg_price_by_cat = df.groupby('ProductCategory')['PricePerUnit'].mean().sort_values(ascending=False)
print(f"Highest: {avg_price_by_cat.idxmax()} at ₹{avg_price_by_cat.max():,.2f}")

# Q10: Revenue Per Unit
rev_per_unit = (df.groupby('ProductCategory')['TotalAmount'].sum() / 
                df.groupby('ProductCategory')['Quantity'].sum()).sort_values(ascending=False)
print(f"Highest: {rev_per_unit.idxmax()} at ₹{rev_per_unit.max():,.2f} per unit")
```

### Answers to Section B

**Q6:** Total Revenue = ₹598,485

**Q7:** 
1. Electronics: ₹361,000
2. Furniture: ₹128,500
3. Clothing: ₹37,050

**Q8:** Electronics has highest total (361k) and average (40.1k per txn) with 10 units sold

**Q9:** Electronics at ₹39,944.44 average price per unit

**Q10:** Electronics at ₹36,100 revenue per unit

---

## Section C: Customer and Segment Analysis

```python
# Q11: Age Group Metrics
agegroup_metrics = df.groupby('AgeGroup').agg(
    txn_count=('TransactionID', 'count'),
    total_revenue=('TotalAmount', 'sum'),
    avg_amount=('TotalAmount', 'mean')
)
print(agegroup_metrics)

# Q12: AgeGroup x Gender Segment Analysis
segment_metrics = df.groupby(['AgeGroup', 'Gender']).agg(
    total_revenue=('TotalAmount', 'sum'),
    avg_amount=('TotalAmount', 'mean'),
    txn_count=('TransactionID', 'count')
).sort_values('total_revenue', ascending=False)
print(segment_metrics.head())

# Q13: Top 10 Customers
top_customers = df.groupby('CustomerID')['TotalAmount'].sum().sort_values(ascending=False).head(10)
print(top_customers)

# Q14: Top 10 Customers - Detailed
top_ids = top_customers.index
cust_detail = df[df['CustomerID'].isin(top_ids)].groupby('CustomerID').agg(
    total_revenue=('TotalAmount', 'sum'),
    txn_count=('TransactionID', 'count'),
    avg_order_value=('TotalAmount', 'mean'),
    avg_qty=('Quantity', 'mean')
).sort_values('total_revenue', ascending=False)
print(cust_detail)
```

### Answers to Section C

**Q11:** 26-35 age group: 25 transactions, ₹333,490 total, ₹13,339.60 avg; 36-50 age group: 17 transactions, ₹247,040 total, ₹14,531.76 avg

**Q12:** Most valuable: (26-35, Male) with ₹188,320 total revenue

**Q13:** C002 (₹83,960), C001 (₹71,620), C010 (₹70,000)

**Q14:** Top customers have AOV ranging from ₹8,037.50 to ₹17,500

---

## Section D: Time-Based Analysis

```python
# Q15: Date Features
print(f"Period: {df['Date'].min().date()} to {df['Date'].max().date()}")
print(f"All transactions in January 2024")

# Q16: Monthly Metrics
month_metrics = df.groupby('Month').agg(
    total_revenue=('TotalAmount', 'sum'),
    txn_count=('TransactionID', 'count'),
    avg_amount=('TotalAmount', 'mean')
)
print(month_metrics)

# Q17: Weekday Revenue
weekday_revenue = df.groupby('Weekday')['TotalAmount'].sum().sort_values(ascending=False)
print(weekday_revenue)

# Q18: High-Performing Days
avg_daily = df.groupby('Weekday')['TotalAmount'].mean().mean()
high_days = weekday_revenue[weekday_revenue > avg_daily]
print(high_days)
```

### Answers to Section D

**Q15:** All transactions in January 2024

**Q16:** January 2024: Total revenue ₹598,485, 50 transactions, avg ₹11,969.70 per transaction

**Q17:** Best day: Wednesday (₹176,030), followed by Saturday (₹170,850)

**Q18:** Days above average: Wednesday, Saturday, Sunday, Friday

---

## Section E: NumPy-Focused Analysis

```python
# Q19: NumPy Statistics
amounts = df['TotalAmount'].to_numpy()
mean_amt = np.mean(amounts)
std_amt = np.std(amounts)
percentiles = np.percentile(amounts, [25, 50, 75, 90, 95])

print(f"Mean: ₹{mean_amt:,.2f}")
print(f"Std Dev: ₹{std_amt:,.2f}")
print(f"Percentiles: {percentiles}")

# Q20: Z-Score Normalization
z_scores = (amounts - mean_amt) / std_amt
z_outliers_mask = z_scores > 2
z_outliers_idx = np.where(z_outliers_mask)[0]

print(f"Number of outliers (Z > 2): {len(z_outliers_idx)}")
print(df.iloc[z_outliers_idx][['TransactionID', 'TotalAmount', 'ProductCategory']])

# Q21: Average Order Value
aov = np.mean(amounts)
print(f"AOV: ₹{aov:,.2f}")

# Q22: Electronics Analysis (NumPy)
categories = df['ProductCategory'].to_numpy()
mask_elec = categories == 'Electronics'
elec_amounts = amounts[mask_elec]

print(f"Electronics Mean: ₹{np.mean(elec_amounts):,.2f}")
print(f"Electronics Std: ₹{np.std(elec_amounts):,.2f}")
```

### Answers to Section E

**Q19:** Mean ₹11,969.70, Std ₹15,694.67, Percentiles: 25th ₹2,250, 50th ₹3,775, 75th ₹19,125, 90th ₹41,400, 95th ₹47,650

**Q20:** 5 outliers with Z-score > 2: T0001 (45k), T0009 (52k), T0030 (46k), T0035 (50k), T0050 (49k)

**Q21:** AOV = ₹11,969.70

**Q22:** Electronics mean ₹40,111.11, std ₹14,019.39

---

## Section F: Business Insights & Recommendations

```python
# Q23: Top Customer Segments
print("Top 3 Most Valuable Customer Segments:")
top_segments = segment_metrics.head(3)
for (age_group, gender), row in top_segments.iterrows():
    print(f"{age_group}, {gender}: ₹{row['total_revenue']:,.2f}")

# Q24: Categories for Promotion
print("\nCategories for Promotion:")
print("Grocery: High volume (117 units), low value (₹81 per unit)")
print("Clothing & Beauty: Mid-range, frequent purchases")

# Q25: Strategic Recommendations
print("\nRecommendation 1: Target 26-35 and 36-50 age groups")
print("Recommendation 2: Leverage peak days (Wednesday, Saturday)")
```

### Answers to Section F

**Q23:** 
1. Age 26-35, Male: ₹188,320
2. Age 26-35, Female: ₹145,170
3. Age 36-50, Male: ₹130,430

**Q24:** 
- Grocery: Volume discounts for high-quantity purchases
- Clothing & Beauty: Seasonal promotions and loyalty programs

**Q25:**
1. Focus premium marketing on 26-35 and 36-50 age groups
2. Optimize operations on high-traffic days (Wednesday, Saturday)

---

## Key Findings Summary

| Metric | Value |
|--------|-------|
| **Total Revenue** | ₹598,485 |
| **Average Order Value** | ₹11,969.70 |
| **Total Transactions** | 50 |
| **Unique Customers** | 12 |
| **Product Categories** | 7 |
| **Top Category** | Electronics (60.3%) |
| **Best Day** | Wednesday |
| **Best Customer Segment** | Age 26-35, Male |

---

## How to Use This Code

1. Copy the complete code into a Jupyter notebook or Python file
2. Run each section sequentially
3. Modify the CSV data to use your own dataset
4. Export results using `df.to_csv()`

**Project Completed Successfully!**
