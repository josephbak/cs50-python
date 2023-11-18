import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):

    um_pattern = re.compile(r'\bum\b', re.IGNORECASE)
    # Count the number of matches
    um_count = len(um_pattern.findall(s))
    return count

if __name__ == "__main__":
    main()