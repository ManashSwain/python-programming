# Break and continue in loops 
# Break means break out of loop
# continue means skip the current iteration


# Break statement 
i = 0 
while(i<10):
    if(i==4):
        break
    print(i)
    i = i + 1

# output
# 0
# 1
# 2
# 3

# continue statement
# Note: continue immediately jumps back to the beginning of the while loop. 

k = 0
while(k<10):
    if(k==5):
        k = k + 1
        continue
    print(k)
    k = k + 1

# Output
# 0
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
