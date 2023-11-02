def main():
    # Ask use for their name
    # name = input("What's your name? ").strip().title()
    # hello(name)
    x = int(input("What's x? "))
    print("x squared is", square(x))

def hello(to="world"):
    print("hello", to)

def square(n):
    return n * n

# Remove whitespace from str
# name = name.strip()
# Capitalize user's name
# name = name.title()

# Split user's name into first name and last name
# first, last = name.split(" ")

# Say hello to user
# print("hello, " + name)
# print("hello,", name)
# print("hello, ", name, end="??")
# print(f"hello, {name}")

main()