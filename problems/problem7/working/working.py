import re
import sys


def main():
    # print(convert(input("Hours: ")))
    convert(input("Hours: "))


def convert(s):
    time_range_pattern = re.compile(r'\b([1-9]|1[0-2])\s?(?::[0-5][0-9])?\s?(AM|PM|am|pm)?\s?to\s?([1-9]|1[0-2])\s?(?::[0-5][0-9])?\s?(AM|PM|am|pm)?\b')
    # time_range_pattern = re.compile(r'\b(\d{1,2}(?::\d{2})?)\s?(AM|PM|am|pm)?\s?to\s?(\d{1,2}(?::\d{2})?)\s?(AM|PM|am|pm)?\b')
    # time_range_pattern = re.compile(r'\b(\d{1,2}(?::[0-5][0-9])?)\s?(AM|PM|am|pm)?\s?to\s?(\d{1,2}(?::[0-5][0-9])?)\s?(AM|PM|am|pm)?\b')
    # time_range_pattern = re.compile(r'\b(\d{1,2}(?::[0-5][0-9])?)\s?(AM|PM|am|pm)?\s?to\s?(\d{1,2}(?::[0-5][0-9])?)\s?(AM|PM|am|pm)?\b')

    # Test the regular expression
    test_strings = [
        "9AM to 5PM",
        "9:00 AM to 5:00 PM",
        "10 PM to 8 AM",
        "10:30 PM to 8:50 AM",
        "9:60 AM to 5:60PM",
        "9 AM - 5 PM",
        "09:00 AM - 17:00PM"
    ]

    for test_string in test_strings:
        match = time_range_pattern.search(test_string)
        if match:

            print(f"Match: {test_string}")
            print(f"Start Hour: {match.group(1)}")
            print(f"Start AM/PM: {match.group(2)}" if match.group(2) else "")
            print(f"End Hour: {match.group(3)}")
            print(f"End AM/PM: {match.group(4)}" if match.group(4) else "")
            print()

            # if match.group(2).lower() == "am":


        else:
            print(f"No match: {test_string}")
    # print(s)

    # match = time_range_pattern.search(s)
    # print(match)
    # if match:
    #     print(match.group(0))
    # else:
    #     print("none")


if __name__ == "__main__":
    main()