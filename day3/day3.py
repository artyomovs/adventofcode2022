from pathlib import Path

GROUP_SIZE = 3
def get_symbol_number(symbol):
    if symbol.islower():
        return ord(symbol) - 96
    else:
        return ord(symbol) - 38


def read_input(filename="input.txt"):
    return Path(filename).read_text().splitlines()


def get_common_symbols(lists, count=2):
    total_list = []
    total_set = []
    common_symbols = []
    for l in lists:
        total_list.extend(list(set(l)))

    total_set = set(total_list)
    for symbol in total_set:
        if total_list.count(symbol) >= count:
            common_symbols.append(symbol)
    return common_symbols

def get_sum_of_symbols(symbols):
    sum = 0
    for symbol in symbols:
        sum += get_symbol_number(symbol)
    return sum

def part_one(lines):
    sum = 0
    for line in lines:
        middle_index = int((len(line)) / 2)
        common_symbols = get_common_symbols([line[:middle_index], line[middle_index:]], 2)
        sum += get_sum_of_symbols(common_symbols)
    print(sum)

def part_two(lines):
    group_counter = 0
    group_lists = []
    sum = 0
    for line in lines:
        group_counter += 1
        group_lists.append("".join(line))
        if group_counter == 3:
            common_symbols = get_common_symbols(group_lists, 3)
            sum += get_sum_of_symbols(common_symbols)
            group_counter = 0
            group_lists = []
    print(sum)



if __name__ == "__main__":
    part_one(read_input())
    part_two(read_input())