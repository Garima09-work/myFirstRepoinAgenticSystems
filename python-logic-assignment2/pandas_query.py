import pandas as pd

# Create a sample dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma", "Frank"],
    "Score": [95, 92, 78, 88, 84, 90],
    "Passed": [True, True, True, True, False, True],
    "Category": ["A", "A", "B", "B", "C", "A"]
}

df = pd.DataFrame(data)

print("----- Full Dataset -----")
print(df)


print("\n----- Single Column (Score) -----")
score_column = df["Score"]
print(score_column)


print("\n----- Multiple Columns (Name and Score) -----")
selected_columns = df[["Name", "Score"]]
print(selected_columns)


print("\n----- First 3 Rows using iloc -----")
print(df.iloc[0:3])

df_indexed = df.set_index("Name")

print("\n----- Row for Alice using loc -----")
print(df_indexed.loc["Alice"])

print("\n----- Students with Score > 85 -----")
high_scores = df[df["Score"] > 85]
print(high_scores)

print("\n----- Score > 85 AND Passed -----")
filtered = df[(df["Score"] > 85) & (df["Passed"] == True)]
print(filtered)


sorted_result = filtered.sort_values(by="Score", ascending=False)

print("\n----- High-performing students (sorted) -----")
print(sorted_result[["Name", "Score"]])

print("\n----- Chained Filtering and Sorting -----")
chained = df[(df["Score"] > 85) & (df["Passed"] == True)].sort_values(by="Score", ascending=False)
print(chained)