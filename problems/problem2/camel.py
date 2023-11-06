def main():
    camel_case = input("cameCase: ")
    snake_case = camel_to_snake(camel_case)
    print(snake_case)


def camel_to_snake(camel_case):
    snake_case = ""
    for c in camel_case:
        if c.isupper():
            snake_case = snake_case + "_" + c.lower()
        else:
            snake_case = snake_case + c
    return snake_case

if __name__ == "__main__":
    main()