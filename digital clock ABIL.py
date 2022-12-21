from tkinter import Tk
from tkinter import Label
import time
import sys



master = Tk()
master.title("digital clock")

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)

Label(master,font=("arial",30),text="Abil's digital clock",fg="white",bg="red").pack()
clock = Label(master,font=("arial",90),bg="grey",fg="white")
clock.pack()
get_time()
master.mainloop()
