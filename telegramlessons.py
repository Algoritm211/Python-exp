from tkinter import *
from tkinter import ttk
import time
root = Tk()
root.geometry('400x300+700+300')

pole = Label(root, bg='blue')
pole.pack(fill=X, expand=True)


def pole_event(event):
    print(event)
    print('Left Click')

pole.bind('<Button-1>', pole_event)


def entry_event(event, key):
    print(event, key)


entry_1 = Entry(root, justify=CENTER, font='Arial 15')
entry_1.pack(fill=X, expand=True, padx=10, ipady=12)
entry_1.bind('<Button-1>',lambda event, key='Left Click': entry_event(event, key))
entry_1.bind('<Button-2>',lambda event, key='Right Click': entry_event(event, key))


root.mainloop()
