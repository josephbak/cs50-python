name = input("What's your name? ")

# w is for write and a is for append
# file = open("names.txt", "w")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()