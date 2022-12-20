"""
RULES

The winner of the whole tournament is the player with the highest score. 
Your total score is the sum of your scores for each round. 
The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

A X - rock     | 1 point
B Y - paper    | 2 points
C Z - scissors | 3 points

win  - 6 points
draw - 3 point
loss - 0 points

"""

# Read the input
with open("input.txt", "r") as file:
    #lines = file.read()
    #print(lines[2])
    for line in file:
        print(line)
        print(line[0]) # prints opponents move
        print(line[2]) # prints my move
        break