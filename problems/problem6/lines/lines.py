import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        file_path = sys.argv[1]
        if not is_python_file(file_path):
            sys.exit("Not a Python file")
        else:
            try:
                with open(file_path, 'r') as file:
                    counter = 0
                    for line in file:
                        # string method strip() returns true if it's not empty string.
                        if line.lstrip().startswith("#") or not line.strip():
                            continue
                        else:
                            counter += 1
                    print(counter)
                    return 0
            except FileNotFoundError:
                sys.exit("File does not exist")
            except Exception as e:
                sys.exit(f"An error occurred: {e}")

def is_python_file(file_path):
    return file_path.lower().endswith('.py')

if __name__ == "__main__":
    main()