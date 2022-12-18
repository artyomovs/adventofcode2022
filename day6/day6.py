from pathlib import Path

def if_line_uniq(line):
    return len(set(line)) == len(line)

def get_first_marker(line, number_distinct=4):
    i = 0
    for i in range(number_distinct, len(line)):
        if if_line_uniq(line[i-number_distinct:i]):
            return i
    return -1

def read_input(filename):
    return Path(filename).read_text()


if __name__ == "__main__":
    line = read_input("input.txt")
    part_one_result = get_first_marker(line)
    part_two_result = get_first_marker(line, 14)
    print(f"Part one: {part_one_result}")
    print(f"Part two: {part_two_result}")