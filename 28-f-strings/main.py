# General formatting

name = "Manash"
country = "India"

sentence = "My name is {} and i am from {}"
updatedsentence = sentence.format(country,name)
print(updatedsentence) # My name is India and i am from Manash

# Note : If variable order is wrong then the flow also will be wrong
# Note Old syntax : sentence = "My name is {1} and i am from {0}" 1 and 0 are variable index order

# fstring

print(f"My name is {name} and i am from {country}") # My name is Manash and i am from India

# more formatting
txt = "For only {price:.2f} dollars"
print(txt.format(price = 49.888888)) # For only 49.89 dollars

# price formatting usinf fstrings
price = 66.7789
newtxt = f"For only {price:.2f} dollar"
print(newtxt) # For only 66.78 dollar

# Other fstring techniques

val = "Geeks"
print(f"{val} for {val} is a website for {val}") # Geeks for Geeks is a website for Geeks

print(f"value : {2*6}") # value : 12