input_file = open("input.txt", "r")

input_list = input_file.read().split("\n")

result = 0


def read_input_for_digit(input):
    for c in input:
        if c.isdigit():
            return c


for input in input_list:
    num = ''
    num = num + read_input_for_digit(input)
    input = input[::-1]
    num = num + read_input_for_digit(input)

    result = result + int(num)

print(result)