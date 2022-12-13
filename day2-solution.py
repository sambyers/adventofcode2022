import sys


# https://adventofcode.com/2022/day/2
# A = Rock, B = Paper, C = Scissors
# X = Rock, Y = Paper, Z = Scissors
# Part two: X = lose, Y = draw, Z = win

name_dict = {
    "X": "rock", 
    "Y": "paper", 
    "Z": "scissors", 
    "A": "rock", 
    "B": "paper", 
    "C": "scissors"
    }
result_score_dict = {
    "W": 6, 
    "D": 3, 
    "L": 0
    }
shape_score_dict = {
    "X": 1, 
    "Y": 2, 
    "Z": 3, 
    }
# Returns winner of round
rpz_rules_dict = {
    "A": {"X": "D", "Y": "Y", "Z": "A"}, 
    "B": {"X": "B", "Y": "D", "Z": "Z"},
    "C": {"X": "X", "Y": "C", "Z": "D"}
    }

def rounds_str_to_list(s):
    s = s.split("\n")
    for i in range(len(s)):
        s[i] = s[i].split(" ")
    return s

def play_round(player_a, player_b, rules=rpz_rules_dict):
    # Play round against rules of game
    r = rules[player_a][player_b]
    if r == "D":
        return "D" # return draw
    else:
        return r # return winner

def score_player_b(
    winner,
    player_b,
    shape_scoring=shape_score_dict, 
    result_scoring=result_score_dict
    ):
    # Get the score player B will get for the shape they played
    shape_score = shape_scoring[player_b]
    # If player B wins, get points
    if winner == player_b:
        result_score = result_scoring["W"]
    # If draw, get points
    elif result_scoring.get(winner):
        result_score = result_scoring[winner]
    # If loss, get points
    else:
        result_score = result_scoring["L"]
    # Return shape and result sum
    return shape_score + result_score

def get_total_score_for_player_b(rounds):
    total = 0
    for r in rounds:
        player_a = r[0]
        player_b = r[1]
        winner = play_round(player_a, player_b)
        total += score_player_b(winner, player_b)
    return total

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

    list_of_game_rounds = rounds_str_to_list(games)
    total_score = get_total_score_for_player_b(list_of_game_rounds)
    print(total_score)

if __name__ == "__main__":
    main()