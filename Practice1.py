# A program to give the grades to a student 

marks=int(input("Enter the marks of the student here:"))

if marks >=90:
    grade="A"
elif marks>=75 :
    grade="B"
elif marks>=50:
    grade="C"
else: 
    grade="B"
    print("Your grade is"  + grade)
