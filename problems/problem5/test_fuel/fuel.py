def main():
    user_input = input("Fraction: ")
    print(gauge(convert(user_input)))

    # while True:
    #     user_input = input("Fraction: ")
    #     if "/" in user_input:
    #         x, y = user_input.split("/")
    #         try:
    #             x = int(x)
    #             y = int(y)
    #             try:
    #                 percent = x/y
    #                 if x > y:
    #                     pass
    #                 else:
    #                     percent = round(x/y * 100)
    #                     if percent <= 1:
    #                         print("E")
    #                     elif percent >= 99:
    #                         print("F")
    #                     else:
    #                         print(percent, "%", sep="")
    #                     break
    #             except ZeroDivisionError:
    #                 print("Zero division not permitted")
    #         except ValueError:
    #                 print("Non integer not permitted")
    #     else:
    #         print("Type a correct fraction.")


def convert(fraction):
    x, y = fraction.split("/")
    try:
        x = int(x)
        y = int(y)
        if x > y:
            raise ValueError("x is greater than y")
        try:
             return round(x/y * 100)
        except ZeroDivisionError:
            print("Can't divide by 0")
    except ValueError:
        print("Integer only")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
