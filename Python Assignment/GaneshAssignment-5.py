# Generated from: GaneshAssignment-5.ipynb
# Converted at: 2025-12-20T09:26:24.440Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# ## ASSIGNMENT 5: Matplotlib Visualization
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("assignment5_monthly_trends(in).csv")
df

# ## Q5.1: Line Plot - Monthly Revenue
# #### Create a line plot showing total monthly revenue for 2024 with proper labels and grid
df['Month']=pd.to_datetime(df['Month'])
plt.figure(figsize=(10,6))
plt.plot(df['Month'],df['TotalRevenue'],marker='o',linewidth=2,color='blue')
plt.xlabel('Month',fontsize=12)
plt.ylabel('TotalRevenue $',fontsize=12)
plt.title('Total Monthly Revenue-2024',fontsize=12,fontweight='bold')
plt.grid(True,alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ## Q5.2: Grouped Bar Chart 
# #### Create a bar chart comparing ProductA, ProductB, and ProductC revenues across all months
plt.figure(figsize=(10,6))
x=range(len(df)) # It is used to find out the length of the data
width=0.25
plt.bar([i - width for i in x],df['ProductA_Revenue'],width,label='Product A',color='red')
plt.bar([i for i in x],df['ProductB_Revenue'],width,label='Product B',color='blue')
plt.bar([i + width for i in x],df['ProductC_Revenue'],width,label='Product C',color='green')
plt.xlabel('Month',fontsize=12)
plt.ylabel('Revenue',fontsize=12)             # strftime - It is used convert the list into the string formatted time
plt.title('Product Revenue Comparison',fontsize=12,fontweight='bold')
plt.xticks(x, [d.strftime('%b') for d in df['Month']])                 
plt.legend()                                         # %b - It is used to figure x-axis in the letters like Jan,Feb,..
plt.tight_layout()                             # %B - It is used to figure x-axis in the letters like January,Feburary,..
plt.show()                                                # %m - It is used to figure x-axis in the letters like 01,02,..

# ## Q5.3: Subplots for Products
# #### Plot ProductA and ProductB on the same figure using subplots (2 separate plots)
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(14,5))
ax1.plot(df['Month'],df['ProductA_Revenue'],marker='o',linewidth=2)
ax1.set_title('ProductA Monthly Revenue',fontsize=12,fontweight='bold')
ax1.set_xlabel('Month')
ax1.set_ylabel('Revenue $')
ax1.grid(True,alpha=0.3)

ax2.plot(df['Month'],df['ProductB_Revenue'],marker='s',linewidth=2,color='red')
ax2.set_title('ProductB Monthly Revenue',fontsize=12,fontweight='bold')
ax2.set_xlabel('Month')
ax2.set_ylabel('Revenue $')
ax2.grid(True,alpha=0.3)

plt.tight_layout()
plt.show()

# ## Q5.4: Multi-line Plot with Legend
# #### Create a line plot with markers showing all three products and a legend
plt.figure(figsize=(10,6))
plt.plot(df['Month'],df['ProductA_Revenue'],marker='o',linewidth=2,linestyle='-',label='Product A')
plt.plot(df['Month'],df['ProductB_Revenue'],marker='s',linewidth=2,linestyle='--',label='Product B')
plt.plot(df['Month'],df['ProductC_Revenue'],marker='^',linewidth=2,linestyle='-.',label='Product C')
plt.xlabel('Month',fontsize=12)
plt.ylabel('TotalRevenue $',fontsize=12)
plt.title('Total Monthly Revenue-2024',fontsize=12,fontweight='bold')
plt.grid(True,alpha=0.3)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# ## Q5.5: Customized Bar Chart
# #### Customize a bar chart with different colors for each month and a bold title
colors=plt.cm.plasma(range(len(df)))
plt.figure(figsize=(10,6))
bars=plt.bar(range(len(df)),df['TotalRevenue'],color=colors,edgecolor='black',linewidth=2)
plt.title('Total Monthly Revenue 2024', fontsize=14, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.xticks(range(len(df)), [d.strftime('%B') for d in df['Month']], rotation=45)
for bar in bars:
    height=bar.get_height()
    plt.text(bar.get_x()+bar.get_width()/2,height,f'${height:,.0f}',va='bottom',ha='center',fontsize=12)
plt.tight_layout()
plt.show()

# ## Q5.6: Complex Subplot Layout
# #### Create a figure with multiple subplots: line plot, bar chart, and scatter plot.
fig,axes=plt.subplots(2,2,figsize=(14,10))
# Line Plot
axes[0, 0].plot(df['Month'],df['ProductA_Revenue'],marker='o')
axes[0, 0].set_title('Line Plot for Total Revenue in Months')
axes[0, 0].set_xlabel('Month')
axes[0, 0].set_ylabel('Revenue $',fontsize=12)
axes[0, 0].grid(True,alpha=0.3)
# Bar Chart
axes[0, 1].bar(range(len(df)), df['TotalRevenue'], color='coral')
axes[0, 1].set_title('Bar Chart for Product A in Months')
axes[0, 1].set_xlabel('Month')
axes[0, 1].set_ylabel('Revenue ($)',fontsize=12)
# Scatter Plot
axes[1, 0].scatter(range(len(df)), df['AvgOrderValue'], s=100, color='green', alpha=0.6)
axes[1, 0].set_title('Scatter plot for Avg Order Value in Months')
axes[1, 0].set_xlabel('Month')
axes[1, 0].set_ylabel('Revenue ($)')
axes[1, 0].set_xlabel('Month')
# Line Plot
axes[1, 1].plot(df['Month'],df['ProductC_Revenue'],marker='o')
axes[1, 1].set_title('Line Plot for Product C in Months')
axes[1, 1].set_xlabel('Month')
axes[1, 1].set_ylabel('Revenue $',fontsize=12)
axes[1, 1].grid(True,alpha=0.3)

plt.tight_layout()
plt.show()

# ## Q5.7: Annotations
# #### Add annotations to show the highest revenue month on a line plot
plt.figure(figsize=(10,6))
plt.plot(df['Month'],df['TotalRevenue'],marker='o',linewidth=2,color='blue')
max_idx=df['TotalRevenue'].idxmax()
max_month=df.loc[max_idx,'Month']
max_revenue=df.loc[max_idx,'TotalRevenue']
plt.annotate(f"Highest: ${max_revenue:,.0f}", 
                                        xy=(max_month, max_revenue),
                                        xytext=(10, 10), textcoords='offset points',
                                        bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
                                        arrowprops=dict(arrowstyle='->', color='red', lw=2))
plt.xlabel('Month',fontsize=12)
plt.ylabel('TotalRevenue $',fontsize=12)
plt.title('Monthly Revenue with peak annotation',fontsize=12,fontweight='bold')
plt.grid(True,alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ## Q5.8: Stacked Bar Chart
# #### Create a stacked bar chart showing the contribution of each product per month
plt.figure(figsize=(12,6))
bottom_a = df['ProductA_Revenue']
bottom_ab = df['ProductA_Revenue'] + df['ProductB_Revenue']
plt.bar(range(len(df)), df['ProductA_Revenue'],label='Product A', color='skyblue')
plt.bar(range(len(df)), df['ProductB_Revenue'],bottom=bottom_a, label='Product B', color='orange')
plt.bar(range(len(df)), df['ProductC_Revenue'],bottom=bottom_ab, label='Product C', color='green')
plt.xticks(range(len(df)), df['Month'], rotation=45)
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.title('Monthly Product Revenue Contribution')
plt.legend()
plt.tight_layout()
plt.show()

# ## Q5.9: Save Chart as Image
# #### Save a visualization as 'monthly_analysis.png' with 300 DPI.
plt.figure(figsize=(10,6))
plt.plot(df['Month'],df['TotalRevenue'],marker='o',linewidth=2,color='blue')
plt.xlabel('Month',fontsize=12)
plt.ylabel('Revenue $',fontsize=12)
plt.title('Monthly Revenue Analysis 2024',fontsize=12,fontweight='bold')
plt.grid(True,alpha=0.3)
plt.xticks(rotation=45)
plt.savefig('monthly_analysis.png',dpi=300)
print("Chart saved as 'monthly_analysis.png' (DPI: 300)")
plt.show()

# ## Q5.10: Dual-Axis Plot
# #### Create a dual-axis plot: line for TotalRevenue and bars for AvgOrderValue
fig, ax1 = plt.subplots(figsize=(12, 6))
# Primary axis: Line plot for TotalRevenue
ax1.plot(df['Month'], df['TotalRevenue'], marker='o', color='blue', linewidth=2.5, label='Revenue')
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Total Revenue ($)', color='blue', fontsize=12)
ax1.tick_params(axis='y', labelcolor='blue')
# Secondary axis: Bar chart for AvgOrderValue
ax2 = ax1.twinx()
ax2.bar(df['Month'], df['AvgOrderValue'], alpha=0.3, color='green', label='Avg Order Value')
ax2.set_ylabel('Avg Order Value ($)', color='green', fontsize=12)
ax2.tick_params(axis='y', labelcolor='green')
plt.title('Dual-Axis for  Revenue and Order Value', fontsize=14, fontweight='bold')
fig.legend(loc='upper left',bbox_to_anchor=(1.05,1))
plt.tight_layout()
plt.show()

# ## Challenge Extension
# #### Challenge 1: Create a dashboard-style figure with 4 different visualizations.
fig,axes=plt.subplots(2,2,figsize=(14,10))
# Line Plot
axes[0, 0].plot(df['Month'],df['ProductB_Revenue'],marker='o')
axes[0, 0].set_title('Line Plot for Product B Revenue in Months')
axes[0, 0].set_xlabel('Month')
axes[0, 0].set_ylabel('Revenue $',fontsize=12)
axes[0, 0].grid(True,alpha=0.3)
# Bar Chart
axes[0, 1].bar(range(len(df)), df['ProductA_Revenue'], color='coral')
axes[0, 1].set_title('Bar Chart for Product A in Months')
axes[0, 1].set_xlabel('Month')
axes[0, 1].set_ylabel('Revenue ($)',fontsize=12)
# Scatter Plot
axes[1, 0].scatter(range(len(df)), df['ProductC_Revenue'], s=100, color='green', alpha=0.6)
axes[1, 0].set_title('Scatter plot for Product C in Months')
axes[1, 0].set_xlabel('Month')
axes[1, 0].set_ylabel('Revenue ($)')
# HistPlot
axes[1, 1].hist(df['ProductC_Revenue'], bins=10, alpha=0.7)
axes[1, 1].set_title('Histogram of Product Analysis')
axes[1, 1].set_xlabel('Revenue ($)')
axes[1, 1].set_ylabel('Frequency')
plt.tight_layout()
plt.show()


# #### Challenge 2: Animate a chart showing progressive revenue growth.
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
HTML(ani.to_jshtml())
fig, ax = plt.subplots()
ax.set_xlim(0, len(df['Month']))
ax.set_ylim(0, df['TotalRevenue'].max() + 5000)
line, = ax.plot([], [], marker='o')
def update(frame):
    x = range(frame)                     
    y = df['TotalRevenue'][:frame]     
    line.set_data(x, y)
    return line,
ani = FuncAnimation(fig,update,frames=len(df) + 1,interval=500)
ax.set_xlabel('Month Index')
ax.set_ylabel('Total Revenue')
ax.set_title('Animated Revenue Growth')

plt.show()
ani

# #### Challenge 3: Create histograms with overlapping transparency.
plt.figure(figsize=(12,6))
plt.hist(df['ProductA_Revenue'], bins=10, alpha=0.3, label='Product A')
plt.hist(df['ProductB_Revenue'], bins=10, alpha=0.3, label='Product B')
plt.hist(df['ProductC_Revenue'], bins=10, alpha=0.3, label='Product C')
plt.xlabel('Revenue')
plt.ylabel('Frequency')
plt.title('Overlapping Revenue Distribution')
plt.legend()
plt.tight_layout()
plt.show()