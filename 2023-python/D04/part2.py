input_file = open("input.txt", "r")
input_list = input_file.read().split("\n")
result = len(input_list)

def process_list(input):
    temp_list = []
    for x in input:
        filtered = x.split(':')[1]
        segments = filtered.split('|')
        drawn_numbers = segments[0].split(' ')
        winning_numbers = segments[1].split(' ')

        while ("" in drawn_numbers):
            drawn_numbers.remove("")

        while ("" in winning_numbers):
            winning_numbers.remove("")

        j = 1
        for dn in drawn_numbers:
            try:
                i = winning_numbers.index(dn)
            except ValueError:
                continue
            if i is not None:
                if input_list.index(x) + j <= len(input_list):
                    temp_list.append(input_list[input_list.index(x) + j])
                    j += 1
    return temp_list


temp_list = process_list(input_list)

while len(temp_list) > 0:
    result += len(temp_list)
    temp_list = process_list(temp_list)
    print(len(temp_list))

print(result)
