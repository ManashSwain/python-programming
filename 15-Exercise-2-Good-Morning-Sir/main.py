import time 

currenttime = time.strftime("%H:%M:%S")
get_hour = int(time.strftime("%H"))

if(get_hour < 12):
    print("Good Morning!")
elif((get_hour >= 12) & (get_hour<= 18)):
    print("Good Evening")
else:
    print("good Night!")