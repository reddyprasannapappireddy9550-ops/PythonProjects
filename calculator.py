print("simple calculator")
while True:
    n1= float(input("Enter first number: "))
    n2= float(input("Enter second number: "))

    print("choose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5.modulus")

 
    choice=input("enter your choice(1-5):")

    if choice=="1":
        print("ans=",n1+n2)
    elif choice=="2":
        print("ans=",n1-n2)
    elif choice=="3":
        print("ans=",n1*n2)
    elif choice=="5":
        print("ans=",n1%n2)
    elif choice =="4":
        if n2 !=0:
          print("ans=",n1/n2)
        else:
            print("cannot divide by zero.")
    else:
       print("Invalid choice.")


    again=input("want to perform another calculation?(yes/no):").lower()
    
    if again== "yes":
        print("continue calculation")

    else: 
          print("Thank you for using the calculator.")
          break
        
        










          