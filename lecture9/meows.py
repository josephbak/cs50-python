# Constants
# Type Hints, mypy


# class Cat:
#     MEOWS = 3

#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("meow")


# cat = Cat()
# cat.meow()

def meow(n: int) -> str:
    return "meow\n" * n
    # for _ in range(n):
    #     print("meow")


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")