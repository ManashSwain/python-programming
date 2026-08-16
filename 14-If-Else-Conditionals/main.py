# if statement

marks = 56
if(marks > 49):
    print("Result : Passed!")

# output : Result : Passed!

# if else statement

age = 18

if(age >= 18):
    print("You can drive")
else: 
    print("You cannot drive")

# output : You can drive

# if -- elif --else
amount = 350

if(amount >= 700):
    print("Amount is greater or equal to 700")
elif(amount >= 350):
    print("Amount is greater or equal to 350")
else: 
    print("Amount is not in the given condition")

# output : Amount is greater or equal to 350

# Nested conditionals

username = "johndoe"
password = "john123"

if(username == "johndoe"):
    if(password == "john123"):
        print("Authenticated")
    else:
        print("Password is incorrect")
else:
    print("Invalid username")

# output : Authenticated