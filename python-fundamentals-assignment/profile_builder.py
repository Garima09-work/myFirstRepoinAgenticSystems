name = input("Enter your name: ")
age = input("Enter your age: ")
active_status = input("Are you an active user (True/False): ")

age = int(age)
active_status = active_status == "True"

print(f"User {name} is {age} years old. Active status: {active_status}")
