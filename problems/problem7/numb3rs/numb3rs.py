import re

def main():
    print(validate(input("IPv4 Address: ")))
    # validate(input("IPv4 Address: "))


def validate(ip):
    if len(ip.split(".")) != 4:
        return False
    else:
        match = re.search(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
        print(match.group())
        ip_list = []
        if match:
            for i in range(1, 5):
                ip_list.append(int(match.group(i)))
            print(ip_list)
            return all(ele >= 0 for ele in ip_list) and all(ele <= 255 for ele in ip_list)
        else:
            return False


if __name__ == "__main__":
    main()