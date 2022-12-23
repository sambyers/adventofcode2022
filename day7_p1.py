from sys import argv
from pprint import pprint

class Directory():
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.child_directories = []
        self.child_files = []
        self.capacity = 70000000

    @property
    def size(self):
        if hasattr(self, "_size"):
            return self._size
        size = 0
        if len(self.child_files) > 0:
            for file in self.child_files:
                size += file.size
        if len(self.child_directories) > 0:
            for dir in self.child_directories:
                size += dir.size
        self._size = size
        return self._size
    
    @property
    def utilization(self):
        return round((self.size / self.capacity)*100, 2)
    
    @property
    def free(self):
        return self.capacity - self.size

    def add_file(self, file):
        self.child_files.append(file)

    def add_dir(self, dir):
        self.child_directories.append(dir)

    def __repr__(self):
        return f"Directory({self.name})"

    def __str__(self):
        return (
            f"[ Directory: Name: {self.name}, "
            f"Child Directories: {len(self.child_directories)}, "
            f"Child Files: {len(self.child_files)} ]"
        )

class File():
    def __init__(self, name, parent, size) -> None:
        if not isinstance(size, int): raise ValueError("Size is not int.")
        self.name = name
        self.parent = parent
        self.size = size

    def __repr__(self):
        return f"File({self.name}, {self.size})"

def walk_to_root(dir):
    while dir.parent:
        dir = dir.parent
    return dir

# Depth first search on the tree to find sum of dirs <= threshold.
def sum_dirs_with_threshold(tree, threshold, node=None, visited=None):
    if visited is None:
        visited = []
    if node is None:
        node = tree
    if not hasattr(tree, "p1_answer"):
        tree.p1_answer = 0
    if node not in visited and isinstance(node, Directory):
        if node.size <= threshold:
            # Store sum of dirs in p1_solution property of root tree obj
            tree.p1_answer += node.size
        visited.append(node)
        for dir in node.child_directories:
            sum_dirs_with_threshold(tree, threshold, node=dir, visited=visited)
    return tree

# Depth first search on the tree to find smallest
# dir to free up enough space for the update
def find_rm_candidate(tree, update_size, node=None, visited=None):
    if visited is None:
        visited = []
    if node is None:
        node = tree
    if not hasattr(tree, "p2_answer"):
        tree.p2_answer = None
    if node not in visited and isinstance(node, Directory):
        potential_space = tree.free + node.size
        if potential_space >= update_size:
            if not tree.p2_answer:
                tree.p2_answer = node
            elif tree.p2_answer and tree.p2_answer.size > node.size:
                tree.p2_answer = node
        visited.append(node)
        for dir in node.child_directories:
            find_rm_candidate(tree, update_size, node=dir, visited=visited)
    return tree
    
def cmds_to_tree(lines_str):
    lines_list = lines_str.split("\n")
    curr_dir = None
    for line in lines_list:
        line_substrs = line.split()
        # CD command
        if "$" in line_substrs[0] and "cd" in line_substrs[1]:
            # Up a dir
            if ".." in line_substrs[2]:
                curr_dir = curr_dir.parent
            # Into a dir
            else:
                dir_name = line_substrs[2]
                new_dir = Directory(dir_name, curr_dir)
                if not curr_dir is None:
                    curr_dir.add_dir(new_dir)
                curr_dir = new_dir
        # File
        elif line_substrs[0].isnumeric():
            file_size = int(line_substrs[0])
            file_name = line_substrs[1]
            child_file = File(file_name, curr_dir, file_size)
            curr_dir.add_file(child_file)
    return walk_to_root(curr_dir)

def main():
    with open(argv[1]) as fh:
        puzzle_input_str = fh.read()
    tree = cmds_to_tree(puzzle_input_str)
    print(f"Total size: {tree.size}")
    tree = sum_dirs_with_threshold(tree, 100000)
    print("Answer 1:", tree.p1_answer)
    update_size = 30000000
    tree = find_rm_candidate(tree, update_size)
    print("Answer 2:", tree.p2_answer.name, tree.p2_answer.size)
    # 7951177 is too high


if __name__ == "__main__":
    main()