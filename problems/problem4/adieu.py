def main():
    name_list = []
    while True:
        try:
            name_list.append(input("Name: "))
        except EOFError:
            if len(name_list) == 1:
                print("Adieu, adieu, to ", name_list[0], sep="")
            elif len(name_list) == 2:
                print("Adieu, adieu, to ", name_list[0], " and ", name_list[1], sep="")
            else:
                name_str = name_list[0]
                for name in name_list[1:-1]:
                    name_str = name_str + ", " + name
                print("Adieu, adieu, to ", name_str, ", and ", name_list[-1], sep="")
            break




if __name__ == "__main__":
    main()