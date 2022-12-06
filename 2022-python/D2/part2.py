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
    opponent_choice = input[:1]
    result_needed = input[-1:]
    my_choice = ''

    if result_needed == 'Y':  # Draw
        if opponent_choice == 'A':
            total_score += 1
        elif opponent_choice == 'B':
            total_score += 2
        else:
            total_score += 3
        total_score += 3
    elif result_needed == 'X':  # Lose
        if opponent_choice == 'A':
            total_score += 3
        elif opponent_choice == 'B':
            total_score += 1
        else:
            total_score += 2
        total_score += 0
    elif result_needed == 'Z':  # Win
        if opponent_choice == 'A':
            total_score += 2
        elif opponent_choice == 'B':
            total_score += 3
        else:
            total_score += 1
        total_score += 6

print(total_score)
