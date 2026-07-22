print("===== Student Record Management System =====")
print("======= MENU=====")
students=[]
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice=="1":
        student_name=input("enter student name:")
        age=int(input("enter age:"))
        course=input("enter course:")
        student={
            "name":student_name,
            "age":age,
            "course":course
    }
        students.append(student)
        print("student added successfully!")

    elif choice=="2":
            if not students:
                print("No students available")
            else:
                for student in students:
                    print("----------------------")
                    print("name:",student["name"])
                    print("age:",student["age"])
                    print("course:",student["course"])
    elif choice=="3":
        search=input("enter name to search:")
        found=False
        for student in students:
            if student["name"]==search:
                found=True
                print("name:",student["name"])
                print("age:",student["age"])
                print("course:",student["course"])
        if found==False:
            print("student not found")
    elif choice=="4":
        search_student=input("enter student name to update:")
        age=int(input("enter New age:"))
        course=input("enter New course:")
        found=False
        for student in students:
            if student["name"]==search_student:
                found=True
                student["age"]=age
                student["course"]=course
                print("student updated successfully!")
        if found==False:
            print("student not found")
    elif choice=="5":
        search_student=input("enter student name to delete:")
        found=False
        for student in students:
            if student["name"]==search_student:
                found=True
                students.remove(student)
                print("student deletion is successful")
        if found==False:
            print("student not found")
    elif choice=="6":
        print("Thank you for using Student Record Management system.")
        break
    else:
        print("invalid choice! please enter 1 to 6.")


            

                



