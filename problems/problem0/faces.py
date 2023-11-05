def main():
    user_input = input("")
    converted_user_input = convert(user_input)
    print(converted_user_input)

def convert(user_input):
    user_input_list = user_input.split()
    if ":)" in user_input_list:
        user_input_list =  ['🙂' if ele == ':)' else ele for ele in user_input_list]
    if ":(" in user_input_list:
        user_input_list =  ['🙁' if ele == ':(' else ele for ele in user_input_list]

    return " ".join(user_input_list)

main()
