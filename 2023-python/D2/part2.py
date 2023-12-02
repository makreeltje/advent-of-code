input_file = open("input.txt", "r")

input_list = input_file.read().split("\n")

result = 0

for input in input_list:

    red = 0
    green = 0
    blue = 0

    for segment in input.split(':')[1].split(';'):
        for cube in segment.split(','):
            if cube.split(' ')[2] == 'red' and int(cube.split(' ')[1]) > red:
                red = int(cube.split(' ')[1])
            if cube.split(' ')[2] == 'green' and int(cube.split(' ')[1]) > green:
                green = int(cube.split(' ')[1])
            if cube.split(' ')[2] == 'blue' and int(cube.split(' ')[1]) > blue:
                blue = int(cube.split(' ')[1])

    result = result + (red * green * blue)

print(result)
