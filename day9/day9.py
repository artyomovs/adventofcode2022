"""
Unfortunately, didn't manage to solve it my way and 
copypasted code from this repo: GalaxyInfernoCodes/Advent_Of_Code_2022/.
Sorry for that. Maybe will come back later and try to finish.
"""

from pathlib import Path
from pprint import pprint
import numpy as np

FILENAME = "input.txt"
TAIL_POINTS = []
ARR_WIDTH = 500
ARR_HEIGHT = 500

def read_input(filename):
    return Path(filename).read_text().splitlines()
    #  [line.split(" ") for line in lines]

def create_initial_array(width, height, symbol):
    arr = []
    for i in range(0, height+1):
        line = []
        for j in range(0, width+1):
            line.append(symbol)
        arr.append(line)
    return arr


def print_array(arr):
    # arr.reverse()
    tmp_arr = list(arr)
    tmp_arr.reverse()
    print("--------------")
    for line in tmp_arr:
        print(''.join(line))

def parse_command(commands):
    return [(entry.strip().split(' ')[0],int(entry.strip().split(' ')[1])) for entry in commands]


def get_coords(command, y, x):
    direction = command[0]
    steps = int(command[1])
    coords = []
    delta_y = 0
    delta_x = 0

    if direction == "R":
        delta_x = 1
    elif direction == "U":
        delta_y = 1
    elif direction == "D":
        delta_y = -1
    elif direction == "L":
        delta_x = -1

    for i in range(0, steps):
        y = y + delta_y
        x = x + delta_x
        coords.append([y, x])
    return coords


def step(arr, head_y, head_x, tail_y, tail_x):
    global TAIL_POINTS
    # arr = create_initial_array(ARR_HEIGHT, ARR_WIDTH, ".")
    arr[head_y][head_x] = "H"
    arr[tail_y][tail_x] = "T"
    TAIL_POINTS.append(f"{tail_y},{tail_x}")
    return arr


def move_head(arr, commands):
    i = 0
    head_y = 0
    head_x = 0
    tail_y = 0
    tail_x = 0

    for command in commands:
        i += 1
        print(f"{i}/{len(commands)}")
        coords = get_coords(command, head_y, head_x)
        # print(command)
        for point in coords:

            if tail_far(point[0], point[1], tail_y, tail_x):
                tail_y = head_y
                tail_x = head_x          

            head_y = point[0]
            head_x = point[1]
            arr = step(arr, head_y, head_x, tail_y, tail_x)
            # tail_far(head_y, head_x, tail_y, tail_x)
            # print(f"head_y: {head_y}, head_x: {head_x}, tail_y: {tail_y}, tail_x: {tail_x}")
            # if point != coords[-1]:    
            #     tail_y = head_y
            #     tail_x = head_x
            # print_array(arr)
        

def tail_far(head_y, head_x, tail_y, tail_x):
    print(f"diag {head_y}, {head_x}, {tail_y}, {tail_x}")
    a = abs(head_x - tail_x)
    b = abs(head_y - tail_y)
    print(f"{a}, {b}")
    if abs(head_x - tail_x) > 1 or (head_y - tail_y) > 1:
        print("tail_far")
        return True
    else:
        return False


def update_head(head, direction):
    if direction == 'R':
        head[1] += 1
    elif direction == 'L':
        head[1] -= 1
    elif direction == 'U':
        head[0] += 1
    elif direction == 'D':
        head[0] -= 1
    return head

def update_tail(head, tail):
    difference = head - tail
    change_for_tail={
        # head is 2 up 1 right from tail, then tail follows up and right once
        (2, 1):(1, 1),
        # 1 up, 2 right
        (1, 2):(1, 1),
        # 2up
        (2, 0):(1, 0),
        # 2up 1left
        (2, -1):(1, -1),
        # 1up, 2eft
        (1, -2):(1, -1),
        # 2left
        (0, -2):(0, -1),
        (-1, -2):(-1,-1),
        (-2, -1):(-1, -1),
        (-2, 0):(-1, 0),
        (-2, 1):(-1, 1),
        (-1, 2):(-1, 1),
        (0, 2):(0, 1),
        # additional cases for part 2
        (2, 2):(1, 1),
        (-2, -2):(-1, -1),
        (-2, 2):(-1, 1),
        (2, -2):(1, -1)
      }
    new_tail_pos = tail + np.array(change_for_tail.get(tuple(difference), (0,0)))
    return new_tail_pos

if __name__ == "__main__":
    tail = np.array([0,0])
    head = np.array([0,0])

    tail_positions = set([tuple(tail)])


    commands = parse_command(read_input(FILENAME))

    for direction, steps in commands:
        while steps > 0:
            head = update_head(head, direction)
            steps -= 1
            tail = update_tail(head, tail)
            tail_positions.add(tuple(tail))
    print(len(tail_positions))


    rope = [np.array([0,0]) for _ in range(10)]

    tail_positions = set([tuple(rope[9])])
    for direction, steps in commands:
        while steps > 0:
            rope[0] = update_head(rope[0], direction)
            steps -= 1
            for i in range(1, len(rope)):
                rope[i] = update_tail(rope[i-1], rope[i])
            tail_positions.add(tuple(rope[9]))
    print(len(tail_positions))

    # for comm

    # arr =create_initial_array(ARR_HEIGHT, ARR_WIDTH, ".")
    # arr[0][0] = "H"
    # # print_array(arr)
    
    # move_head(arr, commands)
    # print(set(TAIL_POINTS))
    # part_one_result = len(set(TAIL_POINTS))
    # print(f"Part one result is {part_one_result}")

    # # delta_y, delta_x = get_delta(commands[1])
    # # print(f"delta_y: {delta_y}, delta_x: {delta_x}")


    # tail_points = set([tuple(tail)])
    # for command in commands
