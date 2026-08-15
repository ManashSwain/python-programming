#String methods

# upper()

str1 = "manash"
print(str1.upper()) # MANASH

# lower()
str2 = "ARTIFICIAL"
print(str2.lower()) # artificial

# strip()
str3 = "    Hello world!     "
print(str3) #    Hello world!
print(str3.strip()) #Hello world!

# rstrip()
str4 = "Welcome to python programming !!!!"
print(str4.rstrip("!")) # Welcome to python programming 

# replace()
str5 = "Silver spoon"
print(str5.replace("sp", "m")) # Silver moon

# split()
str6 = "silver spoon"
print(str6.split(" ")) # ['silver', 'spoon']

# capitalize()
str7 = "hello world"
modstr = str7.capitalize()
print(modstr) # Hello world

str8 = "hello worLD"
modstr8 = str8.capitalize()
print(modstr8) # Hello world

# center()
str9 = "Welcome to the Console!!!"
print(str9.center(50)) #            Welcome to the Console!!! 

# Giving arguments to center
print(str9.center(50, "*")) #************Welcome to the Console!!!*************s

#count()
print(str9.count("e")) # 4

# endswith()
print(str9.endswith("!!")) # True

# check a charater within the position
print(str9.endswith("to", 4,10)) # True

# find()
# find will give occurance number 
# It will return -1 if index is not found
print(str9.find("the")) #11

#index()
# throws error if not found 
#File "/Users/manashswain/Desktop/Development/python/13-String-Methods/main.py", line 60, in <module>
#print(str9.index("con")
# ValueError: substring not found 
print(str9.index("Con")) # 15 

# isalnum()
# true only if the entire string only consists of A-Z, a-z, 0-9
str10 = "Welcome to India!!!"
print(str10.isalnum()) # False

# isalpha()
# True only if the entire string only consists of A-Z, a-z.

str11 = "Welcome"
print(str11.isalpha()) # True

# islower()
print(str11.islower()) # False

# isprintable()
print(str11.isprintable()) # True

# isspace()
str12 = "            " # can use space or tab
print(str12.isspace()) # True


# istitle()
# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
str13 = "Hello World!"
print(str13.istitle()) # True

# isupper()
str14 = "MY NAME IS MANASH"
print(str14.isupper()) # True

# startswith()
print(str14.startswith("MY")) # True

# swapcase() 
# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

str15 = "My name is John Doe"
print(str15.swapcase()) # mY NAME IS jOHN dOE

# title()
# The title() method capitalizes each letter of the word within the string. It also makes other chars as small

print(str15.title()) # My Name Is John Doe