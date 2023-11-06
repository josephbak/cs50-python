def main():

    while True:
        user_input = input("Fraction: ")
        if "/" in user_input:
            x, y = user_input.split("/")
            try:
                x = int(x)
                y = int(y)
                try:
                    percent = x/y
                    if x > y:
                        pass
                    else:
                        percent = round(x/y * 100)
                        if percent <= 1:
                            print("E")
                        elif percent >= 99:
                            print("F")
                        else:
                            print(percent, "%", sep="")
                        break
                except ZeroDivisionError:
                    print("Zero division not permitted")
            except ValueError:
                    print("Non integer not permitted")
        else:
            print("Type a correct fraction.")


if __name__ == "__main__":
    main()