import re
import sys


def main():
    print(parse(input("HTML: ")))
    # parse(input("HTML: "))


def parse(s):

    pattern = re.compile(r'<iframe[^>]*src=["\'](https?://[^"\']+)', re.IGNORECASE)

    # Find all matches in the HTML
    matches = pattern.findall(s)

    if matches and "embed" in matches[0]:
        ele = matches[0].split("/")[-1]
        return "https://youtu.be/" + ele
    else:
        return "None"

if __name__ == "__main__":
    main()