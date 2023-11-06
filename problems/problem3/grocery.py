def main():
    grocery_dict = {}

    while True:
        try:
            item = input().lower()
            
            if item in grocery_dict:
                grocery_dict[item] += 1
            else:
                grocery_dict[item] = 1

        except EOFError:
            sorted_grocery_dict = dict(sorted(grocery_dict.items()))
            for item in sorted_grocery_dict:
                print(f"{sorted_grocery_dict[item]} "+item.upper())

            break


if __name__ == "__main__":
    main()