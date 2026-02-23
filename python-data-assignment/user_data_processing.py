# User Data Processing System

# Function to calculate average score of users
def calculate_average(scores):
    return sum(scores) / len(scores)


# Function to check admin access
def has_admin_access(user_roles):
    if "admin" in user_roles:
        return True
    else:
        return False


def main():
    # Store users data
    users = [
        {
            "name": "Alice",
            "scores": [80, 85, 90],
            "roles": {"admin", "editor"}
        },
        {
            "name": "Bob",
            "scores": [70, 75, 72],
            "roles": {"viewer"}
        },
        {
            "name": "Charlie",
            "scores": [88, 92, 84],
            "roles": {"editor", "viewer"}
        }
    ]

    # Process each user
    for user in users:
        print("\nName:", user["name"])

        avg_score = calculate_average(user["scores"])
        print("Average Score:", avg_score)

        admin_status = has_admin_access(user["roles"])
        print("Admin Access:", admin_status)


# Call main function
main()
