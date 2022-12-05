from pathlib import Path

SHAPE_SCORES = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

POSITIONS = {
    "win": ["AY", "BZ", "CX"],
    "lose": ["AZ", "BX", "CY"],
    "draw": ["AX", "BY", "CZ"]
}

SIGNS = {"X": "lose", "Y": "draw", "Z": "win"}

def get_shape_score(shape):
    return SHAPE_SCORES[shape]

def get_position_score(step):
    if step in POSITIONS["win"]:
        return 6
    elif step in POSITIONS["lose"]:
        return 0
    else:
        return 3

def get_round_end(sign):
    return SIGNS[sign]

def get_result_score(sign, end):
    for position in POSITIONS[end]:
        if position[0] == sign:
            score = get_shape_score(position[1])
            if end == "win":
                position_score = 6
            elif end == "lose":
                position_score = 0
            else:
                position_score = 3
            # print(f"{position} {sign} {end}: {score} + {position_score}")
            return score + position_score

def part_one(filename="input.txt"):
    scores = 0
    for line in Path(filename).read_text().splitlines():
        scores = scores + get_shape_score(line[-1]) + get_position_score(line.replace(" ", ""))
    return scores

def part_two(filename="input.txt"):
    scores = 0
    for line in Path(filename).read_text().splitlines():
        round_end = get_round_end(line[-1])
        sign = line[0]
        scores += get_result_score(sign, round_end)
    return scores



if __name__ == "__main__":
    print(f"Part one result: {part_one()}")
    print(f"Part two result: {part_two()}")