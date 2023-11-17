import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        file_path = sys.argv[1]
        if not is_python_file(file_path):
            sys.exit("Not a CSV file")
        else:
            try:
                with open(file_path) as file:
                    reader = csv.DictReader(file)
                    print(tabulate(reader, headers="keys", tablefmt="grid"))
                    return 0
            except FileNotFoundError:
                sys.exit("File does not exist")
            except Exception as e:
                sys.exit(f"An error occurred: {e}")

def is_python_file(file_path):
    return file_path.lower().endswith('.csv')

if __name__ == "__main__":
    main()