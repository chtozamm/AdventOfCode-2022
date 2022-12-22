"""
# Rock, Paper, Scissors tournament
Advent Of Code, Day 2
https://adventofcode.com/2022/day/2

## Rules

The winner of the whole tournament is the player with the highest score. 
Your total score is the sum of your scores for each round. 
The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Opponent's move, My move | Points
------------------------------------     
A, X - rock              | 1 point
B, Y - paper             | 2 points
C, Z - scissors          | 3 points
------------------------------------     


Result | Points
-------------------
win    | 6 points
draw   | 3 point
loss   | 0 points
-------------------

## Part 1:
Print your total score according to tournament log (input.txt).

"""

# Open file
with open("input.txt", "r") as file:

    # Variable declarations 
    my_points = 0

    rock = 1
    paper = 2
    scissors = 3

    win = 6
    draw = 3
    loss = 0

    # Go through each round
    for line in file:

        # Declare variables for moves
        opponent_move = line[0]
        my_move = line[2]

        # Update my score accordingly
        if opponent_move == "A":
            if my_move == "X":
                my_points += draw + rock
            elif my_move == "Y":
                my_points += win + paper
            elif my_move == "Z":
                my_points += loss + scissors

        elif opponent_move == "B":
            if my_move == "X":
                my_points += loss + rock
            elif my_move == "Y":
                my_points += draw + paper
            elif my_move == "Z":
                my_points += win + scissors

        elif opponent_move == "C":
            if my_move == "X":
                my_points += win + rock
            elif my_move == "Y":
                my_points += loss + paper
            elif my_move == "Z":
                my_points += draw + scissors

    # Print total score
    print(my_points)