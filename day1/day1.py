from pathlib import Path

def part_one(filename="input.txt"):
    elve_calories = []
    max_calories = 0
    for line in Path(filename).read_text().splitlines():
        if not(line):
            calories = sum(elve_calories)
            max_calories = calories if calories > max_calories else max_calories
            elve_calories = []
        else:
            elve_calories.append(int(line))
    print(max_calories)


def part_two(filename="input.txt"):
    elve_sum_calories = []
    current_elve_calories = 0
    for line in Path(filename).read_text().splitlines():
        if not(line):
            elve_sum_calories.append(current_elve_calories)
            current_elve_calories = 0
        else:
            current_elve_calories += int(line)
    elve_sum_calories.sort(reverse=True)
    top_three = sum(elve_sum_calories[:3])
    print(top_three)

if __name__ == "__main__":
    part_one()
    part_two()