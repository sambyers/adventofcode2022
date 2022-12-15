from day4_p1 import input_text, get_pairs, rangeify


# https://adventofcode.com/2022/day/4

# For part 2, to check if ranges overlap at all
def range_overlap(a, b):
    return a.start <= b.stop and a.stop >= b.start

if __name__ == "__main__":
    prs = get_pairs(input_text)
    rng_list = rangeify(prs)
    sum = 0
    for r in rng_list:
            if range_overlap(r[0], r[1]):
                sum += 1
    print(sum)