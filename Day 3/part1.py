"""
# Rucksack Reorganization
Advent Of Code, Day 3
https://adventofcode.com/2022/day/3

## Rules

Suppose you have the following list of contents from six rucksacks:

    --------------------------------     
    vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw
    --------------------------------    
    
    - The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
    - The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
    - The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
    - The fourth rucksack's compartments only share item type v.
    - The fifth rucksack's compartments only share item type t.
    - The sixth rucksack's compartments only share item type s.

To help prioritize item rearrangement, every item type can be converted to a priority:

    - Lowercase item types a through z have priorities 1 through 26.
    - Uppercase item types A through Z have priorities 27 through 52.

In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.


## Part 1:
Find the sum of the priorities of the item types that appear in both compartments of each rucksack.

"""

# Declare sum of priorities
priorities = 0

with open("input.txt", "r") as file:
    for line in file:

        # Helper to break from loops: 
        #    "True" if item that appears in both rucksack's compartments is found
        #    "False" by default - resets on each rucksack iteration
        found = False

        # Amount of items in rucksack
        items = len(line.rstrip())

        # Go through the first rucksack's compartment
        for i in range(items // 2):

            if found == True:
                break
              
            # Go through the second rucksack's compartment
            for j in range(items // 2, items):

                if found == True:
                    break

                if line[i] == line[j]:

                    found = True

                    # Check for letter case and add priorities accordingly
                    # 1. Use "ord" method to convert character to ASCII decimal
                    # 2. Subtract number according to letter case to get proper amount of priorities
                    if line[i] == line[i].upper():
                        priorities += ord(line[i]) - 38

                    elif line[i] == line[i].lower():
                        priorities += ord(line[i]) - 96
                      

# Print sum of priorities
print(priorities)