def main():
    user_input = input("Input: ")
    print(shorten(user_input))

def shorten(word):
    shorten_word = ""
    vowels = "aeiouAEOIU"
    for c in word:
        if c not in vowels:
            shorten_word += c
    return shorten_word



if __name__ == "__main__":
    main()
