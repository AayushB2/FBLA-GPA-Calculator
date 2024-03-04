import tkinter as tk
from tkinter import *
import class_entry 
from class_entry import *

#root means the root application. Here is where we are creating the window
root = tk.Tk()
root.title("GPA Calculator")
#The first  parameter is for the width and the second is for the height
root.resizable(False,False)
#We are setting the width and height of the window in this function. 
#The left number is the width and the right number is the height
root.geometry("800x500")

u_gpas =[]
w_gpas = []

classes = []
widget_list = []
first_class = EntryRow(0, root, widget_list, classes)
classes.append(first_class)

def add_classes():
    if len(classes) >= 2:
        if classes[-1].not_toggled[0]:
            new_row_number = classes[-1].row_number + 1
            print(classes[-1])
            print(classes.index(classes[-1]))
            print("this is new row number ", new_row_number)
            add_class.grid(row=new_row_number + 4)
            calc_gpa.grid(row=new_row_number + 5)
            gpa_text.grid(row=new_row_number + 6)
            new_class = EntryRow(new_row_number, root, widget_list, classes)
            classes.append(new_class)
            print("this is len ", len(classes))
        else:
            new_row_number = classes[-1].add_assignment.grid_info()['row']+1
            add_class.grid(row=new_row_number + 4)
            calc_gpa.grid(row=new_row_number + 5)
            gpa_text.grid(row=new_row_number + 6)
            new_class = EntryRow(new_row_number, root, widget_list, classes)
            classes.append(new_class)
            print("this is len ", len(classes))
    else:
        if classes[0].not_toggled[0]:
            new_row_number = classes[0].row_number + 1
            print(new_row_number)
            print('hi ', classes[0].name.grid_info()['row'])
            add_class.grid(row=new_row_number + 4)
            calc_gpa.grid(row=new_row_number + 5)
            gpa_text.grid(row=new_row_number + 6)
            new_class = EntryRow(new_row_number, root, widget_list, classes)
            classes.append(new_class)
            print("this is len ", len(classes))
        else:
            new_row_number = classes[0].add_assignment.grid_info()['row'] + 1
            print(classes[0].add_assignment.grid_info()['row'])
            add_class.grid(row=new_row_number + 4)
            calc_gpa.grid(row=new_row_number + 5)
            gpa_text.grid(row=new_row_number + 6)
            print(add_class, add_class.grid_info())
            new_class = EntryRow(new_row_number, root, lambda entry: classes.remove(entry), widget_list, classes)
            classes.append(new_class)
            print("this is len ", len(classes))


add_class = tk.Button(width = 61, command = add_classes, text="Add Class")
add_class.grid(row = (classes[-1].row_number + 3), column = 0, sticky = W, columnspan = 3)
widget_list.append(add_class)

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
gpa_text.grid(row=(classes[-1].row_number + 5), column = 2, pady=25, sticky = 'nsew')
gpa_text['state'] = 'disabled'
widget_list.append(gpa_text)


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
    gpa_text.delete(1.0, END)
    gpa_text.insert('1.0',f"Your unweighted GPA is {round(sum(u_gpas)/len(u_gpas), 3)} \nYour weighted GPA is {round(sum(w_gpas)/len(w_gpas), 2)}")
    gpa_text['state'] = 'disabled'

calc_gpa = tk.Button(width = 61, command = run_calc_button, text="Calculate GPA")
calc_gpa.grid(row = (classes[-1].row_number + 4), column = 0, sticky=W, columnspan = 3)
widget_list.append(calc_gpa)




def reset_rows():
    print(classes)
    print("this is the type ", type(classes))
    for i in list(classes):
        print(i)
        print("index haha ", classes.index(i))
        if(classes.index(i) != 0):
            print("Ur good")
            i.toggle_btn.destroy()
            i.name.destroy()
            i.grade.destroy()
            i.weight.destroy()
            i.remove_but.destroy()
            i.add_assignment.destroy()

            for x in list(i.class_assignments):
                x.assignment_name.destroy()
                x.assignment_grade.destroy()
                x.assignment_weight.destroy()
                i.class_assignments.remove(x)
            classes.remove(i)
        else:
            print("u suck lol")
            for x in list(i.class_assignments[1:]):
                x.assignment_name.destroy()
                x.assignment_grade.destroy()
                x.assignment_weight.destroy()
                i.class_assignments.remove(x)

        
        print(len(classes))
    print(classes)    
reset = tk.Button(width = 20, text="Reset", command = reset_rows)
reset.grid(row = 0, column = 5, sticky=W, columnspan = 3)
widget_list.append(reset)

root.mainloop()

