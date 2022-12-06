from pathlib import Path

def read_input(filename="input.txt"):
    return Path(filename).read_text().splitlines()

def if_contains(list_a, list_b):
    result = False
    if list_a[0] >= list_b[0] and list_a[-1] <= list_b[-1]:
        result = True
    elif list_b[0] >= list_a[0] and list_b[-1] <= list_a[-1]:
        result = True
    else:
        result = False
    return result

def generate_numbers(numbers):
    result = []
    for i in range(numbers[0], numbers[-1] + 1):
        result.append(i)
    return result

def if_overlap(list_a, list_b):
    set_a = set(generate_numbers(list_a))
    set_b = set(generate_numbers(list_b))
    return not(set_a.isdisjoint(set_b))

def generate_list(line):
    columns = line.split(",")
    list_a = []
    list_b = []
    numbers = columns[0].split("-")
    list_a.append(int(numbers[0]))
    list_a.append(int(numbers[1]))
    numbers = columns[1].split("-")
    list_b.append(int(numbers[0]))
    list_b.append(int(numbers[1]))
    return list_a, list_b


def part_one(lines):
    subset_count = 0
    for line in lines:
        list_a, list_b = generate_list(line)
        if if_contains(list_a, list_b):
            subset_count += 1
    print(subset_count)

def part_two(lines):
    overlaps = 0
    for line in lines:
        list_a, list_b = generate_list(line)
        if if_overlap(list_a, list_b):
            overlaps += 1
    print(overlaps)

if __name__ == "__main__":
    lines = read_input()
    part_one(lines)
    part_two(lines)