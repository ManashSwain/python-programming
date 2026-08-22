# Tuple methods
# Applying methods on tuple does not change the original tuple

tup1 = (12,24,65)
tup2 = ("Red","Green","Blue")

print(tup1) # (12, 24, 65)
print(type(tup1)) # <class 'tuple'>

print(tup2) # ('Red', 'Green', 'Blue')
print(type(tup2)) # <class 'tuple'>

# Tuple with different data type

tup3 = ("Rabbit", 56, True, None)
print(tup3) # ('Rabbit', 56, True, None)
print(type(tup3)) # <class 'tuple'>

# Tuple Indexing

print(tup1[0]) # 12
print(tup1[1]) # 24
print(tup1[2]) # 65

# Tuple negative indexing

tup4 = (89,43,23,56,32,65,8,2,5,28,34,65)
print(len(tup4)) # 12
print(tup4[-5]) # Total length - 5 : 12-5 = 7th index
# Output : 2