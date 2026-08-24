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

# Functions and meaning 

# 1. union - No repetation prints all the items from a and b without duplicates
# 2. update - updates the set with no repetition same as union but modifies the set
# 3. intersection - common items but does not modify the set
# 4. intersection_update - common between the sets and also modifies the set
# 5. symmetric_difference - Will display all the items other than common things between two sets
# 6. symmetric_difference_update - Will display all the items other than common things between two sets also modifies the set
# 7. differnce - Its like a -b what ever is common in a will not get displayed
# 8. difference_update - Its like a -b what ever is common in a will not get displayed and set will get updated
