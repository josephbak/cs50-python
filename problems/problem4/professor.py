import random


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                print("Please enter one of 1, 2, or 3 level.")
            else:
                return level
        except:
            print("That's not an integer.")


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError
    else:
        count_flag = 0
        score = 0
        num_of_probs = 1
        a, b = level_to_num_digits(level)
        x, y = random.randint(a, b), random.randint(a, b)
        while num_of_probs <= 10:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer != x + y:
                    count_flag += 1
                    if count_flag == 3:
                        print(f"{x} + {y} = {x + y}")
                        num_of_probs += 1
                        x, y = random.randint(a, b), random.randint(a, b)
                    else:
                        print("EEE")
                else:
                    score += 1
                    num_of_probs += 1
                    x, y = random.randint(a, b), random.randint(a, b)
            except:
                count_flag += 1
                if count_flag == 3:
                    print(f"{x} + {y} = {x + y}")
                    num_of_probs += 1
                    x, y = random.randint(a, b), random.randint(a, b)
                else:
                    print("EEE")
        print(f"Score: {score}")


def level_to_num_digits(level):
    if level == 1:
        return 0, 9
    elif level == 2:
        return 10, 99
    elif level == 3:
        return 100, 999
    else:
        raise ValueError

if __name__ == "__main__":
    main()
