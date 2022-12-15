import sys


# https://adventofcode.com/2022/day/2
# A = Rock, B = Paper, C = Scissors
# X = Rock, Y = Paper, Z = Scissors
# Part two: X = lose, Y = draw, Z = win

name_dict = { 
    "A": "rock", 
    "B": "paper", 
    "C": "scissors"
    }

result_dict = {
    "X": "L", 
    "Y": "D", 
    "Z": "W",
}

result_score_dict = {
    "W": 6, 
    "D": 3, 
    "L": 0
    }

shape_score_dict = {
    "rock": 1, 
    "paper": 2, 
    "scissors": 3, 
    }

rules = {
    "rock": {
        "beats": "scissors",
        "loses_to": "paper"
    },
    "paper": {
        "beats": "rock",
        "loses_to": "scissors"
    },
    "scissors": {
        "beats": "paper",
        "loses_to": "rock"
    }
}

def score_round(choice1, choice2, rules):
  if choice1 == choice2:
    return 3
  elif rules[choice1]["beats"] == choice2:
    return 6
  else:
    return 0

def rounds_str_to_list(s):
    s = s.split("\n")
    for i in range(len(s)):
        s[i] = s[i].split(" ")
    return s

def score(rounds):
    score = 0
    round = 0
    for r in rounds:
        
        opponent_choice_name = name_dict[r[0]]
        target_result = result_dict[r[1]]

        if target_result == "W":
            my_choice = rules[opponent_choice_name]["loses_to"]
            result_score = result_score_dict["W"]
        elif target_result == "L":
            my_choice = rules[opponent_choice_name]["beats"]
            result_score = result_score_dict["L"]
        elif target_result == "D":
            result_score = result_score_dict["D"]
            my_choice = opponent_choice_name

        shape_score = shape_score_dict[my_choice]
        score += shape_score + result_score
        round += 1
    return score


def main():
    # -i means use the puzzle input
    # -e means use example puzzle input
    arg = sys.argv[1]
    if arg == "-e":
        with open("day2-example-input") as fh:
            games = fh.read()
    elif arg == "-i":
        with open("day2-input") as fh:
            games = fh.read()

    print(score(rounds_str_to_list(games)))

if __name__ == "__main__":
    main()