# List
# Note : List are like arrays

marks = [24,56,77]
print(marks) # [24, 56, 77]

# Accessing Individual values
print(marks[0]) # 24
print(marks[1]) # 56
print(marks[2]) # 77

# List can store different data type in same list variable

values = [21 ,"Hello", True]
print(values) # [21, 'Hello', True]

# Working with negative index 
# Trick : add len(variable) - index to it

nums = [12,46,734,567,35,56]

print(nums[-3]) # 567
print(nums[len(nums)-3]) # 567

# To check whether a item is present or not
# Hint: Use if/else along with in 

mylist = [23,"Manash",True,4.5,"Python"]

if "Manash" in mylist:
    print("True")
else:
    print("False")

# Output 
# True

animals = ["Cat","Dog","Rat","Mouse","Lion","Tiger","Elephant"]

# Print all values 
print(animals) # ['Cat', 'Dog', 'Rat', 'Mouse', 'Lion', 'Tiger', 'Elephant']
print(animals[:]) # ['Cat', 'Dog', 'Rat', 'Mouse', 'Lion', 'Tiger', 'Elephant']

# Print in a particular Range
# Hint start index will include and end index will not include

print(animals[2:6]) # ['Rat', 'Mouse', 'Lion', 'Tiger']

# Print every second character / print alternate character

print(animals[::2]) #['Cat', 'Rat', 'Lion', 'Elephant']
# Note Last argument is step index or jump index

# List Comprehension in Python
# Syntax : new_list = [expression for item in iterable]

allNumbers = [1,2,3,4,5,6,7,8,9]
outputnum = [i*i for i in allNumbers]
print(outputnum) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

