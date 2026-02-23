# Employee Role Checker

# Store employee details in tuple
employee = (101, "Aman", "IT")

# Store roles in set
roles = {"editor", "viewer", "admin"}

# Print employee information using tuple indexing
print("Employee ID:", employee[0])
print("Employee Name:", employee[1])
print("Department:", employee[2])

# Check admin access
if "admin" in roles:
    print("Admin Access: Yes")
else:
    print("Admin Access: No")
