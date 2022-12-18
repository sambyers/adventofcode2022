from sys import argv
from pprint import pprint

with open(argv[1]) as fh:
    puzzle_input_str = fh.read()

def cmds_to_dict(s):
    """
    Cmds to a flat dictionary with nesting represented as pointers
    """
    cmd_list = s.split("\n")
    dir_stack = []
    result_dict = {}
    for cmd in cmd_list:
        cmd_substrs = cmd.split()
        # Change dir or return to last dir, preserve last dir
        if cmd_substrs[1] == "cd":
            if cmd_substrs[2] == "..":
                dir_stack.pop()
            else:
                dir_stack.append(cmd_substrs[2])
                unique_name = "_".join(dir_stack)
                result_dict[unique_name] = {}
        # Make new dict of files and dirs
        elif cmd_substrs[1] == "ls":
            result_dict["_".join(dir_stack)] = {"files": [], "dirs": [], "size": 0}
        # Add files to current dir
        elif cmd_substrs[0].isnumeric():
            result_dict["_".join(dir_stack)]["files"].append({
                "name": cmd_substrs[1], 
                "size": int(cmd_substrs[0]),
            })
            result_dict["_".join(dir_stack)]["size"] += int(cmd_substrs[0])
        # Add a dir to current dir
        elif cmd_substrs[0] == "dir":
            unique_name = "_".join(dir_stack)
            result_dict["_".join(dir_stack)]["dirs"].append({
                "name": f"{unique_name}_{cmd_substrs[1]}"
            })
    # Add size of nested dirs into dir size
    for k, v in result_dict.items():
        for dir in v["dirs"]:
            result_dict[k]["size"] += result_dict[dir["name"]]["size"]
    return result_dict

def sum_directories(directories, threshold=100000):
    result = 0
    for d in directories.values():
        size = d["size"]
        if size <= threshold:
            result += size
    return result

def main():
    d = cmds_to_dict(puzzle_input_str)
    # pprint(d, indent=4, width=100)
    print(sum_directories(d))

if __name__ == "__main__":
    main()