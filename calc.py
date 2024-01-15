grades = []
types = []
u_gpas = []
w_gpas = []

print("Input your grades:")
for i in range(0,4):
    if(i<=4):
        x = int(input())
        grades.append(x)
print(grades)

print("Input type for respective class(CP-C, Honors-H, AP-A, IB-I): ")
for i in range(0,4):
    if(i<=4):
        x = input()
        types.extend(x)
        print(types)
print(len(types))
def calculate_gpa(grade, type):
    u_gpa = 0
    w_gpa = 0
    print(grade, type)
    if type == "C":
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
    if type == "H":
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
                
    if type == "A" or type == "I":
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

for i in range(0,len(grades)):
    tmp_gpa, tmpw_gpa = calculate_gpa(grades[i], types[i])
    u_gpas.append(tmp_gpa)
    w_gpas.append(tmpw_gpa)
print(u_gpas)
print(w_gpas)
print(f"Your unweighted GPA is {sum(u_gpas)/len(u_gpas)} \nYour weighted GPA is {sum(w_gpas)/len(w_gpas)}")
