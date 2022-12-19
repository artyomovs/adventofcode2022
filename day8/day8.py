from pathlib import Path
import sys

FILENAME = "input.txt"

class TreeData:
    def __init__(self, forest, forest_height, forest_width, tree_x, tree_y, tree_height):
        self.forest = forest
        self.forest_height = forest_height
        self.forest_width = forest_width
        self.tree_x = tree_x
        self.tree_y = tree_y
        self.tree_height = tree_height
        self.neighbors_stack = []
        self.visible = False
        self.edge = False
        self.visibility_score = 0

    def find_neighbors(self, delta_y, delta_x):
        i = self.tree_y
        j = self.tree_x
        neighbors = []
        while (i != 0) and (i != self.forest_height - 1) and (j != 0) and (j != self.forest_width - 1):
            i += delta_y
            j += delta_x
            neighbors.append(self.forest[i][j])
        return neighbors

    def get_neighbors_stack(self):
        self.neighbors_stack.append(self.find_neighbors(1, 0))
        self.neighbors_stack.append(self.find_neighbors(-1, 0))
        self.neighbors_stack.append(self.find_neighbors(0, 1))
        self.neighbors_stack.append(self.find_neighbors(0, -1))

    def is_edge(self):
        if self.tree_x == 0 or \
            self.tree_y == 0 or \
            self.tree_y == self.forest_height - 1 or \
            self.tree_x == self.forest_width - 1:
            self.edge = True
        else:
            self.edge = False
        return self.edge

    def is_visible(self):
        for neighbors in self.neighbors_stack:
            neighbors.sort()
            if neighbors[-1] < self.tree_height:
                self.visible = True
                return self.visible
        self.visible = False
        return self.visible

    def get_visibility_score_one_direction(self, delta_y, delta_x):
        visibility_score = 0
        i = self.tree_y
        j = self.tree_x
        while (i != 0) and (i != self.forest_height - 1) and (j != 0) and (j != self.forest_width - 1):
            i += delta_y
            j += delta_x
            visibility_score += 1                
            if self.forest[i][j] >= self.tree_height:
                break
        return visibility_score

    def get_visibility_score(self):
        self.visibility_score = \
        self.get_visibility_score_one_direction(1, 0) * \
        self.get_visibility_score_one_direction(-1, 0) * \
        self.get_visibility_score_one_direction(0, 1) * \
        self.get_visibility_score_one_direction(0, -1)


def read_input(filename):
    return Path(filename).read_text().splitlines()


def find_visible_trees(lines):
    visible_trees = 0
    max_visibility_score = 0 
    width = len(lines[0])
    height = len(lines)
    for y in range(0, height):
        for x in range(0, width):
            tree = TreeData(lines, height, width, x, y, lines[y][x])
            if tree.is_edge():
                visible_trees +=1
            else:
                tree.get_neighbors_stack()                    
                if tree.is_visible():
                    visible_trees += 1

            tree.get_visibility_score()
            if tree.visibility_score > max_visibility_score:
                max_visibility_score = tree.visibility_score
    return visible_trees, max_visibility_score


def convert_to_int(lines):
    new_array = []
    for line in lines:
        new_array.append([int(i) for i in line])
    return new_array

if __name__ == "__main__":
    lines = convert_to_int(read_input(FILENAME))
    part_one_result, part_two_result = find_visible_trees(lines)
    print(f"Part one (visible trees): {part_one_result}.\nPart two(max visibility score): {part_two_result}")
