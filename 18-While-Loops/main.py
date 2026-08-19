# Basic while loop

count = 0 
while(count<10):
    print(count)
    count = count + 1

# output
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# while loop with else 
# if condition in while fails it goes to else
# while and else should be in same level

score = 0 
while(score <10):
    print("score =",score)
    score = score + 1
else :
    print("Invalid score")

# output 

# score = 0
# score = 1
# score = 2
# score = 3
# score = 4
# score = 5
# score = 6
# score = 7
# score = 8
# score = 9
# Invalid score