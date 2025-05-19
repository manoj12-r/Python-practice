class invalidMobile(Exception):
    pass

try:
    mobile = input("Enter your mobile number: ")
    if not mobile.isdigit() or len(mobile) != 10:
        raise invalidMobile
except invalidMobile:
    print("Mobile number should be 10 digits and numeric.")
else:
    print("Valid mobile number:", mobile)
