print("---Student Data System---")
name =input("Enter Student Name:")
roll_no=int(input("Enter Student Roll Number:"))
age=int(input("Enter Student Age:"))
marks=int(input("Enter Student Marks:"))
is_pass=marks>=40

persentage=(marks/100)*100

print("\n===Student Data===")
print("Name:",name )
print("Roll No:",roll_no)
print("Age:",age)
print("Marks:",marks)
print("Is Pass:",is_pass)
print("Percentage:",percentage)
print("Result:","Pass"if is_pass else "fail")

print("\n---Data Types Used---")
print("Type of Name:",type(name))
print("Type of Roll No:",type(roll_no))
print("Type of Age:",type(age))
print("Type of Marks:",type(marks))
print("Type of Is Pass:",type(is_pass))
print("Type of Percentage:",type(percentage))