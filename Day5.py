def add_op(i, array):
    index1 = array[i + 1]
    index2 = array[i + 2]
    index3 = array[i + 3]
    if len(str(array[i])) == 3:
        array[index3] = index1 + array[index2]
    elif len(str(array[i])) == 4:
        if array[i] == 1001:
            array[index3] = array[index1] + index2
        elif array[i] == 1101:
            array[index3] = index1 + index2
    else:
        array[index3] = array[index1] + array[index2]


def multiply_op(i, array):
    index1 = array[i + 1]
    index2 = array[i + 2]
    index3 = array[i + 3]
    if len(str(array[i])) == 3:
        array[index3] = index1 * array[index2]
    elif len(str(array[i])) == 4:
        if array[i] == 1002:
            array[index3] = array[index1] * index2
        elif array[i] == 1102:
            array[index3] = index1 * index2
    else:
        array[index3] = array[index1] * array[index2]


def output_op(i, array):
    index = array[i + 1]
    if len(str(array[i])) == 3:
        print(index)
    else:
        print(array[index])


def jump_if_true(i, array):
    index1 = array[i + 1]
    if array[i] == 1105:
        if index1 != 0:
            return True
    else:
        if array[index1] != 0:
            return True
    return False


def jump_if_false(i, array):
    index1 = array[i + 1]
    if array[i] == 1106:
        if index1 == 0:
            return True
    else:
        if array[index1] == 0:
            return True
    return False


def less_than(i, array):
    index1 = array[i + 1]
    index2 = array[i + 2]
    index3 = array[i + 3]
    if len(str(array[i])) == 3:
        if index1 < array[index2]:
            array[index3] = 1
        else:
            array[index3] = 0
    elif len(str(array[i])) == 4:
        if array[i] == 1107:
            if index1 < index2:
                array[index3] = 1
            else:
                array[index3] = 0
        elif array[i] == 1007:
            if array[index1] < index2:
                array[index3] = 1
            else:
                array[index3] = 0
    else:
        if array[index1] < array[index2]:
            array[index3] = 1
        else:
            array[index3] = 0


def equals(i, array):
    index1 = array[i + 1]
    index2 = array[i + 2]
    index3 = array[i + 3]
    if len(str(array[i])) == 3:
        if index1 == array[index2]:
            array[index3] = 1
        else:
            array[index3] = 0
    elif len(str(array[i])) == 4:
        if array[i] == 1108:
            if index1 == index2:
                array[index3] = 1
            else:
                array[index3] = 0
        elif array[i] == 1008:
            if array[index1] == index2:
                array[index3] = 1
            else:
                array[index3] = 0
    else:
        if array[index1] == array[index2]:
            array[index3] = 1
        else:
            array[index3] = 0


def intcode_computer(arr):
    """
    Modified version of the method in Day 2. Added opcodes and modes
    Part 1: added opcodes 3 and 4. Input is 5, Output is 12440243
    Part 2: added opcodes 5 to 8.
    """
    input_int = 0
    n = 0
    while n < len(arr):
        print(arr)
        s = str(arr[n])
        if len(s) > 1:
            if s[-2:] == '01':
                add_op(n, arr)
                n += 4
            elif s[-2:] == '02':
                multiply_op(n, arr)
                n += 4
            elif s[-2:] == '04':
                output_op(n, arr)
                n += 2
            elif s[-2:] == '05':
                if jump_if_true(n, arr):
                    n = arr[n + 2]
                else:
                    n += 3
            elif s[-2:] == '06':
                if jump_if_false(n, arr):
                    n = arr[n + 2]
                else:
                    n += 3
            elif s[-2:] == '07':
                less_than(n, arr)
                n += 4
            elif s[-2:] == '08':
                equals(n, arr)
                n += 4
            elif s[-2:] == '99':
                return
        else:
            if arr[n] == 1:
                add_op(n, arr)
                n += 4
            elif arr[n] == 2:
                multiply_op(n, arr)
                n += 4
            elif arr[n] == 3:
                index = arr[n + 1]
                arr[index] = input_int
                n += 2
            elif arr[n] == 4:
                output_op(n, arr)
                n += 2
            elif arr[n] == 5:
                if jump_if_true(n, arr):
                    n = arr[n + 2]
                else:
                    n += 3
            elif arr[n] == 6:
                if jump_if_false(n, arr):
                    n = arr[n + 2]
                else:
                    n += 3
            elif arr[n] == 7:
                less_than(n, arr)
                n += 4
            elif arr[n] == 8:
                equals(n, arr)
                n += 4


# Retrieving the numbers
f = open('inputs/day5.txt', 'r')
int_code_1 = []
for line in f:
    line = line.strip('\n').split(',')
    for num in line:
        int_code_1.append(int(num))
f.close()

x = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
intcode_computer(x)
