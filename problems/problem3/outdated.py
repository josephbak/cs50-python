def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    while True:
        date = input("Date: ")
        if "/" in date:
            try:
                month, day, year = date.split("/")
                month, day, year = int(month), int(day), int(year)
                if month < 1 or month > 12 or day < 1 or day >31:
                    pass
                else:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break
            except:
                print("wrong format")
        else:
            try:
                month, day, year = date.split(" ")
                if month not in months or int(day[:-1]) < 1 or int(day[:-1]) > 31:
                    pass
                else:
                    month = int(months.index(month) + 1)
                    day = int(day[:-1]) 
                    year = int(year)
                    print(f"{year:04}-{month:02}-{day:02}")
                    break
            except:
                print("wrong format")

if __name__ == "__main__":
    main()