from pyfiglet import Figlet
import sys
import random

def main():
    while True:
        if len(sys.argv) not in [1, 3]:
            sys.exit("Invalid usage")

        figlet = Figlet()
        if len(sys.argv) == 1:
            user_input = input("Input: ")
            figlet.setFont(font=random.choice(figlet.getFonts()))
            print(figlet.renderText(user_input))
            break
        elif len(sys.argv) == 3:
            if sys.argv[1] in ["-f", "-font"]:
                if sys.argv[2] in figlet.getFonts():
                    user_input = input("Input: ")
                    figlet.setFont(font=sys.argv[2])
                    print(figlet.renderText(user_input))
                    break
                else:
                    sys.exit("Invalid usage")
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
