# General formatting

name = "Manash"
country = "India"

sentence = "My name is {} and i am from {}"
updatedsentence = sentence.format(country,name)
print(updatedsentence) # My name is India and i am from Manash

# Note : If variable order is wrong then the flow also will be wrong
# Note Old syntax : sentence = "My name is {1} and i am from {0}" 1 and 0 are variable index order