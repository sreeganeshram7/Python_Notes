# Generated from: GaneshAssignment-1.ipynb
# Converted at: 2025-12-20T08:48:33.598Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# ## Q1.1: Load and Inspect
# #### Load the sales dataset and display its shape, column names, and first 5 rows.

import pandas as pd
df=pd.read_csv("assignment1_sales_data.csv")
df
print("Shape:",df.shape)
print("ColNames:",df.columns.tolist())
df.describe()
df.head()

# ## Q1.2: Regional Analysis
# #### Count the total number of products in each region and display the results.
df.groupby('Region').agg({'ProductID':'count'})
total=df.groupby('Region').size().reset_index()
print("Total number of Products per each Region:",total)

# ## Q1.3: Filter and Export High Sales
# #### Filter all products where TotalSales > 2000 and save to a new CSV file named high_sales_products.csv

high_sales=df[df['TotalSales']>2000]
high_sales
high_sales.to_csv('high_sales_products.csv',index=False)
high_sales.count().reset_index()

# ## Q1.4: CSV Module Reading
# #### Read the CSV file using the csv module (standard library) and print all product names.
import csv
with open('assignment1_sales_data.csv','r')as f:
    reader = csv.DictReader(f)
    print("Product Names:")
    for row in reader:
        print(f"{row['ProductName']}")

# ## Q1.5: Find Best Performer
# #### Find the product with the highest TotalSales and display its complete details.
Best=df['TotalSales'].idxmax()
df.loc[Best].reset_index()

# ## Q1.6: Category Filtering
# #### Create a CSV file containing only Electronics products with their quarterly sales (Q1-Q4).
Electronics=df[df['Category']=='Electronics']
Electronics_cols=['ProductName','Category','Region','Q1Sales','Q2Sales','Q3Sales','Q4Sales','UnitPrice']
Electronics[Electronics_cols].to_csv('Electronics quarterly sales.csv',index=False)
Electronics.count().reset_index()

# ## Q1.7: Summary Statistics
# #### Calculate the average UnitPrice per region and write results to avg_price_by_region.csv
avg_price=df.groupby('Region')['UnitPrice'].mean()
avg_price.reset_index()
avg_price.to_csv('avg_price_by_region.csv',index=False)

# ## Q1.8: Data Quality Check
# #### Identify missing values in the dataset (if any) and handle them appropriately.
df.isnull().sum().reset_index()

# ## Q1.9: Sorting and Export
# #### Sort the dataset by TotalSales in descending order and save as sorted_sales.csv
sort_sales=df.sort_values(by='TotalSales',ascending=False)
sort_sales
sort_sales.to_csv('sorted_sales.csv',index=False)

# ## Q1.10: Data Merging
# #### Merge this dataset with a region-level summary and export as merged_analysis.csv
region_summary=df.groupby('Region').agg({'TotalSales':'sum','UnitPrice':'mean'})
region_summary.rename(columns={'TotalSales':'RegionTotalSales','UnitPrice':'RegionUnitPrice'}).reset_index()
merged=df.merge(region_summary,on='Region',how='left')
merged
merged.to_csv('merged_analysis.csv',index=False)

# ## Challenge Extension
# ### Challenge 1:
# #### Create a report showing top 5 products per region and export as a single CSV.
sort=df.sort_values(['Region','TotalSales'],ascending=[True,False])
sort
top_5=sort.groupby('Region').head(5)
top_5
top_5.to_csv('top_5_products per Region.csv',index=False)

# ## Challenge 2
# #### Calculate quarterly growth rate for each product and identify fastest-growing products
df['Growth_Q2']=(df['Q2Sales']-df['Q1Sales'])/df['Q1Sales']*100
df['Growth_Q3']=(df['Q3Sales']-df['Q2Sales'])/df['Q2Sales']*100
df['Growth_Q4']=(df['Q4Sales']-df['Q3Sales'])/df['Q3Sales']*100
df['Avg_Growth']=df[['Growth_Q2','Growth_Q3','Growth_Q4']].mean(axis=1)
df
Fastest=df.sort_values(by='Avg_Growth',ascending=False)
Fastest

# ## Challenge 3:
# #### Detect and handle duplicate rows intelligently.
df[df.duplicated()].sum().reset_index()