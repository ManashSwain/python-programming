# Manipulating tuples
# Hint : Convert to list then apply list methods and then convert to tuple 

nums = (12,23,45,87,54)
converted = list(nums)
print(type(nums)) # <class 'tuple'>
print(type(converted)) # <class 'list'>
converted.append(777)
nums = tuple(converted)
print(nums) # (12, 23, 45, 87, 54, 777)