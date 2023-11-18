import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    time_pattern = re.compile(r'\b(?:\d{1,2}(:[0-5]\d)?\s*[APMapm]+ to \d{1,2}(:[0-5]\d)?\s*[APMapm]+)\b')

    # Test the regular expression
    # test_strings = [
    #     "9 AM to 5 PM",
    #     "9:00 AM to 5:00 PM",
    #     "10 PM to 8 AM",
    #     "10:30 PM to 8:50 AM",
    #     "9:60 AM to 5:60PM",
    #     "9 AM - 5 PM",
    #     "09:00 AM - 17:00PM"
    # ]

    match = time_pattern.search(s)
    # print(match)
    if match:
        s_list = s.split(" ") # 9:00, AM, to, 5, PM
        # print(s_list)
        if s_list[1].lower() == "pm":
            if s_list[0].split(":")[0] == "12":
                s_list[0] = "12:00"
            else:
                if ":" in s_list[0]: # ex) 9:00
                    s_list[0] = str(int(s_list[0].split(":")[0]) + 12) + ":" + s_list[0].split(":")[1]
                else: # ex) 9
                        s_list[0] = str(int(s_list[0]) + 12) + ":00"
        else:
            if int(s_list[0].split(":")[0]) < 10:
                if ":" in s_list[0]: # ex) 9:00
                    s_list[0] = "0" + s_list[0]
                else: # ex) 9
                    s_list[0] = "0" + s_list[0] + ":00" 
            elif int(s_list[0].split(":")[0]) == 12:
                s_list[0] = "00:00"
            else:
                if ":" not in s_list[0]: # ex) 9
                    s_list[0] = s_list[0] + ":00"

        if s_list[4].lower() == "pm":
            if s_list[3].split(":")[0] == "12":
                s_list[3] = "12:00"
            else:
                if ":" in s_list[3]: # ex) 9:00
                    s_list[3] = str(int(s_list[3].split(":")[0]) + 12) + ":" + s_list[3].split(":")[1]
                else: # ex) 9
                    s_list[3] = str(int(s_list[3]) + 12) + ":00"
        else:
            if int(s_list[3].split(":")[0]) < 10:
                if ":" in s_list[3]: # ex) 9:00
                    s_list[3] = "0" + s_list[3]
                else: # ex) 9
                    s_list[3] = "0" + s_list[3] + ":00" 
            elif int(s_list[3].split(":")[0]) == "12":
                s_list[3] = "00:00"
            else:
                if ":" not in s_list[0]: # ex) 9
                    s_list[0] = s_list[0] + ":00"

        return s_list[0] + " to " + s_list[3]

    else:
        raise ValueError("value error")

if __name__ == "__main__":
    main()