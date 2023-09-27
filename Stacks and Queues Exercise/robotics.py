from collections import deque
import datetime

robot = deque(x for x in input().split(';'))
print(robot)
robot.rotate(1)
print(robot)
starting_time = input()

products = []

while True:
    command = input()

    if command == 'End':
        break

    hh, mm, ss = starting_time.split(':')
    time = int(hh) * 3600 + int(mm) * 60 + int(ss)
    current_time = time + 1

    result = robot.popleft().split('-')
    current_robot = result[0]
