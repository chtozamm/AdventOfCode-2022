"""
# Calorie Counting 
Advent Of Code, Day 1
https://adventofcode.com/2022/day/1

## Rules

The list below represents the Calories of the food carried by five Elves:

    The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
    The second Elf is carrying one food item with 4000 Calories.
    The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
    The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
    The fifth Elf is carrying one food item with 10000 Calories.

------------------------------------
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
------------------------------------

## Part 1:
Find the Elf carrying the most Calories.

## Part 2:
Find the sum of total calories of three biggest bags

"""

# Open file and record input as string
with open("input.txt", "r") as file:
    input_text = file.read() 

# Declare variables
text_len = len(input_text)
all_bags = []
bag = []
num = ''
most_calories = 0
unsorted_bags = []

# Go through characters in text
for i in range(text_len):

    # If character is digit - append to number
    if input_text[i].isdigit():
        num = num + input_text[i]

    else: 
        if num.isdigit():

            # Add number to bag
            bag.append(int(num))

            # Clear number
            num = ''

    # Check for end of file 
    if i+1 < text_len:

        # If two break lines in a row - append bag to array of all bags
        if input_text[i] == "\n" and input_text[i+1] == "\n":
            all_bags.append(bag)

            # Clear bag
            bag = []

# Update most calories
for arr in all_bags:
    x = sum(arr)
    unsorted_bags.append(x)
    if x > most_calories:
        most_calories = x

# Sort bags
bags_sorted = sorted(unsorted_bags)

# Print the sum of top three bags
print(bags_sorted[-1] + bags_sorted[-2] + bags_sorted[-3])