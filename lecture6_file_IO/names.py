# name = input("What's your name? ")

# w is for write and a is for append
# file = open("names.txt", "w")
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# using with, no need to close the file
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# with open("names.txt", "r") as file:
#     lines = file.readlines()
# for line in lines:
#     print("hello,", line.rstrip())

# with open("names.txt", "r") as file:
#     for line in file: # this reads line by line of file
#         print("hello,", line.rstrip())

# sorted
# names = []
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
# for name in sorted(names):
#     print(f"hello, {name}")


with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())