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