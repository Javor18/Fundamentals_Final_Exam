leave_time = input().split(":")

steps = int(input())
time_for_step = int(input())

hours = int(leave_time[0])

minutes = int(leave_time[1])

seconds = int(leave_time[2])

for i in range(steps):

    seconds += time_for_step

    if seconds >= 60:

        seconds -= 60
        minutes += 1

    if minutes >= 60:

        minutes -= 60
        hours += 1

    if hours == 24:

        hours = 00

print(f"Time Arrival: {hours}:{minutes}:{seconds}")