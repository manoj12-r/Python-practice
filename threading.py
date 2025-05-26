import threading
import time
def print_numbers ():
    for i in range (1,6):
        print("numbers=",i)
        time.sleep()
def print_letters ():
    for letter in range ('a','b','c','d','e'):
        print("letters=", letter)
        time.sleep()
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

print("done")
