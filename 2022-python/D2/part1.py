# A/X = Rock = 1
# B/Y = Paper = 2
# C/Z = Scissor = 3
# Won = 6
# Draw = 3
# Lost = 0

input_file = open("input.txt", "r")

input_result = input_file.read().split("\n")

total_score = 0

for input in input_result:
    my_choice = input[-1:]
    opponents_choice = input[:1]

    if my_choice == 'X':
        total_score += 1
    elif my_choice == 'Y':
        total_score += 2
    elif my_choice == 'Z':
        total_score += 3

    if my_choice == 'X' and opponents_choice == 'C' or my_choice == 'Y' and opponents_choice == 'A' or my_choice == 'Z' and opponents_choice == 'B':
        total_score += 6
    elif my_choice == 'X' and opponents_choice == 'B' or my_choice == 'Y' and opponents_choice == 'C' or my_choice == 'Z' and opponents_choice == 'A':
        total_score += 0
    elif my_choice == 'X' and opponents_choice == 'A' or my_choice == 'Y' and opponents_choice == 'B' or my_choice == 'Z' and opponents_choice == 'C':
        total_score += 3

print(total_score)
