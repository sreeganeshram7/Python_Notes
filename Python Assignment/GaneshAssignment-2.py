# Generated from: GaneshAssignment-2.ipynb
# Converted at: 2025-12-20T08:57:48.638Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# ## ASSIGNMENT 2: NumPy for Numeric Data
# ## Q2.1: Array Creation and Shape
# #### Load the regional performance data into NumPy arrays and display the shape and data types.
import pandas as pd
import numpy as np
df=pd.read_csv('assignment2_regional_performance(in).csv')
df
shape=df.shape
print(f"Shape:{shape}")
data=df.values
print(f"DataTypes:{data}")
regional_performance=df[['RegionName','Q1Revenue','Q2Revenue','Q3Revenue','Q4Revenue']]
regional_performance
regional_shape=regional_performance.shape
print(f"Regional_performance shape:{regional_shape}")
regional_data=regional_performance.values
print(f"Regional_performance datatypes:{regional_data}")

# ## Q2.2: Annual Revenue Calculation
# #### Calculate the total annual revenue for each region (sum of Q1, Q2, Q3, Q4 revenues)
region=df[['Q1Revenue','Q2Revenue','Q3Revenue','Q4Revenue']]
region
total_revenue=region.sum(axis=1)
total_revenue
print("Annual Revenue per Region:")
for i, region in enumerate(df['RegionName']):
    print(f"{region}: ${total_revenue[i]:,.0f}")

# ## Q2.3: Quarterly Average
# #### Find the average units sold per quarter across all regions
region_units=df[['Q1Units','Q2Units','Q3Units','Q4Units']]
region_units
region_unit=df[['Q1Units','Q2Units','Q3Units','Q4Units']].values
region_unit
avg_units=region_units.mean(axis=1)
avg_units
print("Average Units per Region:")
for i, region_units in enumerate(df['RegionName']):
    print(f"{region_units}: ${avg_units[i]:,.0f}")

# ## Q2.4: Conditional Filtering
# #### Identify regions where Q4 revenue is higher than the annual average revenue.
Filter_region=df[['Q1Revenue','Q2Revenue','Q3Revenue','Q4Revenue']].values
Filter_region
q4_revenue=Filter_region[:,3]
q4_revenue
avg_revenue=total_revenue.mean()
print(f"Average Revenue:{avg_revenue}")
high_q4=q4_revenue>avg_revenue
print(f"High_Q4_Salary:{high_q4}")
high_q4_regions= df.loc[high_q4, 'RegionName'].tolist()
print(f"High_Q4_Regions:{high_q4_regions}")

# ## Q2.5: 2D Matrix Operations
# #### Create a 2D matrix of quarterly revenues and compute column-wise totals (total revenue per quarter)
quarter=['Quarter_1','Quarter_2','Quarter_3','Quarter_4']
revenue_matrix=Filter_region
quarterly_revenue=revenue_matrix.sum(axis=0)
quarterly_revenue
print("Total Revenue per Quarter")
for q, total in zip(quarter, quarterly_revenue):
    print(f"{q}:${total:,.0f}")

# ## Q2.6: Min-Max Normalization
# #### Normalize all revenue values between 0 and 1 using min-max normalization.
revenue_flat=Filter_region.flatten()
normalized=(revenue_flat/revenue_flat.min())/(revenue_flat.max()-revenue_flat.min())
normalized
print("Normalized (first 10):")
print(normalized[:10])
print(f"Min: {normalized.min()}, Max: {normalized.max()}")

# ## Q2.7: Boolean Masking
# #### Use Boolean indexing to filter regions with total annual revenue > 500,000.
total_revenue
high_revenue_mask =total_revenue>500000
high_revenue_mask
high_revenue_regions = df.loc[high_revenue_mask,['RegionName', 'Q1Revenue', 'Q2Revenue', 'Q3Revenue', 'Q4Revenue']]
print("Regions with revenue > $500,000:")
print(high_revenue_regions)

# ## Q2.8: Element-wise Division
# #### Calculate the revenue per unit for each region and quarter (Revenue / Units).
quarter=['Quarter_1','Quarter_2','Quarter_3','Quarter_4']
revenue_per_unit=Filter_region/region_unit
revenue_per_unit
print("Revenue per Unit for each regions:")
for i in range(len(revenue_per_unit)):
    print(f"\n{df.loc[i, 'RegionName']}:")
    for q, val in zip(quarter,revenue_per_unit[i]):
        print(f"{q}: ${val:,.2f}")

# ## Q2.9: Statistical Analysis
# #### Calculate the standard deviation of revenue and identify outlier regions (> 2 std deviations from mean).
revenue_mean=revenue_flat.mean()
print(f"Revenue_Mean:{revenue_flat_mean:,.0f}")
revenue_std=revenue_flat.std()
print(f"Revenue_Std:{revenue_flat_std:,.0f}")
outlier=np.abs(revenue_flat-revenue_mean)>2*revenue_std
outlier
num_outliers = outlier.sum()
print(f"Number of outlier values: {num_outliers}")

# ## Q2.10: Correlation Matrix
# #### Create a correlation matrix between quarterly revenues using NumPy.
corr_matrix = np.corrcoef(Filter_region)
print("Correlation Matrix (Quarterly Revenues):")
print("Quarters: Q1, Q2, Q3, Q4")
print(corr_matrix)
corr_matrix = np.corrcoef(Filter_region.T) # Transpose is used to fixed the matrix automatically by the dataframe
print(f"Correlation_Matrix:{corr_matrix}")

# ## Challenge Extension
# ### Challenge 1
# #### Create a 3D array structure and perform multi-axis operations.
arr = np.arange(1,37).reshape(3,3,4)    
arr
# It is happened between the layers and rows
print(f"Sum of a 3D array:{np.sum(arr,axis=(0,1))}")
print(f"Minimum of a 3D array:{np.min(arr,axis=(0,1))}")
print(f"Maximum of a 3D array:{np.max(arr,axis=(0,1))}")
print(f"Mean of a 3D array:{np.mean(arr,axis=(0,1))}")
print(f"Standard Deviation of a 3D array:{np.std(arr,axis=(0,1))}")
# It is happened between the cols and rows
print(f"Sum of a 3D array:{np.sum(arr,axis=(1,2))}")
print(f"Minimum of a 3D array:{np.min(arr,axis=(1,2))}")
print(f"Maximum of a 3D array:{np.max(arr,axis=(1,2))}")
print(f"Mean of a 3D array:{np.mean(arr,axis=(1,2))}")
print(f"Standard Deviation of a 3D array:{np.std(arr,axis=(1,2))}")
# It is happened between the cols and layers
print(f"Sum of a 3D array:{np.sum(arr,axis=(1,0))}")
print(f"Minimum of a 3D array:{np.min(arr,axis=(1,0))}")
print(f"Maximum of a 3D array:{np.max(arr,axis=(1,0))}")
print(f"Mean of a 3D array:{np.mean(arr,axis=(1,0))}")
print(f"Standard Deviation of a 3D array:{np.std(arr,axis=(1,0))}")

# ## Challenge 2
# #### Implement z-score normalization instead of min-max.
#1D array
data = np.array([10, 20, 30, 40, 50])
z_score = (data - np.mean(data)) / np.std(data)
print("Z-score Normalized Data:")
print(z_score)
#2D array
data = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400]])
z_score = (data - np.mean(data, axis=0)) / np.std(data, axis=0)
print("Z-score Normalized Data:")
print(z_score)
z_score = (data - np.mean(data)) / np.std(data)
z_score
#3D array
z_score = (arr - np.mean(arr, axis=(0,1))) / np.std(arr, axis=(0,1))
print(z_score)
print("Mean:", np.mean(z_score, axis=(0,1)))
print("Std :", np.std(z_score, axis=(0,1)))

# ## Challenge 3
# #### Detect and analyze seasonal patterns in quarterly data.
quarterly_data = np.array([
    [120, 150, 200, 170],   # Year 1
    [130, 160, 210, 180],   # Year 2
    [125, 155, 205, 175],   # Year 3
    [135, 165, 215, 185]    # Year 4
])
quarterly_data 
# Calculate average revenue per quarter
quarterly_mean = np.mean(quarterly_data, axis=0)
quarters=['Quarter_1','Quarter_2','Quarter_3','Quarter_4']   #  Quarter with highest average → peak season
for q, val in zip(quarters, quarterly_mean):                 #  Quarter with lowest average → weak season
    print(f"{q} Average Revenue: {val}")                 
# Seasonal Index Calculation
overall_mean = np.mean(quarterly_data)
seasonal_index = quarterly_mean / overall_mean               # Index > 1 → above-average quarter
for q, idx in zip(quarters, seasonal_index):                 # Index < 1 → below-average quarter
    print(f"{q} Seasonal Index: {idx:.2f}")             
# Standard Deviation
quarterly_std = np.std(quarterly_data,axis=0)
for q, sd in zip(quarters, quarterly_std):                   # Low std → consistent seasonal behaviour
    print(f"{q} Std Dev: {sd:.2f}")                          # High std → unstable seasonality
# Detect seasonal variation using standard deviation per region
seasonal_variation = revenue_matrix.std(axis=1)
for i in range(len(seasonal_variation)):
    region_name = df.loc[i, 'RegionName']
    variation = seasonal_variation[i]
print(f"{region_name}: ${variation:,.2f}")
max_var_idx = seasonal_variation.argmax()
print(f"\nRegion with the highest seasonal variation: {df.loc[max_var_idx, 'RegionName']}")
# Detect seasonal variation using standard deviation per region
seasonal_variation = revenue_matrix.std(axis=1)
print("Seasonal Variation (Standard Deviation) per Region:")
for i in range(len(seasonal_variation)):
    region_name = df.loc[i, 'RegionName']
    variation = seasonal_variation[i]
print(f"{region_name}: ${variation:,.2f}")
max_var_idx = seasonal_variation.argmax()
print(f"\nRegion with the highest seasonal variation: {df.loc[max_var_idx, 'RegionName']}")