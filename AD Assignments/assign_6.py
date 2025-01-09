#Day_6 Assignments Question-1

import pandas as pd
data = {
    'Name': ['John', 'Alice', 'Bob', 'Diana'],
    'Age': [28, 34, 23, 29],
    'Department': ['HR', 'IT', 'Marketing', 'Finance'],
    'Salary': [45000, 60000, 35000, 50000]
}
df = pd.DataFrame(data)
print(df)

#Day_6 Assignments Question-2

import pandas as pd

data = {
    'Name': ['John', 'Alice', 'Bob', 'Diana'],
    'Age': [28, 34, 23, 29],
    'Department': ['HR', 'IT', 'Marketing', 'Finance'],
    'Salary': [45000, 60000, 35000, 50000]
}
df = pd.DataFrame(data)
print(df.head(2))
df['Bonus'] = df['Salary'] * 0.10
average_salary = df['Salary'].mean()
print("Average Salary:", average_salary)
filtered_employees = df[df['Age'] > 25]
print(filtered_employees)
