### AdventOfCode Day 1: 
### p.1 Find the elf carrying the most calories and print the sum of them
### p.2 

# Open input file and record input as string
with open("input.txt", "r") as file:
    input_text = file.read() 

# Initialize variables for loop
text_len = len(input_text)
outer_array = []
inner_array = []
num = ''

# Iterate through characters in text
for i in range(text_len):
    # If character is a digit - append to number
    if input_text[i].isdigit():
        num = num + input_text[i]
    # Otherwise - add number to inner array
    else: 
        if num.isdigit():
            inner_array.append(int(num))
            # Clear number
            num = ''

    # Check for the end of file 
    if i+1 < text_len:
        # If find two break lines in a row - append inner array to the outer
        if input_text[i] == "\n" and input_text[i+1] == "\n":
            outer_array.append(inner_array)
            # Clear inner array
            inner_array = []

# Initialize result variable
result = 0

# Overwrite result with bigger number
for arr in outer_array:
    x = sum(arr)
    if x > result:
        result = x

# Print the biggest sum
print(result)