# Manipulating tuples
# Hint : Convert to list then apply list methods and then convert to tuple 

nums = (12,23,45,87,54)
converted = list(nums)
print(type(nums)) # <class 'tuple'>
print(type(converted)) # <class 'list'>
converted.append(777)
nums = tuple(converted)
print(nums) # (12, 23, 45, 87, 54, 777)


# Count method

nums2 = (1,1,1,1,1,2,2,2,3,4,)
print(nums2.count(2)) # 3

# index method
print(nums2.index(2)) # 5

# index in a particular range
print(nums2.index(1,3,5)) # 3

