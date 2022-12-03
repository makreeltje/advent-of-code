input_file = open("input.txt", "r")

input_calories = input_file.read().split("\n")

current = 0

every_elves_calories = []

for input in input_calories:
    if input == "":
        every_elves_calories.append(current)
        current = 0
    else:
        current += int(input)

every_elves_calories.sort()

top_three = 0

for i in every_elves_calories[-3:]:
    top_three += i

print(top_three)