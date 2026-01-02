import time

my_time=int(input("Enter the time in seconds for countdown: "))

for i in range(0, my_time):
    print(my_time-i)
    time.sleep(1)

print("TIME'S UP!")