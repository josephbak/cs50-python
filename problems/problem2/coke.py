def main():
    denominations = [5, 10, 25]
    due_amount = 50
    total_coin = 0
    while total_coin < 50:
        # total_coin = 0
        print("Amount Due: ", due_amount - total_coin, sep="")
        coin = int(input("Insert Coin: "))
        if coin in denominations:
            total_coin += coin
        
    print("Change Owed: ", total_coin - due_amount, sep="")
        


if __name__ == "__main__":
    main()