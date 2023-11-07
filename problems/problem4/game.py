import random


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                print("Please enter a positive integer.")
            else:
                rand_int = random.randint(1, level)
                while True:
                    try:
                        guess = int(input("Guess: "))
                        if guess <= 0:
                            print("Please enter a positive integer.")
                        else:
                            if guess < rand_int:
                                print("Too small!")
                            elif guess > rand_int:
                                print("Too large!")
                            else:
                                print("Just right!")
                                break
                    except:
                        print("Please enter a positive integer.")
                break
        except:
            print("Please enter a positive integer.")




if __name__ == "__main__":
    main()