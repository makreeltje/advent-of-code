from functools import reduce

input_file = open("input.txt", "r")
input_list = input_file.read().split("\n")
result = 0

rows = len(input_list)
columns = len(input_list[0])

numbers = []
for x in range(rows):
    y = 0
    while y < columns:
        if input_list[x][y].isdigit():
            start = y
            number = ""
            while y < columns and input_list[x][y].isdigit():
                number += input_list[x][y]
                y += 1
            y -= 1
            numbers.append((int(number), (x, start, y)))

        y += 1

gears = {}
for number in numbers:
    for x in range(number[1][0] - 1, number[1][0] + 2):
        if 0 <= x < rows:
            for y in range(number[1][1] - 1, number[1][2] + 2):
                if 0 <= y < columns:
                    if input_list[x][y] == "*":
                        if not gears.get((x, y)):
                            gears[(x, y)] = []
                        gears[(x, y)].append(number[0])

for gear in gears:
    if len(gears[gear]) == 2:
        product = 1
        for num in gears[gear]:
            product *= num
        result += product

print(result)


