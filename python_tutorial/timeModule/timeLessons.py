from time import *

countdown_start = int(input("Enter a starting number: "))
countdown = countdown_start

while countdown > 0:
    print(countdown)
    countdown -= 1
    sleep(1)
print("Your countdown finished after: ", countdown_start, "Seconds!")

from time import *

file_size = int(input("What is the file size in megabits: "))
internet_speed = int(input("What is your internet speed in megabits/seconds: "))

file_size *= 8
download_time = file_size/internet_speed

print("Time to complete download is: ", round(download_time,1), "Seconds")

countdown = round(download_time)
while countdown > 0:
    print(countdown)
    countdown -= 1
    sleep(1)
print("Download completed!")