# student_evaluation.py

def greet_student(name):
    return f"Hello, {name}"

def calculate_scores(scores):
    total_subjects = len(scores)
    average_score = sum(scores) / total_subjects
    return total_subjects, average_score

def evaluate_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"

def main():
    name = input("Enter student name: ")

    scores_input = input("Enter scores separated by space: ")
    scores = list(map(float, scores_input.split()))

    greeting = greet_student(name)
    subjects, average = calculate_scores(scores)
    result = evaluate_result(average)

    print("\n--- Student Report ---")
    print(greeting)
    print("Subjects:", subjects)
    print("Average Score:", average)
    print("Result:", result)

# Start program
main()
