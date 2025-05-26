import threading
import time
def print_even():
    for i in range (0,11,2):
        print(i)
        time.sleep(0.5)
def print_odd():
    for i in range (1,11,2):
        print(i)
        time.sleep(0.5)

even_thread=threading.Thread(target=print_even)
odd_thread=threading.Thread(target=print_odd)

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()

print("both are completed")
