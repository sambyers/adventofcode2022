from day3_p1 import input_text, get_priority


# https://adventofcode.com/2022/day/3

example = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

def get_rucksacks(s):
    partial_sacks = s.split()
    list_o_sacks = []
    while 0 < len(partial_sacks):
        list_o_sacks.append(partial_sacks[:3])
        partial_sacks = partial_sacks[3:]
    return list_o_sacks

def get_common_letter(l):
    return [t for t in l[0] if t in l[1] and t in l[2]][0]

if __name__ == "__main__":
    rs = get_rucksacks(input_text)
    p_sum = 0
    for s in rs:
        badge = get_common_letter(s)
        p = get_priority(badge)
        p_sum += p
    print(p_sum)