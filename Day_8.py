import pandas as pd

# Sample data for sales transactions and customer information
sales_data = {
    'TransactionID': [1, 2, 3, 4, 5],
    'CustomerID': [101, 102, 103, 104, 101],
    'Amount': [250, 300, 400, 500, 600],
    'Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05']
}

# Sample data for customer information
customer_data = {
    'CustomerID': [101, 102, 103, 104],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [30, 35, 40, 25],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Convert data into DataFrame
sales_df = pd.DataFrame(sales_data)
customers_df = pd.DataFrame(customer_data)

# Show basic structure of sales_df
print("Sales DataFrame:")
print(sales_df.head())

# 1. Exploring the dataset (using shape and describe)
print("\nShape of sales data:", sales_df.shape)  # Get number of rows and columns
print("\nSales data statistics:")
print(sales_df.describe())  # Summary statistics
print("Sales dataframe", sales_df)
print("customers_df", customers_df)

# 2. Merging data (Sales with Customer info)
merged_df = pd.merge(sales_df, customers_df, on='CustomerID', how='inner')
print("\nMerged DataFrame:")
print(merged_df)

# 3. Accessing data using `loc` and `iloc`
print("\nAccess data using `loc` (row 1):")
print(merged_df.loc[1])

print("\nAccess data using `iloc` (row 2):")
print(merged_df.iloc[2])

# 4. Handling Missing Values
# Let's introduce some missing data for demonstration
merged_df.loc[2, 'Age'] = None  # Introduce missing value in Age column
print(merged_df)

# Check for missing values
print("\nCheck missing values (isnull):")
print(merged_df.isnull().sum())

# Fill missing values with the mean (for Age column)
merged_df['Age'] = merged_df['Age'].fillna(merged_df['Age'].mean())
print("\nData after filling missing values:")
print(merged_df)

# 5. Aggregation: Calculate the mean sales per customer
mean_sales = merged_df.groupby('CustomerName')['Amount'].mean()
print("\nMean sales per customer:")
print(mean_sales)

# Create a DataFrame for Patient Information
# 1) Patient Name
# 2) Age
# 3) Date of appointment
# 4) Patient ID
# Create a DataFrame named drag_quantity that includes column names as drag name, quantity, patient_id
# Filter DataFrame to get Patient name and age < 6

# Merge the dataframes with inner join of Patient information and drag quantity DataFrame
print()
print()
#2.Merging data (Sales with Customer info)
merged_df=pd.merge(sales_df, customers_df, on='CustomerID', how='inner')
print("\nMerged DataFrame:")
print(merged_df)
print()
merged_df=pd.merge(sales_df, customers_df, on='CustomerID', how='outer')
print("\nMerged DataFrame:")
print(merged_df)
print()
merged_df=pd.merge(sales_df, customers_df, on='CustomerID', how='left')
print("\nMerged DataFrame:")
print(merged_df)
print()
merged_df=pd.merge(sales_df, customers_df, on='CustomerID', how='right')
print("\nMerged DataFrame:")
print(merged_df)
