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


## Part 2:
Every set of three lines in your list corresponds to a single group, but each group can have a different badge item type. So, in the above example, the first group's rucksacks are the first three lines:

    --------------------------------
    vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    --------------------------------
    
And the second group's rucksacks are the next three lines:

    --------------------------------
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw
    --------------------------------

In the first group, the only item type that appears in all three rucksacks is lowercase r; this must be their badges. In the second group, their badge item type must be Z.

Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (r) for the first group and 52 (Z) for the second group. The sum of these is 70.


Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?

"""

# Declare sum of priorities (answer)
priorities = 0

# List of all rucksacks
rucksacks = []


# Populate list of rucksacks with lines from input file
with open("input.txt", "r") as file:
    for line in file:
        rucksacks.append(line.rstrip())


# Go through each rucksack 
for rucksack in range(len(rucksacks)):

    # Check for the end of list
    if rucksack == len(rucksacks) - 2:
        break
        
    # Make sure to always start with the first rucksack of each three-Elf group
    if rucksack % 3 != 0:
        continue
        
    # Helper to break from loops: 
    #    "True" if item that appears in all three rucksacks is found
    #    "False" by default - resets on each rucksack iteration
    found = False
    
    # Go through each item in the first rucksack of three-Elf group
    for i in rucksacks[rucksack]:
        
        # Check if badge was found 
        if found == True:
            break
            
        # Go through each item in the second rucksack of three-Elf group
        for j in rucksacks[rucksack+1]:
            if found == True:
                break
            
            if i == j:
                
                # Go through each item in the thied rucksack of three-Elf group
                for k in rucksacks[rucksack+2]:
                    if found == True:
                        break

                    if i == k:

                        found = True

                        # Check for letter case and add priorities accordingly
                        # 1. Use "ord" method to convert character to ASCII decimal
                        # 2. Subtract number according to letter case to get proper amount of priorities
                        if i == i.upper():
                            priorities += ord(i) - 38
    
                        elif i == i.lower():
                            priorities += ord(i) - 96            

        
# Print sum of priorities
print(priorities)