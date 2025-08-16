def add_student(students,student,marks):
    students[student]=marks
    return students

def calculate_averages(students):
    averages={}
    for n,m in students.items():
        avg=sum(m)/len(m)
        averages[n]=avg
    return averages

def get_unique_grades(students):
    grades=set()
    for marks in students.values():
        grades.update(marks)
    return grades
if __name__=="__main__":
    students={}
    n=int(input("Enter the no.of student:\n"))
    sub=int(input("Enter the no.of subjects:\n"))

    for i in range(n):
        student=input("Enter the student name:").title()
        marks=[]
        for j in range(sub):
            mark=int(input(f"Enter subject {j+1} marks: "))
            marks.append(mark)
        students=add_student(students,student,marks)
    averages= calculate_averages(students)
    unique_grades=get_unique_grades(students)

        


