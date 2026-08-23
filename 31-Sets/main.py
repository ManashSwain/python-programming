# sets 
# Note : There is no guarantee on the order

items = {"Pickle", 34 , 89.44 , True, None}
print(items) # {None, True, 34, 'Pickle', 89.44}
print(type(items)) # <class 'set'>

# Accessing set elements

for i in items:
    print(i)

# Output : 
# None
# True
# 34
# Pickle
# 89.44

# Note : Order will be different always

# Quiz

newset = {}
print(type(newset)) # <class 'dict'>

# Note : Type of empty set is dict

newset = set()
print(type(newset)) # <class 'set'>

# Note : To create empty set use set() function