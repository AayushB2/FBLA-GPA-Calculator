import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

default_text = ["Class Name", "Class Grade", "Class Weight(CP, Honors, AP, IB)", 
                "Assignment Name", "Assignment Grade", "Assignment Weight"]

class EntryRow:
    def __init__(self, row_number, root, win_widget_list, class_list):
        self.row_number = row_number
        self.root = root        

        self.win_widget_list = win_widget_list
        self.class_list = class_list
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
        name.grid(row = row_number, column = 1, sticky='nsew', padx=0)
        name.insert(0, default_text[0])

        name.bind("<FocusIn>", focus_in)
        name.bind("<Return>", enter)
        self.name = name

        grade= Entry(root, width= 20, fg ='grey')
        grade.grid(row = row_number, column = 2, sticky='nsew', padx=0)
        grade.insert(0, default_text[1])
        
        grade.bind("<FocusIn>", focus_in)
        grade.bind("<Return>", enter)
        self.grade = grade

        weight= Entry(root, width= 30, fg ='grey')
        weight.grid(row = row_number, column = 3, sticky='nsew', padx=0)
        weight.insert(0, default_text[2])

        weight.bind("<FocusIn>", focus_in)
        weight.bind("<Return>", enter)
        self.weight = weight

        remove_image = Image.open("C:\FBLA\Red_X.png")
        remove_image = remove_image.resize((30, 30))
        remove_img = ImageTk.PhotoImage(remove_image)
        self.remove_img = remove_img

        def remove_row():
            self.name.destroy()
            self.grade.destroy()
            self.weight.destroy()
            self.remove_but.destroy()
            self.toggle_btn.destroy()
            self.add_assignment.destroy()

            for i in list(self.class_assignments):
                i.assignment_name.destroy()
                i.assignment_grade.destroy()
                i.assignment_weight.destroy()
                class_assignments.remove(i)
            class_list.remove(self) 

        remove_but = Button(root, image=remove_img,command= remove_row, borderwidth=0, relief="flat")
        remove_but.grid(row=row_number, column=4, sticky='nsew')
        self.remove_but = remove_but

        class Assignment(EntryRow):
            def __init__(self, parent_class, row_n, add_btn):
                self.row_n = row_n
                self.parent_class = parent_class
                assignment_name = Entry(root, width= 20, fg ='grey')
                assignment_name.grid(row = row_n+1, column = 1, sticky='nsew', padx=0)
                assignment_name.insert(0, default_text[3])

                assignment_name.bind("<FocusIn>", focus_in)
                assignment_name.bind("<Return>", enter)
                self.assignment_name = assignment_name
                assignment_name.grid_forget()

                assignment_grade= Entry(root, width= 20, fg ='grey')
                assignment_grade.grid(row = row_n+1, column = 2, sticky='nsew', padx=0)
                assignment_grade.insert(0, default_text[4])
                        
                assignment_grade.bind("<FocusIn>", focus_in)
                assignment_grade.bind("<Return>", enter)
                self.assignment_grade = assignment_grade
                assignment_grade.grid_forget()

                assignment_weight= Entry(root, width= 30, fg ='grey')
                assignment_weight.grid(row = row_n+1, column = 3, sticky='nsew', padx=0)
                assignment_weight.insert(0, default_text[5])

                assignment_weight.bind("<FocusIn>", focus_in)
                assignment_weight.bind("<Return>", enter)
                self.assignment_weight = assignment_weight
                assignment_weight.grid_forget()

                self.add_btn = add_btn
                
            
                
        
        add_assignment = tk.Button(width = 61, text="Add Assignment ")
        add_assignment.grid(row = row_number + 2, column = 1, sticky = W, columnspan = 3)
        self.add_assignment = add_assignment
        add_assignment.grid_forget()

        class_assignments = []
        self.class_assignments = class_assignments
        first_assignment = Assignment(self, row_number, add_assignment)
        class_assignments.append(first_assignment)

        
        def add_assignments():
            if(win_widget_list != None):
                self_idx = class_list.index(self)
                new_row_n = class_assignments[-1].row_n + 2
                new_assignment = Assignment(self, new_row_n, add_assignment)
                class_assignments.append(new_assignment)
                class_assignments[-1].assignment_name.grid(row=new_row_n, column=1, sticky='nsew', padx=0)
                class_assignments[-1].assignment_grade.grid(row=new_row_n, column=2, sticky='nsew', padx=0)
                class_assignments[-1].assignment_weight.grid(row=new_row_n, column=3, sticky='nsew', padx=0)
                add_assignment.grid(row=new_row_n + 1, column=1, sticky=W, columnspan=3)
                
                if class_list[-1] != self:
                    print("y")
                    for i in class_list[self_idx+1:]:
                        print("e")
                        if(class_list[class_list.index(i)-1].not_toggled[0]):
                            print("z")
                            new_row_n = class_list[class_list.index(i)-1].name.grid_info()['row']+1
                            i.name.grid(row=new_row_n)
                            i.weight.grid(row=new_row_n)
                            i.grade.grid(row=new_row_n)
                            i.remove_but.grid(row=new_row_n)
                            i.toggle_btn.grid(row=new_row_n)
                        else:
                            print("s")
                            new_row_n = class_list[class_list.index(i)-1].add_assignment.grid_info()['row']+1
                            i.name.grid(row=new_row_n)
                            i.weight.grid(row=new_row_n)
                            i.grade.grid(row=new_row_n)
                            i.remove_but.grid(row=new_row_n)
                            i.toggle_btn.grid(row=new_row_n)
                        if not i.not_toggled[0]:
                            print("x")
                            i.add_assignment.grid(row=i.class_assignments[-1].assignment_name.grid_info()['row']+1)
                else:
                    class_assignments[-1].assignment_name.grid(row=self.class_assignments[-1].assignment_name.grid_info()['row']+1, column=1, sticky='nsew', padx=0)
                    class_assignments[-1].assignment_name.insert(0, 'helo beta')
                
                print(len(class_assignments))
                win_widget_list[0].grid(row=win_widget_list[0].grid_info()['row']+3)
                win_widget_list[1].grid(row=win_widget_list[1].grid_info()['row']+5)
                win_widget_list[2].grid(row=win_widget_list[2].grid_info()['row']+4)
        add_assignment.configure(command=add_assignments)

        toggle_text = ["v"]
        not_toggled = [True]
        self.toggle_text = toggle_text
        self.not_toggled = not_toggled

        def toggle(btn, text):
                btn.configure(text=text[0])
                if text[0] == "v":
                    not_toggled[0] = False
                    if len(class_list) >= 2:
                        self_idx = class_list.index(self)
                        add_assignment.grid()
                        x = add_assignment.grid_info()['row']
                        for temp_incrm, i in enumerate(class_list[self_idx+1:]):
                            temp_incrm += 1
                            i.name.grid(row=x+temp_incrm)
                            i.weight.grid(row=x+temp_incrm)
                            i.grade.grid(row=x+temp_incrm)
                            i.toggle_btn.grid(row=x+temp_incrm)
                            i.remove_but.grid(row=x+temp_incrm)
                            if not i.not_toggled[0]:
                                for a in i.class_assignments:
                                    temp_incrm = temp_incrm + 1
                                    print("name row ", i.name.grid_info()['row'])
                                    a.assignment_name.insert(0, str(i))
                                    print("lolol ", a.assignment_name, i, self)
                                    print("hahahed ", class_list.index(self))
                                    a.assignment_name.grid(row=i.name.grid_info()['row'] + temp_incrm, column=1, sticky='nsew', padx=0)
                                    a.assignment_grade.grid(row=i.grade.grid_info()['row'] + temp_incrm, column=2, sticky='nsew', padx=0)
                                    a.assignment_weight.grid(row=i.weight.grid_info()['row'] + temp_incrm, column=3, sticky='nsew', padx=0)
                                    add_assignment.grid(row=i.class_assignments[-1].assignment_name.grid_info()['row'] +1, column=1, sticky=W, columnspan=3)
                            
                        for temp_incrm, i in enumerate(class_assignments):
                            temp_incrm = temp_incrm + 1
                            print("name row ", i.parent_class.name.grid_info()['row'])
                            i.assignment_name.insert(0, str(i.parent_class))
                            print("lolol ", i.assignment_name, i.parent_class, self)
                            print("hahahed ", class_list.index(self))
                            i.assignment_name.grid(row=self.name.grid_info()['row'] + temp_incrm, column=1, sticky='nsew', padx=0)
                            i.assignment_grade.grid(row=self.grade.grid_info()['row'] + temp_incrm, column=2, sticky='nsew', padx=0)
                            i.assignment_weight.grid(row=self.weight.grid_info()['row'] + temp_incrm, column=3, sticky='nsew', padx=0)
                            add_assignment.grid(row=i.parent_class.name.grid_info()['row'] + temp_incrm+1, column=1, sticky=W, columnspan=3)
                        win_widget_list[0].grid(row=x+2)
                        win_widget_list[1].grid(row=x+4)
                        win_widget_list[2].grid(row=x+3)
                    else:
                        for idx, i in enumerate(class_assignments):
                            self.class_assignments[idx].assignment_name.grid(row = self.name.grid_info()['row']+1, column = 1, sticky='nsew', padx=0)
                            self.class_assignments[idx].assignment_grade.grid(row = self.grade.grid_info()['row']+1, column = 2, sticky='nsew', padx=0)
                            self.class_assignments[idx].assignment_weight.grid(row = self.weight.grid_info()['row']+1, column = 3, sticky='nsew', padx=0)
                    add_assignment.grid(row = self.class_assignments[-1].assignment_weight.grid_info()['row'] + 1, column = 1, sticky = W, columnspan = 3)
                    x = add_assignment.grid_info()['row']
                    win_widget_list[0].grid(row=x+2)
                    win_widget_list[1].grid(row=x+4)
                    win_widget_list[2].grid(row=x+3)
                    text[0] = "^"
                    return btn.configure(text=text[0])
                if text[0] == "^":
                    not_toggled[0] = True
                    for idx, i in enumerate(class_assignments):
                        self.class_assignments[idx].assignment_name.grid_forget()
                        self.class_assignments[idx].assignment_grade.grid_forget()
                        self.class_assignments[idx].assignment_weight.grid_forget()
                        self.add_assignment.grid_forget()
                    text[0] = "v"
                    return btn.configure(text=text[0])
                    
                if text[0] == None:
                    return btn.configure(text=None)
                    print(text)

        toggle_btn = Button(root, text=toggle_text, relief = "flat")
        toggle_btn.configure(command= lambda: toggle(toggle_btn, toggle_text))
        toggle_btn.grid(row=self.class_assignments[-1].row_n, column=0)
        self.toggle_btn = toggle_btn
