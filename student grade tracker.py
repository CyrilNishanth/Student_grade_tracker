students={}

total=0
averages={}
n=int(input("Enter the no.of student:\n"))
sub=int(input("Enter the no.of subjects:\n"))
for i in range(n):
    student=input("Enter the student name:").title()
    marks=[]
    for j in range(sub):
        mark=int(input(f"Enter subject {j+1} marks: "))
        marks.append(mark)
    students[student]=marks

for n,m in students.items():
    avg=sum(m)/len(m)
    averages[n]=avg

print("Averages of all students:\n")
for i,j in averages.items():
    print(f"{i}->{j}")
print("Set to list unique grades:\n")
for k in students.values():
    a=set(k)
print(a)


        
        


