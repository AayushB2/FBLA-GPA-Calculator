import tkinter as tk
from tkinter import *
import class_entry 
from class_entry import *

#root means the root application. Here is where we are creating the window
root = tk.Tk()
root.title("GPA Calculator")
#The first  parameter is for the width and the second is for the height
root.resizable(True,True)
#We are setting the width and height of the window in this function. 
#The left number is the width and the right number is the height
root.geometry("800x500")

u_gpas =[]
w_gpas = []

classes = []
#Here we are defining the first class. We are saying to remove the class only if the length of 
#classes is not equal to zero. The reason for that is because we are assigning the variable prior
#to appending it, when we call the lambda there are 0 elements in the class
first_class = EntryRow(0, root, None)
classes.append(first_class)
print(len(classes))

def add_classes():
    new_row_number = classes[-1].row_number + 1
    add_class.grid(row = new_row_number + 1)
    calc_gpa.grid(row = new_row_number + 2)
    gpa_text.grid(row=new_row_number + 3)
    new_class = EntryRow(new_row_number, root, lambda entry: classes.remove(entry))
    classes.append(new_class)
    print(len(classes))


add_class = tk.Button(width = 61, command = add_classes, text="Add Class")
add_class.grid(row = (classes[-1].row_number + 1), column = 0, sticky = W, columnspan = 3)

def calculate_gpa(grade, weight):
    u_gpa = 0
    w_gpa = 0
    if weight == "CP":
        if grade >= 90 and grade<= 100:
            u_gpa = 4.0
            w_gpa = 4.0 
        elif grade >= 80 and grade < 90:
            u_gpa = 3.0
            w_gpa = 3.0
        elif grade >= 70 and grade < 80:
            u_gpa = 2.0
            w_gpa = 2.0
        elif grade >= 60 and grade < 70:
            u_gpa = 1.0
            w_gpa = 1.0
        if grade < 60:
            u_gpa = 0
            w_gpa = 0
    if weight == "Honors":
        if grade >= 90 and grade<= 100:
            u_gpa = 4.0
            w_gpa = 4.5 
        elif grade >= 80 and grade < 90:
            u_gpa = 3.0
            w_gpa = 3.5
        elif grade >= 70 and grade < 80:
            u_gpa = 2.0
            w_gpa = 2.5
        elif grade >= 60 and grade < 70:
            u_gpa = 1.0
            w_gpa = 1.5
        elif grade < 60:
            u_gpa = 0
            w_gpa = 0
                
    if weight == "AP" or weight == "IB":
        if grade >= 90 and grade<= 100:
            u_gpa = 4.0
            w_gpa = 5.0
        elif grade >= 80 and grade < 90:
            u_gpa = 3.0
            w_gpa = 4.0
        elif grade >= 70 and grade < 80:
            u_gpa = 2.0
            w_gpa = 3.0
        elif grade >= 60 and grade < 70:
            u_gpa = 1.0
            w_gpa = 2.0
        elif grade < 60:
            u_gpa = 0
            w_gpa = 0
    
    return u_gpa, w_gpa

gpa_text = tk.Text(root, width = 20, height = 10)
gpa_text.grid(row=(classes[-1].row_number + 3), column = 0, pady=25, sticky = 'nsew')
gpa_text['state'] = 'disabled'

def run_calc_button():
    for i in range(0,len(classes)):
        print("This is before calculating", classes[i].grade.get(), classes[i].weight.get())
        tmp_gpa, tmpw_gpa = calculate_gpa(int(classes[i].grade.get()), classes[i].weight.get())
        print("See whats happening ", classes[i].grade.get(), classes[i].weight.get())       
        u_gpas.append(tmp_gpa)
        w_gpas.append(tmpw_gpa)
    print(u_gpas)
    print(w_gpas)
    print(f"Your unweighted GPA is {sum(u_gpas)/len(u_gpas)} \nYour weighted GPA is {sum(w_gpas)/len(w_gpas)}")
    
    gpa_text['state'] = 'normal'
    gpa_text.insert(f"Your unweighted GPA is {sum(u_gpas)/len(u_gpas)} \nYour weighted GPA is {sum(w_gpas)/len(w_gpas)}")
    gpa_text['state'] = 'disabled'

calc_gpa = tk.Button(width = 61, command = run_calc_button, text="Calculate GPA")
calc_gpa.grid(row = (classes[-1].row_number + 2), column = 0, sticky=W, columnspan = 3)

"""
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
"""

root.mainloop()