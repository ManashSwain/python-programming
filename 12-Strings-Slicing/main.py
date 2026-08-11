#string slicing methods

mystr = "HelloWorld!"

#length method
print(len(mystr))

#Slicing methods
#start - includes
#end  - does not include

print(mystr[0:4]) # Hell
print(mystr[2:5]) # llo
print(mystr[:7])  # HelloWo
print(mystr[3:]) # loWorld!


#Negative index
print(mystr[-3]) 
# Hint : just add length before negative Eg len(mystr) - 3

print(mystr[-6:-3])

#Looping through strings

alphabets = 'ABCDEFG'

for i in alphabets:
    print(i)
