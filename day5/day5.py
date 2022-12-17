from pathlib import Path
from pprint import pprint



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
        new_stack = s.replace(" [", "[").replace("] ", "]").replace("   ", "[ ]").replace("][", ",").replace("[", "").replace("]", "").replace(" ", "0").split(",")
        for i in range(0, len(new_stack)):
            if new_stack[i] != "0":
                stacks[i].append(new_stack[i])
    pprint(stacks)
            

    for command in instructions_lines:
        instruction = [int (c) for c in command.replace("move ", "").replace(" from ", ",").replace(" to ", ",").strip().split(",")]
        instructions.append(instruction)
    return stacks, instructions


if __name__ == "__main__":
    stack, instructions = read_inputs("input.txt")
    pprint(stack)
    pprint(instructions)