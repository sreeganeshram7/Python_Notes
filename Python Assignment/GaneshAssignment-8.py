# Generated from: GaneshAssignment-8.ipynb
# Converted at: 2025-12-20T09:36:35.964Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# ## ASSIGNMENT 8: HR Employee Analytics
# ## Q8.1: Department Headcount
# #### Load HR data and display department-wise employee count.
import pandas as pd
df=pd.read_csv('assignment8_hr_employee_data(in).csv')
df
df.head()
df.describe()
employee_count=df['Department'].value_counts().reset_index()
print("Department-Wise Employee Count:")
employee_count

# ## Q8.2: Salary Analysis
# #### Calculate average salary by department and designation.
avg_salary=df.groupby(['Department','Designation'])['Salary'].mean().round(2)
print("Average Salary by Department and Designation:")
avg_salary.reset_index()

# ## Q8.3: Location Analysis
# #### Group employees by location and calculate total and average salary
location=df.groupby('Location')['Salary'].agg(['sum','mean']).round(2)
print("Salary Analysis by Location:")
print(location)

# ## Q8.4: Pivot Table
# #### Create a pivot table showing department vs designation with salary totals
pivot=pd.pivot_table(df,index='Department',
                     columns='Designation',values='Salary',
                     aggfunc='sum')
print("Pivot Table for Department vs Desigination with Salary:")
print(pivot)

# ## Q8.5: Service Years
# #### Add a calculated column for service years (current year - JoiningYear).
df['ServiceYear']=2024-df['JoiningYear']
print("Service Year for Employees:")
print(df[['EmployeeID','EmployeeName','JoiningYear','ServiceYear']])

# ## Q8.6: Top Earners
# #### Find top 10 employees by salary and display their details.
top_earners=df.nlargest(10,'Salary')
print("Top Salary for 10 Employees:")
print(top_earners[['EmployeeID','EmployeeName','Department','Salary']])

# ## Q8.7: Performance Analysis
# #### Identify underperformers (PerformanceRating < 3.0) by department
Filter=df[df['PerformanceRating']<3.0]
underperformers=Filter.groupby('Department')
print("UnderPerformance by Department:")
print(Filter)
print(f"Total UnderPerformers:{len(Filter)}")

# ## Q8.8: Projects Analysis
# #### Create a summary showing projects completed by department
project=df.groupby('Department')['ProjectsCompleted'].agg(['sum','mean','count']).reset_index()
print("Project Summary:")
print(project)

# ## Q8.9: Export Report
# #### Export a comprehensive HR summary to hr_summary_report.csv
hr_summary = df.groupby('Department').agg({
'Salary': ['mean', 'sum', 'min', 'max'],
'PerformanceRating': 'mean',
'ProjectsCompleted': 'sum',
'EmployeeID': 'count'
})
hr_summary.to_csv('hr_summary_report.csv',index=False)

# ## Q8.10: Visualizations
# #### Create visualizations for salary distribution and performance ratings.
import matplotlib.pyplot as plt
import seaborn as sns
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
sns.boxplot(data=df, x='Department', y='Salary', ax=ax1)
ax1.set_title('Salary Distribution by Department')
ax1.set_xlabel('Department')
ax1.set_ylabel('Salary ($)')

sns.violinplot(data=df, x='Location', y='PerformanceRating',hue='Location',palette='Set2')
ax2.set_title('Performance Rating by Location')
ax2.set_xlabel('Location')
ax2.set_ylabel('Performance Rating')
              
plt.tight_layout()
plt.show()