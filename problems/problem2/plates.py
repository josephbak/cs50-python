import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    nums_0 = "0123456789"

    # check the length requirement
    if len(s) < 2 or len(s) > 6:
        return False

    # first two leters requirement
    for c in s[:2]:
        if c in nums_0:
            return False

    # check the punctuation
    for c in s:
        if c in string.punctuation or c == " ":
            return False
   
    if not number_requirement(s):
        return False
        
    return True


def number_requirement(s):
    nums = "123456789"
    nums_0 = "0123456789"

    for c in s:
        # first number can't be 0
        if c == "0" and s[s.index(c)-1] not in nums:
            return False
        if c in nums_0:
            for ele in s[s.index(c):]:
                if ele not in nums_0:
                    return False
    return True

main()