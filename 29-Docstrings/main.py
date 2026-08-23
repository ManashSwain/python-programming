# Docstring programs
# Note : Comments can be ignored but docstings are not ignored 
# Hint: __ : double underscore

def square(a):
   '''Function for squaring the number'''
   return (a*a)

result = square(5)
print(result) # 25
# print the docstring
print(square.__doc__) # Function for squaring the number