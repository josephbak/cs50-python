# run: python scourgify.py before.csv after.csv
import csv
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        before_file_path = sys.argv[1]
        after_file_path = sys.argv[2]
        if not is_csv_file(before_file_path):
            sys.exit("Not a CSV file")
        else:
            try:
                source_data = []
                with open(before_file_path, 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        name_split(row)
                        source_data.append(row)

                # for l in source_data:
                #     print(l)

                with open(after_file_path, 'w', newline='') as dest_csv:
                    writer = csv.DictWriter(dest_csv, fieldnames = ['first', 'last', 'house'])
                    # Write the modified data to the destination file
                    writer.writeheader()  # Write the header row
                    writer.writerows(source_data) 
                    return 0

            except FileNotFoundError:
                sys.exit(f"Could not read {before_file_path}")
            except Exception as e:
                sys.exit(f"An error occurred: {e}")

def is_csv_file(file_path):
    return file_path.lower().endswith('.csv')

def name_split(dict):
    dict['first'] = dict['name'].split(",")[1].strip() 
    dict['last'] = dict['name'].split(",")[0].strip()

    del dict['name']

if __name__ == "__main__":
    main()