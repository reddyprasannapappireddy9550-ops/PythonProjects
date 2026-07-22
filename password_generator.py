'''print("password generator")
import random
length=int(input("enter password length:"))
characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
password=""
count=0
while count<length:
   character=(random.choice(characters))
   password=password+character
   count=count+1
print(password)








for i in range(1,11):
   print(i)



for i in range(2,21):
   if i%2==0:
      print(i)

for i in range(2,21,2):
   print(i)


for i in range(1,6):
   print("*"* i)


marks=[]
for i in range(1,6):
   mark=int(input(f"enter marks for subject{i}:"))
   marks.append(mark)
   print(marks)'''




marks=[90,56,78,56,89]
for i in marks:
  print(i)



marks=[90,56,78,56,89]
total=0
for i in marks:
  total=total+i
print(total)
average=total/len(marks)
print(average)