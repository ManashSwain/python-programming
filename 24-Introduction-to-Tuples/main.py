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