# Basic match case

x = 8 

match x :
    case 2 :
        print("The value of x is 2")
    case 4 : 
        print("The value of x is 4")
    case 6 : 
        print("The value of x is 6")
    case 8 : 
        print("The value of x is 8")
    case _:
        print("Invalid x value")

# output : The value of x is 8

#  Advanced Match case Example


age = 20

match age :
    case 18 :
        print("Exactly 18")
    case 25 :
        print("Eactly 25")
    case _ :
        if age < 18:
            print("Minor")
        elif age < 60:
            print("Adult")
        else:
            print("Senior citizen")

# output : Adult

