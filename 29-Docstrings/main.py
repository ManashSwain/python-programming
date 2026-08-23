# Docstring programs
# Note : Comments can be ignored but docstings are not ignored 
# Hint: __ : double underscore
# Docstring should be written write below the function definition or on the first line within the function 

def square(a):
   '''Function for squaring the number'''
   return (a*a)

result = square(5)
print(result) # 25
# print the docstring
print(square.__doc__) # Function for squaring the number

# PEP 8
# In terminal open python repl and just write import this a poem will be displayed