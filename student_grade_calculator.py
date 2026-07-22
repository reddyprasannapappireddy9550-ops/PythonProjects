print("student grade calculator using python")
student_name=input("enter student name:")
marks=[]
for i in range(1,6):
    mark=int(input(f"enter marks for subject{i}:"))
    marks.append(mark)
    total=0
    for i in marks:
        total=total+i
print("total marks:",total)
average=total/len(marks)
print("avetage:",average)


print("student name:",student_name)


if average >=90:
    print("grade A")
elif average>=75:
    print("grade B")
elif average>=60:
    print("grade C")
elif average>=40:
    print("grade D")
else:
    print("grade F")


if average >=40:
    print("Pass")
else:
    print("Fail")















'''subject1=(int(input("enter marks in subject 1:")))
subject2=(int(input("enter marks in subject 2:")))
subject3=(int(input("enter marks in subject 3:")))
subject4=(int(input("enter marks in subject 4:")))
subject5=(int(input("enter marks in subject 5:")))
total=subject1+subject2+subject3+subject4+subject5
average=total/5

print("student name:",student_name)
print("total marks:",total)
print("average marks:",average)


if average >=90:
    print("grade A")
elif average>=75:
    print("grade B")
elif average>=60:
    print("grade C")
elif average>=40:
    print("grade D")
else:
    print("grade F")


if average >=40:
    print("Pass")
else:
    print("Fail")'''






