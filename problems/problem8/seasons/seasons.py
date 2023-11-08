from datetime import date
import sys
import re
import inflect

def main():
    user_input = input("Date of Birth: ")
    format_checker(user_input)
    diff = number_to_words(convert(user_input))
    # print(diff)
    # diff = number_to_words(round(float(diff)))
    print(diff.capitalize())



def format_checker(date_string):

    date_pattern = r'\d{4}-\d{2}-\d{2}'

    # Test with a date string
    if not re.match(date_pattern, date_string):
        print("Invalid date")
        sys.exit(1)

def convert(date_string):
    today = date.today()
    born_date = date.fromisoformat(date_string)
    delta = born_date - today
    delta_to_numbers = re.findall(r'\d+\.\d+', str(delta.total_seconds() / 60))
    # return "".join(delta_to_numbers)
    # print(delta_to_numbers[0])
    return round(float(delta_to_numbers[0]))

def number_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number, andword="") + " minutes"

if __name__ == "__main__":
    main()