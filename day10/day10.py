from pathlib import Path
from pprint import pprint

FILENAME = "input.txt"
MEASURE_SIGNALS = [20, 60, 100, 140, 180, 220]



CYCLES = {
    "addx": 2,
    "noop": 1
}

def read_commands(filename):
    commands = []
    lines = Path(filename).read_text().splitlines()
    for line in lines:
        command = line.split(" ")
        if len(command) == 1:
            command.append(0)
        else:
            command[1] = int(command[1])
        commands.append((command[0], command[1]))
    return commands

def get_sprite(x):
    sprite = '.'*40
    return sprite[:x] + "###" + sprite[x+3:]


def draw_crt(sprite, current_crt):
    print(len(current_crt))
    s = sprite[len(current_crt)] 
    print(f"current: {current_crt}, s: {s}")
    return current_crt + s


def print_data(cycle, sprite, crt_list):
    # crt_str = ""
    # for crt in crt_list:
    #     crt_str = crt_str + '\n' + crt

    print(f"End of cycle: {cycle}. Sprite: {sprite}.\nCRT:\n{crt_list}")

def execute_program(commands):
    register = 1
    cycles_count = 0
    strength = 0
    sprite_position = get_sprite(0)
    crt = ""
    crt_total = ""
    for direction, steps in commands:
        for i in range(0, CYCLES[direction]):
            crt = draw_crt(sprite_position, crt)
            cycles_count += 1
            print(f"current CRT:{crt}")
            print_data(cycles_count, sprite_position, crt_total)
            if cycles_count in MEASURE_SIGNALS:
                strength = strength + cycles_count * register                
            if cycles_count % 40 == 0:
                crt_total = crt_total + "\n" + crt
                crt = ""
            
    
        register += steps
        print(register)
        sprite_position = get_sprite(register-1)
        
        

        # print(f"End of cycle: {cycles_count}. sprite: {sprite_position}\ncrt:\n{crt}")
    cycles_count += 1
    crt_total = crt_total + "\n" + crt
    print_data(cycles_count, sprite_position, crt_total)

    # print(f"cycle:{cycles_count}, X:{register}, strength: {strength}")
    # print(crt_list)

if __name__ == "__main__":
    commands = read_commands(filename=FILENAME)
    execute_program(commands)
    # print(get_sprite(0))
    
