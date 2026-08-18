# For loop

name = "Manash"

for i in name:
    print(i)

# output : 
# M
# a
# n
# a
# s
# h


cars = ["Audi", "BMW", "Benz"]

for i in cars:
    print(i)

# output

# Audi
# BMW
# Benz

# Iterating individual strings in list

for car in cars:
    for i in car:
        print(i)

# Output 
# A
# u
# d
# i
# B
# M
# W
# B
# e
# n
# z

# Range (Print 0-4)

for k in range(5):
 print(k)

# oputput 

# 0
# 1
# 2
# 3
# 4

for k in range(5):
   print(k+1)

# output 
# 1
# 2
# 3
# 4
# 5

# Range with limits

for k in range(4,8):
   print(k)

# Output

# 4
# 5
# 6
# 7

# Range with steps (step = 2 means prints every 2nd character)

for k in range(1,10,2):
   print(k)

# Output 

# 1
# 3
# 5
# 7
# 9