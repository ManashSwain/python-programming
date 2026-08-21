colors = ["Red","Blue","Green","Orange","Pink"]
nums = [12,43,2,67,45,76]

# sort method 
# Default sort is in ascending order 
print(colors.sort())
print(colors) # ['Blue', 'Green', 'Orange', 'Pink', 'Red']

print(nums.sort())
print(nums) # [2, 12, 43, 45, 67, 76]

# Sorting in descending order
print(colors.sort(reverse=True))
print(colors) # ['Red', 'Pink', 'Orange', 'Green', 'Blue']

print(nums.sort(reverse=True))
print(nums) # [76, 67, 45, 43, 12, 2]

# reverse method
# Reverse the list

nums1 = [43,23,65,123,7,3]
print(nums1.reverse())
print(nums1) # [3, 7, 123, 65, 23, 43]

names = ["Rohit", "Aakash", "Vinay", "Virat"]
print(names.reverse())
print(names) # ['Virat', 'Vinay', 'Aakash', 'Rohit']

# index method
# Will return the index of first occurance

print(names.index("Aakash")) # 2

# count method
# count will return no of occurance of the particular element
nums2 = [1,1,3,5,6,7,7,7,7,7,8,8,5]
print(nums2.count(7)) # 5

# copy method
# creates a new copy of the list
# modifying one will not affect the original array 

copylist = nums2.copy()
print(copylist) # [1, 1, 3, 5, 6, 7, 7, 7, 7, 7, 8, 8, 5]

# append method()
# Will add items to end of the list

Items = ["Bob", "Marley", "John"]
Items.append("Manash")
print(Items) # ['Bob', 'Marley', 'John', 'Manash']

# insert method 
# insert will insert at the particular index

Items.insert(1,"John")
print(Items) # ['Bob', 'John', 'Marley', 'John', 'Manash']

# extend method()
# This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

mycolors = ["Violet","Indigo","Blue"]
rainbow = ["Green","Yellow","Orange","Red"]
mycolors.extend(rainbow)
print(mycolors) # ['Violet', 'Indigo', 'Blue', 'Green', 'Yellow', 'Orange', 'Red']

lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = lst1 + lst2
print(lst3) # [1, 2, 3, 4, 5, 6]

# List methods

# 1. sort()
# 2. sort(reverse=True)
# 3. reverse()
# 4. index()
# 5. count()
# 6. copy()
# 7. append()
# 8. insert()
# 9. extend()
# 10. + (concat)