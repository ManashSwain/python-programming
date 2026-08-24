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
cities.intersection_update(cities2)
print(cities) # {'Bangalore'}