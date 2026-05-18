# Generated from: GaneshAssignment-7.ipynb
# Converted at: 2025-12-20T09:35:53.093Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# ## ASSIGNMENT 7: E-commerce Orders Analysis
import pandas as pd 
df=pd.read_csv('assignment7_ecommerce_orders(in).csv')
df
df.head()
df.describe()

# ## Q7.1: Data Loading and Verification
# #### Load the e-commerce orders data and calculate the total order amount.
total=df['TotalAmount'].sum()
total
print("E-commerce Orders Dataset:")
print(df.head(10))
print(f"\nTotal Orders: {len(df)}")
print(f"Total Amount: ${total:,.2f}")

# ## Q7.2: Order Status Analysis
# #### Filter completed orders and calculate average order value by payment method.
Filter=df[df['OrderStatus']=='Completed']
Filter
print(f"Completed Orders:{len(Filter)}")
avg_order=df.groupby('PaymentMethod')['TotalAmount'].agg(['mean','count']).reset_index()
print("Average Order Value by Payment Method:")
print(avg_order)

# ## Q7.3: Category Summary
# #### Create a summary showing order count and total revenue by product category
Category=df.groupby('ProductCategory').agg({'OrderID':'count',
                            'TotalAmount':'sum'}).rename(columns={'OrderID':'OrderCount','TotalAmount':'TotalRevenue'})
print('Category Summary:')
print(Category)

# ## Q7.4: Payment Method Analysis
# #### Identify the most common payment method and calculate its usage percentage
payment_count=df['PaymentMethod'].value_counts()
most_common_method=payment_count.idxmax()
most_common_count=payment_count.max()
percentage=(most_common_count/len(df))*100
print(f"Most Common Payment Method: {most_common_method} ({percentage:.1f}%)")
print("All Payment Methods:")
print(payment_count.reset_index())

# ## Q7.5: Discount Analysis
# #### Group orders by status and calculate average discount applied per status.
Discount=df.groupby('OrderStatus')['DiscountApplied'].agg(['mean','count','sum'])
print("Average Discount Summary by Status:")
print(Discount)

# ## Q7.6: Pivot Analysis
# #### Create a pivot table with OrderStatus as rows and PaymentMethod as columns (count of orders)
pivot=pd.pivot_table(data=df,index='OrderStatus',columns='PaymentMethod',values='OrderID',aggfunc='count')
print("Order Count for Status and PaymentMethod:")
pivot
pivot=pd.crosstab(df['OrderStatus'],df['PaymentMethod'])
print("Order Count for Status and PaymentMethod:")
pivot

# ## Q7.7: Order Export
# #### Export all completed orders to completed_orders.csv with relevant columns.
Filter.to_csv('completed_orders.csv',index=False)

# ## Q7.8: Top Dates
# #### Find the top 5 dates by total revenue.
top_dates=df.groupby('OrderDate')['TotalAmount'].sum().nlargest(5).reset_index()
print("Top_5 Dates by Total Revenue:")
print(top_dates)

# ## Q7.9: Discount by Category
# #### Calculate the average discount percentage by product category
Discount=df.groupby('ProductCategory')['DiscountApplied'].mean().reset_index()
print("Average Discount by Product Category:")
print(Discount)

# ## Q7.10: Visualizations
# #### Create visualizations comparing order status and payment method distributions.
import matplotlib.pyplot as plt
import seaborn as sns 
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
sns.countplot(data=df,x='OrderStatus',ax=ax1)
ax1.set_title('OrderStatus Distribution')
ax1.set_ylabel('Number of Orders')
sns.countplot(data=df,x='PaymentMethod',ax=ax2,color='orange')
ax2.set_title('PaymentMethod Distribution')
ax2.set_ylabel('Number of Orders')