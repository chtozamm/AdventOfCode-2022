"""
# Camp Cleanup 
Advent Of Code, Day 4
https://adventofcode.com/2022/day/4

"""

counter = 0

with open("input.txt", "r") as file:
    for line in file:
        pair = line.rstrip().split(",")
        first_sections = pair[0].split("-")
        second_sections = pair[1].split("-")
        if int(first_sections[0]) <= int(second_sections[0]) and int(first_sections[1]) >= int(second_sections[1]):
            counter += 1
            continue
        elif int(first_sections[0]) >= int(second_sections[0]) and int(first_sections[1]) <= int(second_sections[1]):
            counter += 1
            continue

print(counter)