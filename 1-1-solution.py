# https://adventofcode.com/2022/day/1
import sys


def format_text_to_lists(text):
    # split text by newlines and convert to integers
    items = text.split('\n\n')
    # initialize lists
    lists = []

    # iterate over items
    for item in items:
        # split current item by newline and convert to integers
        current_items = [int(x) for x in item.split('\n') if x]

        # add current list to lists
        lists.append(current_items)

    # return result
    return lists


def find_largest_sum(lists):
    # initialize variables
    max_sum = 0
    max_list = []

    # iterate over lists
    for lst in lists:
        # calculate sum of current list
        sum = 0
        for item in lst:
            sum += item

        # update max_sum and max_list if current sum is larger
        if sum > max_sum:
            max_sum = sum
            max_list = lst

    # return result
    return max_list, max_sum


def main():
    arg = sys.argv[1]
    if arg == "-e":
        with open("1-1-example-input") as fh:
            lists_str = fh.read()
    elif arg == "-i":
        with open("1-1-input") as fh:
            lists_str = fh.read()

    lists = format_text_to_lists(lists_str)
    sum = find_largest_sum(lists)
    print(sum)


if __name__ == "__main__":
    main()
