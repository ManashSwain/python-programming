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
print(modstr). # Hello world

str8 = "hello worLD"
modstr8 = str8.capitalize()
print(modstr8) # Hello world