import numpy as np

input_file = open("input.txt", "r")
input_list = input_file.read().split("\n")
result = 0

v_array = []

for input in input_list:
    h_array = []
    for c in input:
        h_array.append(c)
    v_array.append(h_array)

for i in v_array:
    for j in i:
        if j.isdigit():
            print(j, end=" ")
        if j != '.' and not j.isdigit():
            print(j, end=" ")

    print()