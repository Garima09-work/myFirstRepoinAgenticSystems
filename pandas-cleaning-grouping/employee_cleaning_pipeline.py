import pandas as pd
import numpy as np

# Creating sample dataset
data = {
    "Employee": ["Amit", "Neha", "Rahul", "Sneha", "Vikram", "Priya", "Arjun", "Divya"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance", "IT", "HR"],
    "Salary": [600000, 500000, np.nan, 700000, 520000, np.nan, 650000, 480000],
    "Temporary Notes": [
        "On probation", "Contract", "Pending docs", "Verified",
        "Intern", "New joiner", "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print("----- Original Dataset -----")
print(df)


print("\n----- Missing Values -----")
print(df.isnull())


mean_salary = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(mean_salary)

print("\n----- After Filling Missing Salary -----")
print(df)


df = df.drop(columns=["Temporary Notes"])

print("\n----- After Dropping Temporary Notes -----")
print(df)


df = df.rename(columns={"Salary": "Annual Salary"})

print("\n----- After Renaming Column -----")
print(df)


summary = df.groupby("Department").agg(
    Mean_Salary=("Annual Salary", "mean"),
    Employee_Count=("Employee", "count")
)

print("\n----- Final Summary Table -----")
print(summary)