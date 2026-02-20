# file_data_processing.py

def read_numbers(file_name):
    """
    Reads integers from a file and returns them as a list.
    """
    numbers_list = []

    with open(file_name, "r") as file:
        print("File opened successfully")

        for line in file:
            clean_line = line.strip()      # Remove whitespace
            if clean_line:                 # Avoid empty lines
                number = int(clean_line)
                numbers_list.append(number)

    print(f"Read {len(numbers_list)} numbers")
    return numbers_list


def compute_statistics(numbers):
    """
    Computes total count, sum, and average of numbers.
    """
    total_count = len(numbers)
    total_sum = sum(numbers)

    if total_count > 0:
        average_value = total_sum / total_count
    else:
        average_value = 0

    print("Computation completed")
    return total_count, total_sum, average_value


def write_log(file_name, total_count, total_sum, average_value):
    """
    Writes processing results to log file in append mode.
    """
    with open(file_name, "a") as log_file:
        log_file.write("File opened successfully\n")
        log_file.write(f"Read {total_count} numbers\n")
        log_file.write(f"Sum: {total_sum}\n")
        log_file.write(f"Average: {average_value}\n")
        log_file.write("Processing completed\n\n")


def main():
    input_file = "numbers.txt"
    log_file = "results.log"

    numbers = read_numbers(input_file)
    total_count, total_sum, average_value = compute_statistics(numbers)
    write_log(log_file, total_count, total_sum, average_value)


if __name__ == "__main__":
    main()