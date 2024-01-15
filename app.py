import tkinter as tk
from tkinter import *

#root means the root application. Here is where we are creating the window
root = tk.Tk()
root.title("GPA Calculator")
#The first  parameter is for the width and the second is for the height
root.resizable(True,True)
#We are setting the width and height of the window in this function. 
#The left number is the width and the right number is the height
root.geometry("800x500")

default_text = ["Class Name", "Class Grade", "Class Weight(CP, Honors, AP, IB)"]

class EntryRow:
    def __init__(self, row_number):
        self.row_number = row_number
    
        def focus_in(event):
            entry = event.widget
            entry.delete(0, tk.END)
            entry.config(fg='black')

        def enter(event):
            entry = event.widget
            a = entry.get()
            print(a)
            root.focus()

        name= Entry(root, width= 20, fg ='grey')
        name.grid(row = row_number, column = 0)
        name.insert(0, default_text[0])

        name.bind("<FocusIn>", focus_in)
        name.bind("<Return>", enter)
        a = name.get()

        grade= Entry(root, width= 20, fg ='grey')
        grade.grid(row = row_number, column = 1)
        grade.insert(0, default_text[1])

        grade.bind("<FocusIn>", focus_in)
        grade.bind("<Return>", enter)

        weight= Entry(root, width= 30, fg ='grey')
        weight.grid(row = row_number, column = 2)
        weight.insert(0, default_text[2])

        weight.bind("<FocusIn>", focus_in)
        weight.bind("<Return>", enter)

classes = []
first_class = EntryRow(0)
classes.append(first_class)


def add_classes():
    new_row_number = classes[-1].row_number + 1
    add_class.grid(row = new_row_number + 1)
    new_class = EntryRow(new_row_number)
    classes.append(new_class)
    

add_class = tk.Button(width = 61, command = add_classes)
add_class.grid(row = (classes[-1].row_number + 1), column = 0, columnspan = 3)

root.mainloop()
