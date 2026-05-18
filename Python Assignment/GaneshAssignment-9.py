# Generated from: GaneshAssignment-9.ipynb
# Converted at: 2025-12-20T09:37:07.756Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# ## ASSIGNMENT 9: Stock Market Time Series
# ## Q9.1: Data Summary
# #### Load stock data and display price statistics (open, close, high, low) per stock.
import pandas as pd
df=pd.read_csv('assignment9_stock_market_data(in).csv')
df
df['Date'] = pd.to_datetime(df['Date'])
df['Date']
stock_stats=df.groupby('Stock')[['OpenPrice','HighPrice','LowPrice','ClosePrice']].describe().reset_index()
print("Stock Statistics per Stock:")
stock_stats

# ## Q9.2: Daily Change
# #### Calculate daily price change (ClosePrice - OpenPrice) and add as new column
df['DailyPrice']=df['ClosePrice']-df['OpenPrice']
print("Daily Price Change:")
df

# ## Q9.3: Stock Metrics
# #### Group by stock and calculate average volume and volatility (HighPrice - LowPrice)
df['Volatility']=df['HighPrice']-df['LowPrice']
stock=df.groupby('Stock').agg({'Volume':'mean','Volatility':'mean'}).round(2)
print("Stock Metrics:")
stock

# ## Q9.4: Single Stock Plot
# #### Filter data for one stock and plot its closing price trend over time.
stock_name=df[df['Stock']=='Wipro'].sort_values('Date')
stock_name
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.plot(stock_name['Date'],stock_name['ClosePrice'],marker='o')
plt.title('Closing Price Trend')
plt.xlabel('Date')
plt.ylabel('ClosePrice')
plt.tight_layout()
plt.show()

# ## Q9.5: Monthly Averages
# #### Calculate monthly average closing price for each stock.
df['Month']=df['Date'].dt.month
monthly_avg=df.groupby('Stock')['Month'].mean().round(2)
print('Monthly Average per stock:')
monthly_avg.reset_index()

# ## Q9.6: Best & Worst Performers
# #### Identify best (highest return) and worst (lowest return) performing stocks.
Performers=df.groupby('Stock')['DailyPrice'].mean()
best_performers=Performers.idxmax()
worst_performers=Performers.idxmin()
print(f"Best_Performers:{best_performers}")
print(f"Lowest_Performers:{worst_performers}")

# ## Q9.7: Pivot Table
# #### Create a pivot table showing average closing price by stock and month
pivot=pd.pivot_table(df,index='Stock',columns='Month',values='ClosePrice',aggfunc='mean').round(2)
print("Pivot Table:")
pivot

# ## Q9.8: Multi-Stock Plot
# #### Visualize closing prices for all stocks on same plot with legend
plt.figure(figsize=(10, 5))
stocks = ['Wipro', 'TCS', 'HCL','TechMahindra','Infosys']
linestyles = ['-', '--', '-.',':',(0,(5,10))]
markers = ['o', 's', '^','D','*']
for i, stock_name in enumerate(stocks):
    stock_data = df[df['Stock'] == stock_name].sort_values('Date')
    plt.plot(stock_data['Date'],stock_data['ClosePrice'],label=stock_name,linestyle=linestyles[i],marker=markers[i])
plt.title('Closing Price Trend of Selected Stocks')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend(title='Stock', loc='upper left', bbox_to_anchor=(1.05, 1))
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ## Q9.9: Correlation Matrix
# #### Calculate correlation between stocks' closing prices using NumPy.
price=pd.pivot_table(df,index='Date',columns='Stock',values='ClosePrice')
correlation=price.corr()
print("Correlation Matrix:")
correlation

# ## Q9.10: Comprehensive Dashboard
# #### Create a dashboard with multiple subplots showing various stock metrics.
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
colors=['r','b','g','c']
linestyles = ['-', '--', '-.',':']
markers = ['o', 's', '^','D']
stocks = df['Stock'].unique()[:4]
for i, stock in enumerate(stocks):
    ax = axes[i//2, i%2]
    stock_data = df[df['Stock'] == stock].sort_values('Date')
    ax.plot(stock_data['Date'], stock_data['ClosePrice'],linestyle=linestyles[i],marker=markers[i], color=colors[i])
    ax.set_title(f'{stock} Closing Price', fontweight='bold')
    ax.set_ylabel('Price ($)')
    ax.grid(True, alpha=0.3)
plt.suptitle('Stock Closing Price Dashboard',fontsize=14,fontweight='bold')
plt.tight_layout()
plt.show()

import seaborn as sns
fig, axs = plt.subplots(2, 2, figsize=(14,8))
sns.lineplot(data=df,x='Date',y='ClosePrice',marker='o',ax=axs[0,0],color='tab:orange')
axs[0,0].set_title('Line plot: ClosePrice vs Date',fontsize=14)
axs[0,0].set_xlabel('Date',fontsize=12)
axs[0,0].set_ylabel('Close Price',fontsize=12)
axs[0,0].grid(True, alpha=0.3)
axs[0,0].tick_params(axis='x', rotation=45)

sns.histplot(data=df,x='ClosePrice',bins=20,kde = True,ax=axs[0,1],color='tab:green')
axs[0,1].set_title('Hist plot: ClosePrice vs Date',fontsize=14)
axs[0,1].set_xlabel('Date',fontsize=12)
axs[0,1].set_ylabel('Close Price',fontsize=12)
axs[0,1].grid(True, alpha=0.3)
axs[0,1].tick_params(axis='x', rotation=45)

sns.barplot(data=df,x='Stock',y='ClosePrice',hue='Stock',ax=axs[1,0],errorbar=('ci', 95),palette='RdBu')
axs[1,0].set_title('Bar plot: ClosePrice vs Date',fontsize=14)
axs[1,0].set_xlabel('Date',fontsize=12)
axs[1,0].set_ylabel('Close Price',fontsize=12)
axs[1,0].grid(True, alpha=0.3)
axs[1,0].tick_params(axis='x', rotation=90)


sns.scatterplot(data=df,x='Date',y='ClosePrice',ax=axs[1,1],color='tab:red')
axs[1,1].set_title('Scatter Plot: Close Price vs Date',fontsize=14)
axs[1,1].set_xlabel('Date',fontsize=12)
axs[1,1].set_ylabel('Close Price',fontsize=12)
axs[1,1].grid(True, alpha=0.3)
axs[1,1].tick_params(axis='x', rotation=45)

plt.suptitle('Dashboard of multiple plot: ClosePrice VS Date',fontsize=16,fontweight='bold')
plt.tight_layout()
plt.show()