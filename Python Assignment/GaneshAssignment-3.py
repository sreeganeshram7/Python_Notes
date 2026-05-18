# Generated from: GaneshAssignment-3.ipynb
# Converted at: 2025-12-20T09:06:07.217Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# ## ASSIGNMENT 3: Introduction to Pandas
# ### Q3.1: Data Exploration
# #### Load the student scores dataset and display its shape, info, and basic statistics
import pandas as pd
df=pd.read_csv('assignment3_student_scores(in).csv')
df
shape=df.shape
print(f"Shape:{shape}")
print("\n--- Dataset Info ---")
df.info()
print("\n--- Basic Statistics ---")
df.describe()

# ## Q3.2: Average Score Calculation
# #### Calculate the average score across all subjects (Math, Science, English, History) for each student
subjects=df[['Math','Science','English','History']]
df['Avg_score']=subjects.mean(axis=1)
print("\n---Average_score for each Student---")
df['Avg_score'].head(10)
df

# ## Q3.3: Missing Value Handling
# #### Fill missing values in Math, Science, and English with their respective column means.
df.isnull().sum()
df['Math'].fillna(df['Math'].mean(), inplace=True)
df['Science'].fillna(df['Science'].mean(), inplace=True)
df['English'].fillna(df['English'].mean(), inplace=True)
df['History'].fillna(df['History'].mean(), inplace=True)
df.isnull().sum()
df

# ## Q3.4: Filtering by Performance
# #### Filter students with an average score above the overall mean and display their names and average scores.
overall_mean=df['Avg_score'].mean()
overall_mean
above_mean=df[df['Avg_score']>overall_mean]
above_mean
print(f"Overall Average Score: {overall_mean:.2f}")
print(f"\nStudents Above Average ({len(above_mean)} students):")
print(above_mean[['Name', 'Avg_score']].sort_values('Avg_score', ascending=False))

# ## Q3.5: Label-based Selection (loc)
# #### Use loc[] to update a specific student's Math score (e.g., StudentID 1001) to a new value.
student_id=1001
df.loc[df['StudentID'] == student_id , 'Math'] = 82
df
print(f"Updated Math score for StudentID {student_id}:")
print(df.loc[df['StudentID'] == student_id, ['Name', 'Math', 'Avg_score']])

# ## Q3.6: Integer-based Selection (iloc)
# #### Use iloc[] to select the first 10 rows and the last 3 columns, display them
data=df.iloc[0:10, 3:] # It is used to select the rows from 0 to 9 and columns from 3 to last
data
subset= df.iloc[0:10, -3:] # It is used to select the rows from 0 to 9 and columns last 3 rows only
print("First 10 Rows,last 3 Columns")
print(subset)

# ## Q3.7: Sorting
# #### Sort students by AttendancePercentage in descending order and display the top 5
sort=df.sort_values(by='AttendancePercentage',ascending=False)
sort.head()
top_attendance = df.nlargest(5, 'AttendancePercentage')
print("Top 5 Students by Attendance:")
print(top_attendance[['Name', 'AttendancePercentage', 'Grade']])

# ## Q3.8: Conditional Column Creation
# #### Create a new column 'PassFail' where 'Pass' if average score > 50, else 'Fail'
# lambda- It is a nameless function to written in one line
# apply- to perform a custom operation on each value or rows or columns
df['PassFail'] = df['Avg_score'].apply(lambda x: 'Pass' if x > 50 else 'Fail')
print("Pass/Fail Distribution:")
print(df['PassFail'].value_counts())
print(df[['Name', 'Avg_score', 'PassFail']].head(10))

# ## Q3.9: Duplicate Removal
# #### Identify and remove duplicate rows (if any) based on all columns.
duplicates=df.duplicated().sum()
duplicates

# ## Q3.10: Data Export
# #### Export the cleaned and processed data to student_scores_cleaned.csv.
cleaned=df.to_csv('student_scores_cleaned.csv',index=False)

# ## Challenge Extension
# ### Challenge 1
# #### Create a grade categorization (A, B, C, D, F) based on average scores
# lambda- It is a nameless function to written in one line
# apply- to perform a custom operation on each value or rows or columns
df['Grade_Name'] = df['Avg_score'].apply(
    lambda x: 'A' if x >= 90 else
              'B' if x >= 75 else
              'C' if x >= 60 else
              'D' if x >= 50 else 'F'
)
print(df[['Name', 'Avg_score', 'Grade']])
df
def get_grade(Avg_score):
    if Avg_score >= 90:
        return 'A'
    if Avg_score >= 75:
        return 'B'
    if Avg_score >= 60:
        return 'C'
    if Avg_score >= 50:
        return 'D'
    else:
        return 'F'
df['Grade_Category'] = df['Avg_score'].apply(lambda x: get_grade(x))
df
bins = [0, 50, 60, 75, 90, 100]
labels = ['F', 'D', 'C', 'B', 'A']
#cut is used to convert the continuous numeric scores into categorical grades using predefined ranges
df['Grade'] = pd.cut(df['Avg_score'], bins=bins, labels=labels, right=False)
print(df[['Name', 'Avg_score', 'Grade']].head(10))

# ## Challenge 2: 
# #### Calculate z-scores for each subject and identify outlier students
# Calculate z-scores
subjects=df[['Math','Science','English','History']]
for subject in subjects:
    df[f"{subject}_z"] = ((df[subject] - df[subject].mean()) / df[subject].std())

outliers = df[(df['Math_z'].abs() > 3) |(df['Science_z'].abs() > 3) | (df['English_z'].abs() > 3)]
print("Outlier Students:")
print(outliers[['StudentID', 'Name','Math_z', 'Science_z', 'English_z']])

# ## Challenge 3
# #### Generate a summary report by Grade (A, B, C, etc.) showing statistics.
grade_summary = df.groupby('Grade')['Avg_score'].agg(Student_Count='count',Average_Score='mean',Min_Score='min',Max_Score='max')
grade=grade_summary.reset_index()
print("Grade-wise Summary Report:")
print(grade)