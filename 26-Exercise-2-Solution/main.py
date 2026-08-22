import time

hour = int(time.strftime("%H"))
minute = int(time.strftime("%M"))
seconds = int(time.strftime("%S"))

print(hour)
print(minute)
print(seconds)

if((hour >= 0) & (hour<=11)):
    print("Good Morning Sir!")
elif((hour >= 12) & ( hour <= 17)):
    print("Good Evening Sir!")
else:
    print("Good Night!")

# Note:  Output will vary based on the time
