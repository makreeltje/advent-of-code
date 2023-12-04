input_file = open("input.txt", "r")
input_list = input_file.read().split("\n")
result = 0



for x in input_list:
    filtered = x.split(':')[1]
    segments = filtered.split('|')
    drawn_numbers = segments[0].split(' ')
    winning_numbers = segments[1].split(' ')

    while ("" in drawn_numbers):
        drawn_numbers.remove("")

    while ("" in winning_numbers):
        winning_numbers.remove("")

    card_score = 0

    for dn in drawn_numbers:
        try:
            i = winning_numbers.index(dn)
        except ValueError:
            continue
        if i != None:
            if card_score == 0:
                card_score += 1
            else:
                card_score = card_score * 2

    result += card_score

print(result)


