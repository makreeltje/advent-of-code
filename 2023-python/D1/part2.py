import time

start_time = time.time()

input_file = open("input.txt", "r")

input_list = input_file.read().split("\n")

start_time_after_import = time.time()

result = 0


def read_input_for_digit(input):
    for c in input:
        if c.isdigit():
            return c


def replace_word_for_digit(input):
    replace = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': '4',
        'five': '5e',
        'six': '6',
        'seven': '7n',
        'eight': 'e8t',
        'nine': 'n9e',
    }

    for k, v in replace.items():
        input = input.replace(k, v)

    return input


for input in input_list:

    input = replace_word_for_digit(input)
    num = ''
    num = num + read_input_for_digit(input)
    input = input[::-1]
    num = num + read_input_for_digit(input)

    result = result + int(num)

print(result)

end_time = time.time()

print("Import time in ms: ", (start_time_after_import - start_time) * 1000)
print("Execution time in ms: ", (end_time - start_time_after_import) * 1000)