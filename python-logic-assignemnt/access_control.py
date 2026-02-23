age = int(input("Enter age: "))
has_id_input = input("Do you have an ID card (True/False): ")

if has_id_input.lower() == "true":
    has_id = True
elif has_id_input.lower() == "false":
    has_id = False
else:
    print("Invalid ID input")
    exit()

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
