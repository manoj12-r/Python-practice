a=int(input())
b=int(input())
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("we cannot divide with zero")
d=a+b
print(d)
e=a-b
print(e)
f=a*b
print(f)

