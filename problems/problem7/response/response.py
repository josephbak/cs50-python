from validator_collection import validators, checkers, errors


def main():
    email = input("What's yhour email address? ")
    if checkers.is_email(email):
        print("Valid")
    else:
        print("Invalid")



if __name__ == "__main__":
    main()