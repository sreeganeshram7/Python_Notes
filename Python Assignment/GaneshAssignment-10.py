# Generated from: GaneshAssignment-10.ipynb
# Converted at: 2025-12-20T10:26:32.773Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# ## ASSIGNMENT 10: Product Performance Analysis
# ## Q10.1: Profit Calculation
# #### Load product data and calculate profit per product (SellingPrice - ManufacturingCost) × UnitsSold
import pandas as pd
df=pd.read_csv('assignment10_product_performance(in).csv')
df
df['Profit']=(df['SellingPrice']-df['ManufacturingCost'])*df['UnitsSold']
print("Profit Analysis:")
print(df[['ProductName','UnitsSold','ManufacturingCost','SellingPrice','Profit']].head())
print(f"\n Profit Calculation: ${df['Profit'].sum():,.2f}")

# ## Q10.2: Category Filtering
# #### Filter products by category and analyze sales performance (UnitsSold vs UnitsProduced).
Filter=df[df['Category']=='Budget']
performance=Filter[['Category','UnitsSold','UnitsProduced','Profit']]
performance.head()
performance = Filter.groupby('Category').agg(UnitsProduced=('UnitsProduced', 'sum'),UnitsSold=('UnitsSold', 'sum')).reset_index()
print("Sales_Performance:")
performance
comparison=(Filter['UnitsSold']>=Filter['UnitsProduced'])
comparison.head()
sales=((Filter['UnitsSold']/Filter['UnitsProduced'])*100).round(2).reset_index().head()
print("Sales Performance:")
sales

# ## Q10.3: Profitability by Category
# #### Group by category and calculate total profit, average profit, and profit margin
df['Revenue']=df['SellingPrice']*df['UnitsSold']
df.head()
category = df.groupby('Category').agg({'Profit': ['sum', 'mean'],'UnitsSold': 'sum','SellingPrice': 'mean'}).round(2)
category

category = (df.groupby('Category').agg(TotalProfit=('Profit', 'sum'),AverageProfit=('Profit', 'mean'),
           TotalUnitsSold=('UnitsSold', 'sum'),TotalRevenue=('Revenue', 'sum')).round(2))
category

category['ProfitMargin']=(category['TotalProfit'] / category['TotalRevenue']) * 100
category['ProfitMargin'].reset_index()

# ## Q10.4: Top 10 Products
# #### Identify top 10 products by profit and create bar chart visualization
top_10=df.nlargest(10,'Profit')
top_10

import matplotlib.pyplot as plt
plt.figure(figsize=(18, 7))
colors = ['lightblue', 'blue', 'purple', 'red', 'yellow', 'orange', 'lightgreen', 'green', 'black', 'pink']
plt.barh(range(len(top_10)), top_10['Profit'], color=colors)
plt.yticks(range(len(top_10)), top_10['ProductName'], fontsize=10)
plt.xlabel('Profit ($)', fontsize=12)
plt.title('Top 10 Products by Profit', fontsize=14, fontweight='bold')
for i, v in enumerate(top_10['Profit']):
    plt.text(v, i, f' ${v:,.0f}', va='center', fontsize=9)
plt.tight_layout()
plt.show()

# ## Q10.5: Relationship Analysis
# #### Analyze correlation between CustomerSatisfaction and ReturnRate using correlation
correlation=df[['CustomerSatisfaction','ReturnRate']]
correlation.corr()

plt.figure(figsize=(10, 6))
plt.scatter(df['CustomerSatisfaction'], df['ReturnRate'], alpha=0.6, s=100)
plt.xlabel('Customer Satisfaction')
plt.ylabel('Return Rate (%)')
plt.title(f"Satisfaction vs Return Rate ")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ## Q10.6: Pivot Analysis
# #### Create pivot table showing average profit by category and market share brackets
df['MarketShareBracket']=pd.cut(df['MarketShare'],bins=3,labels=['Low','Medium','High'])
pivot_profit= pd.pivot_table(df,values='Profit',index='Category',columns='MarketShareBracket',aggfunc='mean',observed=True).round(2)
pivot_profit

# ## Q10.7: Performance Metrics
# #### Add calculated columns: ProfitMargin%, Sellthrough% (UnitsSold/UnitsProduced)
df['ProfitMargin%']=(df['Profit']/df['Revenue'])*100
df['Sellthrough%']=(df['UnitsSold']/df['UnitsProduced'])*100
df.head()

# ## Q10.8: Ranking Report
# #### Export a summary report with product rankings by profitability and performance
ranking_report = (df.sort_values(by='Profit', ascending=False)
      [['ProductName', 'Category', 'Profit', 'ProfitMargin%', 'Sellthrough%', 'CustomerSatisfaction']])
ranking_report.to_csv('product_ranking_report.csv', index=False)

# ## Q10.9: Multi-visualization Dashboard
# #### Create 4 different visualizations: profit by category, satisfaction vs returns, market share, pie chart
fig,axes=plt.subplots(2,2,figsize=(10,6))
colors = ['lightblue', 'blue', 'purple']
# Profit by Category
category=df.groupby('Category')['Profit'].sum()
axes[0,0].bar(category.index,category.values,color=colors)
axes[0,0].set_title('Total Profit by Category')
axes[0,0].set_ylabel('Profit')
# Satisfaction vs Returns
axes[0,1].scatter(df['CustomerSatisfaction'],df['ReturnRate'],s=50,alpha=0.3)
axes[0,1].set_title('Satisfaction vs Returns')
axes[0,1].set_xlabel('CustomerSatisfaction')
axes[0,1].set_ylabel('ReturnRate') 
axes[0,1].grid(True,alpha=0.3)
# Market share
axes[1, 0].hist(df['MarketShare'], bins=15, color='steelblue', alpha=0.7)
axes[1, 0].set_title('Market Share Distribution')
axes[1, 0].set_ylabel('Market Share (%)')
axes[1, 0].set_xlabel('Category')
#pie chart
axes[1,1].pie(category,labels=category.index,autopct='%1.1f%%')
axes[1, 1].set_title('Profit Distribution by Category')

plt.tight_layout()
plt.show()

# ## Q10.10: Executive Summary
# #### Generate comprehensive insights: best/worst products, opportunities, and recommendations.
print("=== EXECUTIVE SUMMARY: PRODUCT PERFORMANCE ANALYSIS ===\n")

best_product = df.loc[df['Profit'].idxmax()]
worst_product = df.loc[df['Profit'].idxmin()]
print("KEY FINDINGS:")
print(f"\n1.Best Performing Product: {best_product['ProductName']}")
print(f"Profit: ${best_product['Profit']:,.2f}")
print(f"Margin: {best_product['ProfitMargin%']:.1f}%")
print(f"Satisfaction:{best_product['CustomerSatisfaction']}/5.0")
print(f"\n2.Worst Performing Product: {worst_product['ProductName']}")
print(f"Profit:${worst_product['Profit']:,.2f}")
print(f"Margin:{worst_product['ProfitMargin%']:.1f}%")
print("\n3.Category Performance:")
for cat in df['Category'].unique():
    category=df[df['Category'] == cat]
    print(
        f"{cat}: ${category['Profit'].sum():,.0f} total profit "
        f"({len(cat_data)} products)"
    )
high_returns = df[df['ReturnRate'] > df['ReturnRate'].quantile(0.75)]
print(f"\n4.High Return Products ({len(high_returns)} products):")
print(f"Average Return Rate: {high_returns['ReturnRate'].mean():.2f}%")
print("Recommendation: Review quality/customer-product fit")
print("\n5.OVERALL METRICS:")
print(f"Total Profit: ${df['Profit'].sum():,.2f}")
print(f"Average Satisfaction: {df['CustomerSatisfaction'].mean():.2f}/5.0")
print(f"Avg Sellthrough: {df['Sellthrough%'].mean():.1f}%")
