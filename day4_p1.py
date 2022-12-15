# https://adventofcode.com/2022/day/4


example = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

with open("day4-input") as fh:
    input_text = fh.read()

def get_pairs(s):
    return [t.split(",") for t in s.split()]

def rangeify(l):
    for p in l:
        for s in p:
            n = s.split("-")
            p[p.index(s)] = range(int(n[0]), int(n[1]))
    return l

# For part 1, to check if ranges overlap fully
def range_fully_overlap(a, b):
    left_in_right = a.start >= b.start and a.stop <= b.stop
    right_in_left = a.start <= b.start and a.stop >= b.stop
    if left_in_right or right_in_left:
        return True
    else:
        return False

if __name__ == "__main__":
    prs = get_pairs(input_text)
    rng_list = rangeify(prs)
    sum = 0
    for r in rng_list:
            if range_fully_overlap(r[0], r[1]):
                sum += 1
    print(sum)