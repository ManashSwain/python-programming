# set methods
# union method

s1 = {1,2,5,6}
s2 = {2,3,7}
print(s1.union(s2)) # {1, 2, 3, 5, 6, 7}

# update method
s3 = {1,2,5,7}
s4 = {2,3,7}
print(s3.update(s4))
print(s3) # {1, 2, 3, 5, 7}
print(s4) # {2, 3, 7}

# Note : Difference between union and update is union creates a new set where as update modifies the existing set

# Intersection 

cities = {"Chennai", "Bangalore", "Noida" , "coimbatore"}
cities2 = {"Bangalore", "nagpur", "kochi"}
print(cities.intersection(cities2)) # {'Bangalore'}

# Intersection update method

cities.intersection_update(cities2)
print(cities) # {'Bangalore'}

# Symmetric difference method

animals = {"cat", "dog", "rat"}
animals2 = {"cat", "elephant" , "lion"}
print(animals.symmetric_difference(animals2)) # {'rat', 'lion', 'dog', 'elephant'}


# Symmetric difference update

animals.symmetric_difference_update(animals2)
print(animals) # {'lion', 'rat', 'elephant', 'dog'}

# Differnce method

fruits1 = {"Apple", "Banana", "Melon"}
fruits2 = {"Orange", "Apple", "jackfruit"}
print(fruits1.difference(fruits2)) # {'Melon', 'Banana'}

# difference_update method

fruits1.difference_update(fruits2)
print(fruits1) # {'Melon', 'Banana'}

# isdisjoint method

n1 = {1,2,4,6}
n2 = {2,7,8}
print(n1.isdisjoint(n2)) # False

# issuperset method 
n3 = {1,2,4,6}
print(n3.issuperset(n1)) # True

# issubset Method 
print(n1.issubset(n2)) # False

# add method

m1 = {12,34,67}
m1.add(777)
print(m1) # {777, 34, 67, 12}

# update method 

m2 = {1,2,3,4}
m2.update({7,8,9}) 
print(m2) # {1, 2, 3, 4, 7, 8, 9}

m3 = {0,66,88}
m4 = {33,44}
m3.update(m4)
print(m3) # {0, 33, 66, 88, 44}

# remove method 

r1 = {55,66,77,88}
r1.remove(555)
print(r1) 

# Output :
# Traceback (most recent call last):
#   File "/Users/manashswain/Desktop/Development/python/32-Set-Methods/main.py", line 84, in <module>
#     r1.remove(555)
#     ~~~~~~~~~^^^^^
# KeyError: 555



# Functions and meaning 

# 1. union - No repetation prints all the items from a and b without duplicates
# 2. update - updates the set with no repetition same as union but modifies the set
# 3. intersection - common items but does not modify the set
# 4. intersection_update - common between the sets and also modifies the set
# 5. symmetric_difference - Will display all the items other than common things between two sets
# 6. symmetric_difference_update - Will display all the items other than common things between two sets also modifies the set
# 7. differnce - Its like a -b what ever is common in a will not get displayed
# 8. difference_update - Its like a -b what ever is common in a will not get displayed and set will get updated
# 9. isdisjoint - It will check whether the items in set1 is present in set2 or not . return boolean
# 10. issuperset - checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.
# 11. issubset - The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.
# 12. add - adds to existing set. Note : Adds only single item
# 13. update - It can add multiple items to set
# 14. remove - removes element from set if item is not present throws error






