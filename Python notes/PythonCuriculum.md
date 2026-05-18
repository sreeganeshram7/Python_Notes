## **25-Hour Integrated Python Curriculum**

### **Learning Outcomes**

By the end of this course, learners will:

1. Understand object-oriented principles — classes, objects, inheritance, encapsulation, and error handling.
2. Apply data manipulation using NumPy arrays and Pandas DataFrames.
3. Read and process CSV files for structured analysis.
4. Visualize and interpret data with Matplotlib and Seaborn.

***

## **Part 1: Object-Oriented Programming and Error Handling (9 Hours)**

### **Session 1: Introduction to Classes and Objects (2 Hours)**

**Goals:**

- Understand why OOP is used in Python.
- Define and instantiate classes.

**Topics:**

- What is OOP? Benefits in Python.
- Defining a class using `class`.
- The `__init__()` constructor and `self`.
- Class vs instance variables.
- Instance methods and object creation.

**Hands-on Exercises:**

- Create a `Student` class with attributes (`name`, `age`, `marks`) and methods to calculate grade.
- Display student info using methods.

***

### **Session 2: Encapsulation and Data Validation (2 Hours)**

**Goals:**

- Learn how to hide data and enforce validation.

**Topics:**

- Public, private (`__attr`), protected (`_attr`) attributes.
- Getters and setters.
- The `@property` decorator for readable access.
- Validation example using setter.

**Hands-on Exercises:**

- Build a `BankAccount` class that restricts invalid withdrawals using encapsulation.
- Display transaction history using private attributes.

***

### **Session 3: Inheritance and Method Overriding (2 Hours)**

**Goals:**

- Apply inheritance and code reuse to model real-world entities.

**Topics:**

- Parent and child classes.
- The `super()` function.
- Overriding built-in and user-defined methods.
- Multiple inheritance overview.

**Hands-on Exercises:**

- Implement a `Vehicle` → `Car` → `ElectricCar` hierarchy.
- Override `car_details()` method to display additional attributes.

***

### **Session 4: Exception Handling (2 Hours)**

**Goals:**

- Manage program errors using Python’s exception model.

**Topics:**

- `try`, `except`, `else`, `finally`.
- Raising exceptions with `raise`.
- Creating custom exception classes.
- File handling exceptions (`FileNotFoundError`, `ValueError`).

**Hands-on Exercises:**

- Implement safe withdrawal in `BankAccount` raising `InsufficientBalanceError`.
- Handle missing CSV files gracefully.

***

## **Part 2: Data Handling and Manipulation (9 Hours)**

### **Session 5: Reading and Writing CSV Files (2 Hours)**

**Goals:**

- Learn how to read/write structured data files.

**Topics:**

- Reading CSV using `pandas.read_csv()` and the `csv` module.
- Writing CSVs with `.to_csv()`.
- Handling missing columns, delimiters, and data types.

**Hands-on Exercises:**

- Import a `sales.csv` dataset.
- Filter top-performing products.
- Save clean data as `filtered_sales.csv`.

***

### **Session 6: NumPy for Numeric Data (2 Hours)**

**Goals:**

- Apply NumPy for fast numeric computation.

**Topics:**

- Creating arrays with `np.array()`, `arange()`, and `reshape()`.
- Operations on arrays: element-wise arithmetic, broadcasting.
- Indexing, slicing, and Boolean masking.
- Statistical functions: `mean()`, `std()`, `sum()`, `min()`, `max()`.

**Hands-on Exercises:**

- Generate a 2D sales performance matrix.
- Calculate averages and totals per region.
- Filter high-performing regions using masks.

***

### **Session 7: Introduction to Pandas (2 Hours)**

**Goals:**

- Use DataFrames for tabular data processing.

**Topics:**

- Series vs. DataFrame.
- Data selection: `loc[]`, `iloc[]`, Boolean conditions.
- Sorting and filtering.
- Handling missing data: `fillna()`, `dropna()`.

**Hands-on Exercises:**

- Load `student_scores.csv`.
- Clean NaN values.
- Filter records by performance above the mean.

***

### **Session 8: Data Summarization and Grouping (2 Hours)**

**Goals:**

- Perform aggregation and categorization of data.

**Topics:**

- Grouping with `groupby()`.
- Aggregating data (`sum`, `mean`, `count`).
- Adding calculated columns.
- Exporting processed data.

**Hands-on Exercises:**

- Analyze `sales_data` grouped by region and category.
- Calculate revenue per state and save summary CSV.

***

## **Part 3: Data Visualization (5 Hours)**

### **Session 9: Basic Plotting with Matplotlib (2 Hours)**

**Goals:**

- Visualize patterns in data.

**Topics:**

- Introduction to `matplotlib.pyplot`.
- Line and bar plots: axes, labels, legends.
- Customization: colors, titles, grids.
- Saving charts as images.

**Hands-on Exercises:**

- Plot sales revenue using `plt.bar()`.
- Show top 5 products using `plt.plot()` with custom styles.

***

### **Session 10: Advanced Visualization with Seaborn (2 Hours)**

**Goals:**

- Create more insightful visualizations from Pandas data.

**Topics:**

- Introduction to Seaborn.
- Scatter plots, count plots, histograms.
- Combining Seaborn with Pandas directly.
- Styling Seaborn charts (`darkgrid`, `whitegrid`).

**Hands-on Exercises:**

- Plot revenue vs. region scatter using Seaborn.
- Create distribution plot for product categories.
- Explore correlation heatmap for numeric columns.

***

## **Final Project (2 Extra Hours Optional or Integrated in Sessions)**

**Project:** *Mini Retail Data Analyzer*

**Goal:** Combine OOP and data analysis.

- Use a `Product` and `SalesRecord` class to simulate real data.
- Read CSV of product sales.
- Handle exceptions for missing files or data.
- Perform cleaning and aggregations using Pandas.
- Plot sales performance charts with Matplotlib.

**Deliverables:**

- Python `.py` or `.ipynb` project file.
- Cleaned and visualized dataset.
- Presentation of insights (average sales, top products, total revenue).

***

### **Teaching Resources**

- **Tools:** Jupyter Notebook or VS Code.
- **Libraries:** `numpy`, `pandas`, `matplotlib`, `seaborn`, `csv`.
