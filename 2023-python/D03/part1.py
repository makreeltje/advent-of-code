input_file = open("input.txt", "r")
input_list = input_file.read().split("\n")
result = 0

rows = len(input_list)
columns = len(input_list[0])

numbers = []
for x in range(rows):
    y = 0
    while y < columns:
        if input_list[x][y].isdecimal():
            start = y
            number = ""
            while y < columns and input_list[x][y].isdigit():
                number += input_list[x][y]
                y += 1
            y -= 1
            numbers.append((int(number), (x, start, y)))

        y += 1

for number in numbers:
    part_number = False
    for x in range(number[1][0] - 1, number[1][0] + 2):
        if 0 <= x < rows:
            for y in range(number[1][1] - 1, number[1][2] + 2):
                if 0 <= y < columns:
                    if not (input_list[x][y].isdigit() or input_list[x][y] == "."):
                        part_number = True
                        result += number[0]
                        break
            if part_number:
                break

print(result)