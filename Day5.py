def check_for_modes(array, number):
    """
    Function used to check the modes of an opcode to determine what the values of the parameters are


    """
    index1, index2 = None, None
    if number != len(array) - 1:
        if number != len(array) - 2:
            index1, index2 = array[number + 1], array[number + 2]
        else:
            index1 = array[number + 1]
    parameters = []
    s = str(array[number])
    if len(s) == 1:
        return [array[index1], array[index2]]
    elif len(s) == 3:
        return [index1, array[index2]]
    elif len(s) == 4:
        if s[1] == '1':
            parameters.extend([index1, index2])
        else:
            parameters.extend([array[index1], index2])
        return parameters


def intcode_computer(arr):
    """
    Modified version of the method in Day 2. Added opcodes and modes
    Part 1: added opcodes 3 and 4. Input is 5, Output is 12440243
    Part 2: added opcodes 5 to 8. Input is 5, Output is 15486302
    """
    input_int = 5
    n = 0
    while n < len(arr):
        parameters = check_for_modes(arr, n)
        s = str(arr[n])
        if s[-1] == '1':
            arr[arr[n + 3]] = parameters[0] + parameters[1]
            n += 4
        elif s[-1] == '2':
            arr[arr[n + 3]] = parameters[0] * parameters[1]
            n += 4
        elif s == '3':
            arr[arr[n + 1]] = input_int
            n += 2
        elif s[-1] == '4':
            print(parameters[0])
            n += 2
        elif s[-1] == '5':
            if parameters[0] != 0:
                n = parameters[1]
            else:
                n += 3
        elif s[-1] == '6':
            if parameters[0] == 0:
                n = parameters[1]
            else:
                n += 3
        elif s[-1] == '7':
            if parameters[0] < parameters[1]:
                arr[arr[n + 3]] = 1
            else:
                arr[arr[n + 3]] = 0
            n += 4
        elif s[-1] == '8':
            if parameters[0] == parameters[1]:
                arr[arr[n + 3]] = 1
            else:
                arr[arr[n + 3]] = 0
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
