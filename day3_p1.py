# https://adventofcode.com/2022/day/3


example = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

with open("day3-input") as fh:
    input_text = fh.read()

def get_priority(t):
    if t.islower():
        # 97 is a, 122 is z in ASCII
        # 96 is the number to subtract to get priority
        return ord(t) - 96
    elif t.isupper():
        # 65 is A, 90 is Z in ASCII
        # 38 is the num to subtract to get priority
        return ord(t) - 38

if __name__ == "__main__":

    ans = input("Example (e) or puzzle input (i)? ")
    if ans == "e":
        input_list = example.split()
    elif ans == "i":
        input_list = input_text.split()

    p_sum = 0
    for i in input_list:
        mid = int(len(i) / 2)
        item_1 = i[:mid]
        item_2 = i[mid:]
        same = [t for t in item_1 if t in item_2][0]
        p = get_priority(same)
        p_sum += p
    print(p_sum)