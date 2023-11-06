def main():

    food_dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    total_cost = 0

    while True:
        try:
            item = input("Item: ").title()
            item_cost = food_dict[item]
            total_cost += item_cost
            print(f"Total: ${total_cost:.2f}") #, item_cost, sep="")
        except KeyError:
            print("Food in not on the list. Please try again.")
        except EOFError:
            print("\n")
            break


if __name__ == "__main__":
    main()
