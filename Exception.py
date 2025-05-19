class invalidMobile(Exception):
    pass
mobile=int(input())
x=int(mobile)
if x<0 or x>0 :
    print (x)
try:
    if x<0 or x>0:
        raise invalidMobile
except invalidMobile :
    print("mobile number should be 10 digits")
else:
    print(x)
