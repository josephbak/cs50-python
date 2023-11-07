import requests
import sys
import json
from string import punctuation


def main():
    while True:
        if len(sys.argv) == 1:
            print("Missing command-line argument")
            sys.exit(1)
        elif len(sys.argv) == 2:
            try:
                num_of_coins = float(sys.argv[1])
                if num_of_coins < 0:
                    print("Enter a positive number")
                else:
                    try:
                        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
                        # print(json.dumps(r.json(), indent=2))
                        rson = r.json()
                        # print(rson)
                        # print(rson["bpi"]["USD"]["rate"])
                        rate_per_coin = extract_num(rson["bpi"]["USD"]["rate"])
                        # print(rate_per_coin)
                        # print(extract_num(rate_per_coin))
                        print(f"${rate_per_coin * num_of_coins:,.4f}")
                        break
                    except requests.RequestException:
                        print("request failed")
                        sys.exit(1)
            except:
                print("Command-line argument is not a number")
                sys.exit(1)
        else:
            print("Too many command-line arguments")
            sys.exit(1)

def extract_num(s):
    em = ""
    for c in s:
        if c == ",":
            pass
        else:
            em += c
    return float(em)



if __name__ == "__main__":
    main()
