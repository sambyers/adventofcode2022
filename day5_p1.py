from collections import deque
from sys import argv

with open(argv[1]) as fh:
    puzzle_input_str = fh.read()

def stackify(str):
    """
    Return stacks as dictionary of deque
    Ex. {1: deque(['[N]', '[D]', '[M]', '[Q]', '[B]', '[P]', '[Z]', '[V]'])}
    """
    stacks_str, moves_str = str.split("\n\n")
    stacks_list = stacks_str.split("\n")
    stacks_list_nums = stacks_list.pop(-1).split()

    stacks_dict = {}
    for n in range(len(stacks_list_nums)):
        stacks_dict[n+1] = deque()
    
    interval = 4
    for line in reversed(stacks_list):
        current_stack = 0
        left, right = 0, 3
        
        while right <= len(line):
            current_stack += 1
            item = line[left:right]
            if "[" in item:
                stacks_dict[current_stack].append(item)
            left += interval
            right += interval
    return stacks_dict, moves_str

def instructify(str):
    """Return string instructions as tuple of dictionaries"""
    instr_list = str.split("\n")
    result_list = []
    for instr in instr_list:
        moves_list = instr.split()
        instr_dict = {
            moves_list[0]: int(moves_list[1]),
            moves_list[2]: int(moves_list[3]),
            moves_list[4]: int(moves_list[5]),
            }
        result_list.append(instr_dict)
    return tuple(result_list)

def crate_mover_9000(stack_dict, instr_tuple):
    """
    CrateMover 9000
    Processes instructions to do work on the stack
    Return resulting stack dictionary
    """
    for i in instr_tuple:
        from_stk = i["from"]
        to_stk = i["to"]
        moves = i["move"]
        for m in range(moves):
            stack_dict[to_stk].append(stack_dict[from_stk].pop())
    return stack_dict

def get_top_crates(d):
    return "".join([v[-1] for v in d.values()]).replace("[", "").replace("]", "").replace(" ", "")

def main():
    stack_dict, instructions_str = stackify(puzzle_input_str)
    instr_tuple = instructify(instructions_str)
    result_stack_dict = crate_mover_9000(stack_dict, instr_tuple)
    print(get_top_crates(result_stack_dict))

if __name__ == "__main__":
    main()