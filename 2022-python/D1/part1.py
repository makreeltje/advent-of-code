input_file = open("input.txt", "r")

input_calories = input_file.read().split("\n")

current_highest = 0

current = 0

for input in input_calories:
    if input == "":
        if (current > current_highest):
            current_highest = current
        current = 0
    else:
        current += int(input)

print(current_highest)