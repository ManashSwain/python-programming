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

# Fibonacci series 

# f0 = 0
# f1 = 1
# f2 = f1 +f 0
# f3 = f2 + f1

def fib(n):
    print("H")
    if(n==0):
        return 0
    if(n==1):
        return 1

    return fib(n-2) + fib(n-1)

result = fib(5)
print(result) # 5

# Explanantion
# 1st Iteration : fib(3) + fib(4)
# 2nd Iteration : fib(3) : fib(1) + fib(2) , fib(4) : fib(2) + fib(3)
# 3rd Iteration :  fib(1) = 1 , fib(2) : fib(0) + fib(1) ,fib(2) : fib(0) + fib(1) , fib(3) : fib(1) + fib(2)
# 4th Iteration :   fib(2) : fib(0)+fib(1)
# 5th Iteration : 0, 1 

# Note : H will be printed 15 times
