std_id = 102
std_name = "Ron Weasley"
add = "10 Riverside Irvine, CA"
dob = "01/01/1990"

print()

print("Student Details")
print("*" * 40)

print("Student ID: ", std_id)
print("Student Name: ", std_name)
print("Address: ", add)
print("Student Date Of Birth: ", dob)

print("+" * 40)

print()


print(type(add))

app_id = int(input("Enter your applicant ID Here: "))
print("Applicant ID is:", app_id)

app_name = str(input("Enter Applicant Name Here: "))
print("Applicant name is: ", app_name)

print(type(app_id))
print(type(app_name))

# Variable Names
#***********************
# Variable declaration and Initialization
# Identifier
# State
# Operand 

# Value
# Literal 

# Data Types 
# int
# String 
# float 
# boolean 
# Tuple
# List 

# The Building Block of python Program:
# 1. Variables  
# 2. Functions 
# 3. Optional Statements 

def triangle(lentgh = 3, breath = 2, height = 4):
    return lentgh * breath * height


res = triangle()
print("The area of the above triangle is: ", res, "cm")

t1 = triangle(5, 6, 1)
print("The area of the triangle is: ", t1)

t2 = triangle(12, 4, 3)
print("The area of a triangle whose sides are 12cm, 4cm, 3cm is: ", t2, "cm")