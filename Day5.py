def add_op(i, array):
    index1, index2, index3 = array[i + 1], array[i + 2], array[i + 3]
    if array[i] == 1:
        array[index3] = array[index1] + array[index2]
    elif array[i] == 101:
        array[index3] = index1 + array[index2]
    elif array[i] == 1001:
        array[index3] = array[index1] + index2
    elif array[i] == 1101:
        array[index3] = index1 + index2


def multiply_op(i, array):
    index1, index2, index3 = array[i + 1], array[i + 2], array[i + 3]
    if array[i] == 2:
        array[index3] = array[index1] * array[index2]
    elif array[i] == 102:
        array[index3] = index1 * array[index2]
    elif array[i] == 1002:
        array[index3] = array[index1] * index2
    elif array[i] == 1102:
        array[index3] = index1 * index2


def output_op(i, array):
    index = array[i + 1]
    if array[i] == 4:
        return array[index]
    elif array[i] == 104:
        return index


def jump_if_true(i, array):
    index1, index2 = array[i + 1], array[i + 2]
    if array[i] == 5:
        if array[index1] != 0:
            return array[index2]
    elif array[i] == 105:
        if index1 != 0:
            return array[index2]
    elif array[i] == 1105:
        if index1 != 0:
            return index2
    elif array[i] == 1005:
        if array[index1] != 0:
            return index2
    return None


def jump_if_false(i, array):
    index1, index2 = array[i + 1], array[i + 2]
    if array[i] == 6:
        if array[index1] == 0:
            return array[index2]
    elif array[i] == 106:
        if index1 == 0:
            return array[index2]
    elif array[i] == 1106:
        if index1 == 0:
            return index2
    elif array[i] == 1006:
        if array[index1] == 0:
            return index2
    return None


def less_than(i, array):
    index1, index2, index3 = array[i + 1], array[i + 2], array[i + 3]
    if array[i] == 7:
        if array[index1] < array[index2]:
            array[index3] = 1
        else:
            array[index3] = 0
    elif array[i] == 107:
        if index1 < array[index2]:
            array[index3] = 1
        else:
            array[index3] = 0
    elif array[i] == 1107:
        if index1 < index2:
            array[index3] = 1
        else:
            array[index3] = 0
    elif array[i] == 1007:
        if array[index1] < index2:
            array[index3] = 1
        else:
            array[index3] = 0


def equals(i, array):
    index1, index2, index3 = array[i + 1], array[i + 2], array[i + 3]
    if array[i] == 8:
        if array[index1] == array[index2]:
            array[index3] = 1
        else:
            array[index3] = 0
    elif array[i] == 108:
        if index1 == array[index2]:
            array[index3] = 1
        else:
            array[index3] = 0
    elif array[i] == 1108:
        if index1 == index2:
            array[index3] = 1
        else:
            array[index3] = 0
    elif array[i] == 1008:
        if array[index1] == index2:
            array[index3] = 1
        else:
            array[index3] = 0


def intcode_computer(arr):
    """
    Modified version of the method in Day 2. Added opcodes and modes
    Part 1: added opcodes 3 and 4. Input is 5, Output is 12440243
    Part 2: added opcodes 5 to 8. Input is 5, Output is 15486302
    """
    input_int = 5
    n = 0
    while n < len(arr):
        s = str(arr[n])
        if s[-1] == '1':
            add_op(n, arr)
            n += 4
        elif s[-1] == '2':
            multiply_op(n, arr)
            n += 4
        elif s == '3':
            index = arr[n + 1]
            arr[index] = input_int
            n += 2
        elif s[-1] == '4':
            print(output_op(n, arr))
            n += 2
        elif s[-1] == '5':
            instruction = jump_if_true(n, arr)
            if instruction is not None:
                n = instruction
            else:
                n += 3
        elif s[-1] == '6':
            instruction = jump_if_false(n, arr)
            if instruction is not None:
                n = instruction
            else:
                n += 3
        elif s[-1] == '7':
            less_than(n, arr)
            n += 4
        elif s[-1] == '8':
            equals(n, arr)
            n += 4
        elif s == '99':
            return


# Retrieving the numbers
f = open('inputs/day5.txt', 'r')
int_code_1 = []
for line in f:
    line = line.strip('\n').split(',')
    for num in line:
        int_code_1.append(int(num))
f.close()

# intcode_computer(int_code_1)
