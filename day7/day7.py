from pathlib import Path
from pprint import pprint
import graphviz
import time


FILENAME = "input.txt"
SIZE_LIMIT = 100000
TOTAL_DISK = 70000000
SPACE_NEED = 30000000
GLOBAL_SIZE = 0
ROOT_SIZE = 0
NEED_TO_FREE = 0
DIR_SIZES = []


def read_inputs(filename):
    return Path(filename).read_text().splitlines()

def get_file_options(line):
    attrs = line.split(" ")

    file_size = int(attrs[0])
    file_name = attrs[1]
    return file_name, file_size

def get_dir_name(line, cd=False):
    if cd:
        return line.split()[2]
    else:
        return line.split()[1]


def get_type_of_command(line):
    if "$ ls" in line:
        return "ls"
    elif "dir " in line:
        return "dir"
    if "$ cd .." in line:
        return "up"
    elif "$ cd " in line:
        return "cd"
    else:
        return "file"

def add_to_tree(tree, path, variable):
    key_path = []
    for p in path:
        key_path.append(p.__repr__())
    key_template = f"[{']['.join(key_path)}]"
    code = f"tree{key_template}.update({variable})"
    exec(code)
    return tree


def create_files_tree(lines):
    tree = {"root":{}}
    path = ["root"]
    for line in lines[2:]:
        command_type = get_type_of_command(line)
        if command_type == "file":
            file_name, file_size = get_file_options(line)
            variable = {file_name: {"size": file_size, "type":"file"}}
            tree = add_to_tree(tree, path, variable)
        elif command_type == "dir":
            variable = {get_dir_name(line): {}}
            tree = add_to_tree(tree, path, variable)
        elif command_type == "cd":
            dir_name = get_dir_name(line, cd=True)
            path.append(dir_name)
        elif command_type == "up":
            path.pop()
    return tree

def is_file(value):
    return "size" in value.keys()
        

def get_directory_size(key, tree):
    global GLOBAL_SIZE
    global ROOT_SIZE
    global NEED_TO_FREE
    global DIR_SIZES
    size = 0
    for k, v in tree.items():
        if is_file(v):
            size += v["size"]
        else:
            size = size + get_directory_size(k, v)
    if key != "root":
        # print(f"{key} size: {size}")
        if size <= SIZE_LIMIT:
            GLOBAL_SIZE += size
        DIR_SIZES.append(size)
    else:
        ROOT_SIZE = size
    return size

def get_directory_to_delete(sizes):
    sizes.sort()
    for dir_size in sizes:
        if dir_size >= NEED_TO_FREE:
            print("dir_size")
            return dir_size


def draw_graph(tree, root, diagram):
    for k,v in tree.items():
        if not(is_file(v)):
            diagram.edge(root, k)
            diagram.render("tree")
            diagram.view() 
            time.sleep(0.2)           
            draw_graph(v, k, diagram)
        


if __name__ == "__main__":
    lines = read_inputs(FILENAME)
    tree = create_files_tree(lines)
    get_directory_size("root", tree['root'])
    NEED_TO_FREE = SPACE_NEED - (TOTAL_DISK - ROOT_SIZE)
    part_one_result = GLOBAL_SIZE
    part_two_result = get_directory_to_delete(DIR_SIZES)
    print("\U0001f600")
    print(f"Need to free: {NEED_TO_FREE}. Part one: {part_one_result}. Part two result: {part_two_result}")
    diagram = graphviz.Digraph('unix', filename='tree.gv', format="png", node_attr={'color': 'lightblue2', 'style': 'filled'})
    diagram.attr(size='6,6')
    diagram.node("/")
    diagram.render("tree")
    diagram.view()
    time.sleep(2)
    draw_graph(tree["root"], root="/", diagram=diagram)
    diagram.view()
    