# Student Marks Analyzer

# Store marks of 8 students
marks = [78, 85, 90, 65, 88, 92, 80, 74]

# Print full list
print("Full Marks List:", marks)

# Print first 3 marks using slicing
print("First 3 marks:", marks[:3])

# Print last 3 marks using slicing
print("Last 3 marks:", marks[-3:])

# Calculate highest, lowest and average
highest_mark = max(marks)
lowest_mark = min(marks)
average_mark = sum(marks) / len(marks)

print("Highest:", highest_mark)
print("Lowest:", lowest_mark)
print("Average:", average_mark)
