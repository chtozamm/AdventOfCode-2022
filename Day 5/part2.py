"""
# Supply Stacks
Advent Of Code, Day 5
https://adventofcode.com/2022/day/5

Part 2

"""

# Declare lists for stacks
stack1 = []
stack2 = []
stack3 = []
stack4 = []
stack5 = []
stack6 = []
stack7 = []
stack8 = []
stack9 = []

with open("input.txt", "r") as file:
    for line in file:

        # Break after reading stack
        if line[1] in ("o", "1"):
            break

        # Populate stack 1
        if len(line) > 1:
            if line[1] != " ":
                stack1.append(line[1])
        # Populate stack 2
        if len(line) > 1:
            if line[5] != " ":
                stack2.append(line[5])
        # Populate stack 3
        if len(line) > 1:
            if line[9] != " ":
                stack3.append(line[9])
        # Populate stack 4
        if len(line) > 1:
            if line[13] != " ":
                stack4.append(line[13])
        # Populate stack 5
        if len(line) > 1:
            if line[17] != " ":
                stack5.append(line[17])
        # Populate stack 6
        if len(line) > 1:
            if line[21] != " ":
                stack6.append(line[21])
        # Populate stack 7
        if len(line) > 1:
            if line[25] != " ":
                stack7.append(line[25])
        # Populate stack 8
        if len(line) > 1:
            if line[29] != " ":
                stack8.append(line[29])
        # Populate stack 9
        if len(line) > 1:
            if line[33] != " ":
                stack9.append(line[33])
                

# Reverse items in lists to match stacks
stack1 = list(reversed(stack1))
stack2 = list(reversed(stack2))
stack3 = list(reversed(stack3))
stack4 = list(reversed(stack4))
stack5 = list(reversed(stack5))
stack6 = list(reversed(stack6))
stack7 = list(reversed(stack7))
stack8 = list(reversed(stack8))
stack9 = list(reversed(stack9))

# Declare and populate list of all stacks
stacks = []
for stack in (stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9):
    stacks.append(stack)


with open("input.txt", "r") as file:
    for line in file:

        # Skip reading stacks
        if line[0] != "m":
            continue

        # Check whether amount of crates to move is one- or two- digit int 
        if line[5].isdigit() and line[6].isdigit():
            crates_amount = int(line[5] + line[6])
            stack_from = int(line[13])
            stack_to = int(line[18])

            # Take group of crates from one stack and move to another
            temp = []
            for i in range(crates_amount):
                crate = stacks[stack_from - 1].pop()
                temp.insert(0, crate)
            stacks[stack_to - 1] += temp

        elif line[5].isdigit():
            crates_amount = int(line[5])
            stack_from = int(line[12])
            stack_to = int(line[17])

            # Take group of crates from one stack and move to another
            temp = []
            for i in range(crates_amount):
                crate = stacks[stack_from - 1].pop()
                temp.insert(0, crate)
            stacks[stack_to - 1] += temp

        else:
            print("Invalid amount of crates.")


# Declare answer and populate with top crates of each stack
answer = ""
for stack in stacks: 
    answer += stack[-1]


print(answer)