input_file = open("input.txt", "r")

input_list = input_file.read().split("\n")

result = 0

for input in input_list:
    game_nr = int(input.split(':')[0].strip('Game '))
    possible = True
    for segment in input.split(':')[1].split(';'):
        for cube in segment.split(','):
            if cube.split(' ')[2] == 'red' and int(cube.split(' ')[1]) > 12:
                possible = False
            if cube.split(' ')[2] == 'green' and int(cube.split(' ')[1]) > 13:
                possible = False
            if cube.split(' ')[2] == 'blue' and int(cube.split(' ')[1]) > 14:
                possible = False

    if possible == True:
        result = result + game_nr

print(result)
