import tkinter as tk
root=tk.Tk()
root.title("button example")
root.geometry("300x200")
def say_hello():
    print("hello button was clicked")
def say_goodbye():
    print("goodbye button was clicked ")
button1=tk.Button(root,text="say hello",command=say_hello)
button2=tk.Button(root,text="say goodbye",command=say_goodbye)
button1.pack(pady=10)
button2.pack(pady=10)
root.mainloop()
