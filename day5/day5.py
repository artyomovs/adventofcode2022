from pathlib import Path
from pprint import pprint
import os
import time
from const import EMOJI_LIST

def read_inputs(filename):
    instructions = list()
    instructions_lines = list()
    stacks = list()
    lines = Path(filename).read_text().splitlines()
    count_of_stacks = 0


    i = 0
    for line in lines:
        if not(line):
            numbers = lines[i - 1].strip().replace("   ", ",").split(",")
            count_of_stacks = int(numbers[-1].strip())
            break
        else:
            i += 1

    for i in range(0, count_of_stacks):
        stacks.append([])

    temp_stacks = list()
    for line in Path(filename).read_text().splitlines():
        if "move" in line:
            instructions_lines.append(line)
        if "[" in line:
            temp_stacks.append(line)
    
    for s in temp_stacks:
        new_stack = s.replace("    ", "[ ]").replace("] [", "][").replace("][", "],[").replace("[ ]", "[0]").replace("]", "").replace("[", "").split(",")
        for i in range(0, len(new_stack)):
            if new_stack[i] != "0":
                stacks[i].append(new_stack[i])
            

    for command in instructions_lines:
        instruction = [int (c) for c in command.replace("move ", "").replace(" from ", ",").replace(" to ", ",").strip().split(",")]
        instructions.append(instruction)
    return stacks, instructions


def move_crate(count, _from, _to, reverse = True):
    buffer= _from[:count]
    if reverse:
        buffer.reverse()
    _to = buffer + _to
    _from = _from[count:]
    return _from, _to


def calculate_top_crates(stacks):
    result = ""
    for stack in stacks:
        if len(stack) > 0:
            result += stack[0]
    return result

def print_stacks(command, stacks, clear=True, emoji=True):
    if clear:
        clear = lambda: os.system('clear')
        clear()
    print(f"--------{command}--------")
    i = 1
    for stack in stacks:
        line = ''.join(stack)
        new_line = ''
        for symbol in line:
            new_line += get_emoji(get_code_symbol(symbol))
        line = new_line if emoji else line
        print(f"{i}: {line}")
        i+=1

def get_code_symbol(symbol):
    return ord(symbol) - 65

def get_emoji(code):
    return EMOJI_LIST[code]


def calculate(stacks, instructions, reverse=True):
    for instruction in instructions:
        count = instruction[0]
        number_from = instruction[1] - 1
        number_to = instruction[2] - 1
        _from = stacks[number_from]
        _to = stacks[number_to]
        stacks[number_from], stacks[number_to] = move_crate(count, _from, _to, reverse)
        print_stacks(f"Move {count} from {instruction[1]} to {instruction[2]}", stacks, clear=True, emoji=True)
        time.sleep(100/1000)
    return calculate_top_crates(stacks=stacks)


if __name__ == "__main__":
    stacks, instructions = read_inputs("input.txt")
    part_one_result = calculate(stacks, instructions, reverse=True)
    part_two_result = calculate(stacks, instructions, reverse=False)
    print(f"Part one result is: {part_one_result}")
    print(f"Part two result is: {part_two_result}")
