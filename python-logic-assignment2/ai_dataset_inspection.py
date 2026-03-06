import pandas as pd

# Load dataset
df = pd.read_csv("sample_dataset.csv")

print("----- First 5 Rows -----")
print(df.head())

print("\n----- Last 5 Rows -----")
print(df.tail())

print("\n----- Dataset Info -----")
print(df.info())

print("\n----- Summary Statistics -----")
print(df.describe())

# Select a single column
age_column = df["Age"]
print("\n----- Selected Single Column (Age) -----")
print(age_column)

# Select multiple columns
selected_columns = df[["Name", "Score"]]
print("\n----- Selected Multiple Columns (Name & Score) -----")
print(selected_columns)

# Filter rows where Score > 80
filtered_rows = df[df["Score"] > 80]
print("\n----- Filtered Rows (Score > 80) -----")
print(filtered_rows)