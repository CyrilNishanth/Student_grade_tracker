students={}

n=int(input("Enter the no.of student:\n"))
sub=int(input("Enter the no.of subjects:\n"))
for i in range(n):
    student=input("Enter the student name:").title()
    marks=[]
    for j in range(sub):
        mark=int(input(f"Enter subject {j+1} marks: "))
        marks.append(mark)

def add_students(students,student,marks):
    students[student]=marks
    return students

def calculate_averages(student):
    averages={}
    for n,m in students.items():
        avg=sum(m)/len(m)
        averages[n]=avg
    return averages

def get_unique_grades(students):
    unique_grades = {}
    for name, marks in students.items():
        unique_grades[name] = list(set(marks))
    return unique_grades

for i in range(n):
    student=input("Enter the student name:").title()
    marks=[]
    for j in range(sub):
        mark=int(input(f"Enter subject {j+1} marks: "))
        marks.append(mark)
    students=add_students(students,student,marks)
averages= calculate_averages(students)
unique_grades=get_unique_grades(students)

print("\nAverage of all students:\n")
for name, marks in averages.items():
    print(f"{name}->{marks:.2f}")
print("\nUnique grades of all students:\n")
for name, grades in unique_grades.items():
    print(f"{name}->{marks}")
        


