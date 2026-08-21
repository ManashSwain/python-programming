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