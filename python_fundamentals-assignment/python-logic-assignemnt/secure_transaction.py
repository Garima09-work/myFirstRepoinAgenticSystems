balance = int(input("Enter account balance: "))
withdrawal = int(input("Enter withdrawal amount: "))
verified_input = input("Are you verified (True/False): ")

if verified_input.lower() == "true":
    verified = True
elif verified_input.lower() == "false":
    verified = False
else:
    print("Invalid verification input")
    exit()

if verified and withdrawal <= balance:
    print("Withdrawal successful")
else:
    print("Transaction denied")
