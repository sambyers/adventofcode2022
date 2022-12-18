from day5_p1 import puzzle_input_str, stackify, instructify, get_top_crates


def crate_mover_9001(stack_dict, instr_tuple):
    """
    CrateMover 9001
    Processes instructions to do work on the stack
    Return resulting stack dictionary
    """
    for i in instr_tuple:
        from_stk = i["from"]
        to_stk = i["to"]
        moves = i["move"]
        tmp = []
        for m in range(moves):
            tmp.append(stack_dict[from_stk].pop())
        stack_dict[to_stk].extend(reversed(tmp))
    return stack_dict

def main():
    stack_dict, instructions_str = stackify(puzzle_input_str)
    instr_tuple = instructify(instructions_str)
    result_stack_dict = crate_mover_9001(stack_dict, instr_tuple)
    print(get_top_crates(result_stack_dict))

if __name__ == "__main__":
    main()