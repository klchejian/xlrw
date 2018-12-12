import Tkinter
import tkMessageBox
from Tkinter import *
import ttk
import time

top = Tkinter.Tk()

def delRow(tree):
    x = tree.get_children()
    for item in x:
        tree.delete(item)

def newwin():
    #tkMessageBox.showinfo("Hello Python", "Hello Runoob")
    top1=Tkinter.Tk()
    top1.title('detail')

    inputentry = Entry(top1)
    inputentry.pack()

    tree = ttk.Treeview(top1,columns=['1','2','3'],show='headings')
    tree.column('1',width=110,anchor='center')
    tree.column('2',width=110,anchor='center')
    tree.column('3',width=110,anchor='center')
    tree.heading('1',text='name')
    tree.heading('2',text='value')
    tree.heading('3',text='note')
    li = ['nnmae','vvlue','nnote']
    tree.insert('','end',values=li)
    tree.grid()
    
    tree.pack()
    top1.mainloop()
    time.sleep(10)
    top1.title('second detail')
    delRow(tree)



B = Tkinter.Button(top, text ="newwin", command = newwin)
B.pack()

top.mainloop()
