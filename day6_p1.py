from sys import argv


with open(argv[1]) as fh:
    puzzle_input_str = fh.read()

def main():
    left, right = 0, 14 # Num of distinct chars, 4 -> 14
    while right < len(puzzle_input_str):
        window = puzzle_input_str[left:right]
        char_counts = {char:0 for char in window}
        for char in window:
            char_counts[char] += 1
        sum = 0
        for char, count in char_counts.items():
            sum += count
        if len(char_counts.keys()) == sum:
            print(right)
            break
        left += 1
        right += 1

if __name__ == "__main__":
    main()