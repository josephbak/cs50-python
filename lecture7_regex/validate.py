import re

email = input("What's your email? ").strip()

# username, domain = email.split("@")
# two boolian expressions
# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")

# in regex, ..* == .+
# in regex, \. means an actual .
# r"..." means a raw string meanihg as it is?
if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")