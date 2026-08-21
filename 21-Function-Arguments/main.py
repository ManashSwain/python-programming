# Function Arguments

# Basic function

def addTwo(a,b):
    print(a+b)

num1 = 2
num2 = 4

addTwo(num1,num2)

# Output 
# 6

# Dafault arguments
# If not all arguments are  default then default argument should come at last
# Note : All the arguments can also be default

def average(a, b=7):
    print(((a+b)/2))

average(3)

# Output
# 5.0

def average2(b, a=4):
    print(((a+b)/2))

average2(3)

# Output 
# 3.5

def fullname(fname, lname, mname="F"):
    print("Hello", fname , mname ,lname)

fullname("john", "keneddy")