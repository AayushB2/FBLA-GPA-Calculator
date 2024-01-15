import tkinter as tk
from tkinter import *

default_text = ["Class Name", "Class Grade", "Class Weight(CP, Honors, AP, IB)"]

class EntryRow:
    def __init__(self, row_number, root, remove_callback):
        self.row_number = row_number
        self.root = root        

        def focus_in(event):
            entry = event.widget
            entry.delete(0, tk.END)
            entry.config(fg='black')

        def enter(event):
            entry = event.widget
            a = entry.get()
            print(a)
            root.focus()

        name = Entry(root, width= 20, fg ='grey')
        name.grid(row = row_number, column = 0, sticky=W)
        name.insert(0, default_text[0])

        name.bind("<FocusIn>", focus_in)
        name.bind("<Return>", enter)
        self.name = name

        grade= Entry(root, width= 20, fg ='grey')
        grade.grid(row = row_number, column = 1, sticky=W)
        grade.insert(0, default_text[1])
        
        grade.bind("<FocusIn>", focus_in)
        grade.bind("<Return>", enter)
        self.grade = grade

        weight= Entry(root, width= 30, fg ='grey')
        weight.grid(row = row_number, column = 2, sticky=W)
        weight.insert(0, default_text[2])

        weight.bind("<FocusIn>", focus_in)
        weight.bind("<Return>", enter)
        self.weight = weight

        remove_img = PhotoImage(file = "C:\FBLA\Red_X.png")
        self.remove_img = remove_img

        def remove_row():
            if(remove_callback != None):
                self.name.grid_forget()
                self.grade.grid_forget()
                self.weight.grid_forget()
                self.remove_but.grid_forget()

                self.name.destroy()
                self.grade.destroy()
                self.weight.destroy()
                self.remove_but.destroy()

                remove_callback(self) 

        remove_but = Button(root, image=remove_img,command= remove_row)
        remove_but.grid(row=row_number, column=3, sticky=W)
        self.remove_but = remove_but
