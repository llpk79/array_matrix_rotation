import pprint
from random import randint

m = [[randint(1, 50) for _ in range(10)] for x in range(1, 100, 10)]


def rot_right(arr):
    arr_len = len(arr)
    new = []
    for _ in range(arr_len):
        new.append([0] * arr_len)
    x = arr_len - 1
    for i in range(arr_len):
        j = 0
        while j < arr_len:
            new[j][x] = arr[i][j]
            j += 1
        x -= 1
    return new


def rot_right_in_place(arr):
    arr_len = len(arr) - 1
    row, column = 0, 0
    while row <= arr_len // 2:
        temp = arr[column][arr_len - row]
        arr[column][arr_len - row] = arr[row][column]
        temp2 = arr[arr_len - row][arr_len - column]
        arr[arr_len - row][arr_len - column] = temp
        temp = arr[arr_len - column][row]
        arr[arr_len - column][row] = temp2
        arr[row][column] = temp
        if column == arr_len - row - 1:
            row += 1
            column = row - 1
        column += 1
    return arr

pprint.pprint(m)

r = rot_right(m)


pprint.pprint(r)


pprint.pprint((rot_right_in_place(m)))

print(rot_right(m) == rot_right_in_place(m))
