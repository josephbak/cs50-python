def main():
    user_input = input("Input: ")
    shorten_output = ""
    for c in user_input:
        if not is_vowel(c):
            shorten_output += c
    print("Output: ",shorten_output, sep="")

def is_vowel(c):
    if c in "aeiouAEOIU":
        return True
    else:
        return False


if __name__ == "__main__":
    main()