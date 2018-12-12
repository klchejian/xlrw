from Tkinter import *

def printkey(event):
    print('pressed:' + event.char)

def printWin(event):
    print('pressedinframe:' + event.char)

root = Tk()

frame = Frame(root)

entry = Entry(root)

entry.bind('<Key>', printkey)

frame.bind('<Key>', printWin)

frame.pack()
entry.pack()
root.mainloop()