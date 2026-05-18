# Generated from: GaneshAssignment-4.ipynb
# Converted at: 2025-12-20T09:25:19.066Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# ## ASSIGNMENT 4: Data Summarization & Grouping
# ## Q4.1: Basic GroupBy
import pandas as pd 
df=pd.read_csv('assignment4_sales_transactions(in).csv')
df

# #### Group sales data by Region and calculate total revenue per region.
total_revenue=df.groupby('Region')['Revenue'].sum()
print("Total Revenue by Region:")
print(total_revenue.reset_index())

# ## Q4.2: Multi-column GroupBy
# #### Group by both Region and Category, showing transaction count and total revenue for each combination.
region_category=df.groupby(['Region','Category']).agg({"TransactionID":"count","Revenue":"sum"})
region_category=region_category.rename(columns={'TransactionID': 'TransactionCount'})
print("Region Category by Transaction count and total Revenue:")
print(region_category.reset_index())

# ## Q4.3: Average Quantity Analysis
# #### Calculate the average quantity sold per region and sort in descending order.
avg_quantity=df.groupby('Region')['Quantity'].mean().sort_values(ascending=False)
print("Average Quantity per Region:")
print(avg_quantity.reset_index())

# ## Q4.4: Pivot Table Creation
# #### Create a pivot table with Region as rows, Category as columns, and sum of Revenue as values.
pivot = pd.pivot_table(df, values='Revenue', index='Region', columns='Category', aggfunc='sum')
print("Pivot Table: Region x Category Revenue:")
print(pivot)

# ## Q4.5: Calculated Columns
# #### Add a calculated column 'RevenuePerUnit' (Revenue / Quantity) for each transaction
df['RevenuePerUnit']=df['Revenue']/df['Quantity']
print("RevenuePerUnit for each Transaction")
print(df[['TransactionID','Revenue','Quantity','RevenuePerUnit']])

# ## Q4.6 Top Products
# #### Find the top 3 products by total revenue and display their sales details
top_3_products=df.groupby('ProductName')['Revenue'].sum().nlargest(3)
print("Top 3 products for Total Revenue:")
top_3_products.reset_index()
print(f"Sales Details:")
for product in top_3_products.index:
    product_data = df[df['ProductName'] == product]
    print(f"\n{product}:")
    print(f"  Total Revenue: ${product_data['Revenue'].sum():,.0f}")
    print(f"  Transaction Count: {len(product_data)}")
    print(f"  Average Order Value: ${product_data['Revenue'].mean():,.0f}")

# ## Q4.7: Customer Type Analysis
# #### Group by CustomerType and calculate total revenue, transaction count, and average order value
customer_summary = df.groupby('CustomerType').agg({
'Revenue': ['sum', 'count', 'mean'],
'Quantity': 'sum'
})
print("Performance by Customer Type:")
print(customer_summary.reset_index())

# ## Q4.8: Composite Analysis
# #### Identify which region-category combination has the highest average revenue per transaction
region_category = df.groupby(['Region', 'Category'])['Revenue'].mean()
region_category.reset_index()
highest_combination = region_category.idxmax()
highest_combination
highest_avg = region_category.max()
highest_avg
print(f"Best Region-Category Combination: {highest_combination}")
print(f"Average Revenue per Transaction: ${highest_avg:,.0f}")

# ## Q4.9: Summary Report Export
# #### Create a summary CSV showing region-wise performance metrics
region_summary=df.groupby('Region').agg({'Revenue':['sum','count','mean'],'Quantity':['sum','mean'],'TransactionID':'count'}).round(2)
region_summary.to_csv('region_summary_report.csv',index=False)
print("Region Summary Report metrics:")
region_summary.reset_index()

# ## Q4.10: Quarterly Summary
# #### Generate a quarterly revenue summary grouped by region (requires Date extraction)
df['Date'] = pd.to_datetime(df['Date'])
df['Quarter'] = df['Date'].dt.quarter
df['Month'] = df['Date'].dt.month
quarterly_summary = df.groupby(['Region', 'Quarter'])['Revenue'].sum()
print("Quarterly Revenue by Region:")
print(quarterly_summary.reset_index())
quarterly_summary.to_csv('quarterly_revenue_by_region.csv',index=False)

# ## Challenge Extension
# ### Challenge 1: 
# #### Create a rolling 7-day revenue analysis.
df['Date'] = pd.to_datetime(df['Date'])
df['Date']
df = df.sort_values('Date')
df.tail(7)
df['Revenue_7Day_Rolling'] = df['Revenue'].rolling(window=7).mean().round(2)
df['Revenue_7Day_Rolling'].reset_index().tail(7)
print(df[['Date', 'Revenue', 'Revenue_7Day_Rolling']].tail(7))

# ### Challenge 2: 
# #### Calculate month-over-month growth rates by region.
df['Month']=df['Date'].dt.month
df['Month'].reset_index().head(20)
monthly_revenue=df.groupby(['Region','Month'])['Revenue'].sum().reset_index()
monthly_revenue
monthly_revenue['MoM_growth_%']=monthly_revenue.groupby('Region')['Revenue'].pct_change()*100
monthly_revenue['MoM_growth_%'].head(10).reset_index()

# ### Challenge 3: 
# #### Generate a comprehensive business intelligence report with multiple views
# Revenue by Region
region_summary = df.groupby('Region').agg(TotalRevenue=('Revenue', 'sum'),
    AvgRevenue=('Revenue', 'mean'),TransactionCount=('Revenue', 'count')).round(2).reset_index()
print("Region_Summary:")
region_summary
# monthly revenue by trend
monthly_summary = (df.groupby('Month')['Revenue'].sum().reset_index())
print("Monthly_Summary:")
monthly_summary
# Region-Month Pivot Table
region_month_pivot = pd.pivot_table(df,values='Revenue',index='Region',columns='Month',aggfunc='sum',)
print("Region_Month_Pivot_Table:")
region_month_pivot
# Top performing Regions
top_regions = region_summary.sort_values(by='TotalRevenue',ascending=False)
print("Top_Performing_Regions:")
top_regions
with pd.ExcelWriter('business_intelligence_report.xlsx') as writer:
    region_summary.to_excel(writer, sheet_name='Region_Summary', index=False)
    monthly_summary.to_excel(writer, sheet_name='Monthly_Summary', index=False)
    region_month_pivot.to_excel(writer, sheet_name='Region_Month_Pivot_Table',index=False)