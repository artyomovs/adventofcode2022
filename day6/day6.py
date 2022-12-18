from pathlib import Path

def if_line_uniq(line):
    return len(set(line)) == len(line)

def get_first_marker(line):
    i = 0
    for i in range(4, len(line)):
        if if_line_uniq(line[i-4:i]):
            return i
    return -1

def read_input(filename):
    return Path(filename).read_text()


if __name__ == "__main__":
    line = read_input("input.txt")
    part_one_result = get_first_marker(line)
    print(part_one_result)