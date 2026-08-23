# Recursion in python

def factorial(n):
    if ((n==0) | (n==1)):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3)) # 6

# Explanantion

# 1st Iteration : 3 * factorial(2)
# 2nd iteration : 3 * 2 * factorial(1)
# 3rd iteration : 3 * 2 * 1 = 6