def check_for_modes(array, number, relative_base):
    """
    Modified version of the method in Day5. Added mode 2 (relative mode)



    """
    index1, index2 = array[(number + 1) % len(array)], array[(number + 2) % len(array)]
    parameters = []
    s = str(array[number])

    if len(s) == 1:
        return [array[index1 % len(array)], array[index2 % len(array)]]

    elif len(s) == 3:
        if s[0] == '1':
            return [index1, array[index2 % len(array)]]
        elif s[0] == '2':
            return [array[(index1 + relative_base) % len(array)], array[index2 % len(array)]]

    elif len(s) == 4:
        if s[1] == '1':
            parameters.append(index1)
        elif s[1] == '2':
            parameters.append(array[(index1 + relative_base) % len(array)])
        else:
            parameters.append(array[index1 % len(array)])

        if s[0] == '1':
            parameters.append(index2)
        else:
            parameters.append(array[(index2 + relative_base) % len(array)])

    elif len(s) == 5:
        if s[2] == '1':
            parameters.append(index1)
        elif s[2] == '2':
            parameters.append(array[(index1 + relative_base) % len(array)])
        else:
            parameters.append(array[index1 % len(array)])

        if s[1] == '1':
            parameters.append(index2)
        elif s[1] == '2':
            parameters.append(array[(index2 + relative_base) % len(array)])
        else:
            parameters.append(array[index2 % len(array)])

    return parameters


def intcode_computer(arr, input_int):
    """
    Modified version of the method in Day 5. Added opcode 9


    """
    relative_base = 0
    n = 0

    while True:
        n = n % len(arr)
        parameters = check_for_modes(arr, n, relative_base)
        s = str(arr[n])

        if s[-1] == '1':
            if len(s) == 5 and s[0] == '2':
                arr[(arr[(n + 3) % len(arr)] + relative_base) % len(arr)] = parameters[0] + parameters[1]
            else:
                arr[arr[(n + 3) % len(arr)] % len(arr)] = parameters[0] + parameters[1]
            n += 4

        elif s[-1] == '2':
            if len(s) == 5 and s[0] == '2':
                arr[(arr[(n + 3) % len(arr)] + relative_base) % len(arr)] = parameters[0] * parameters[1]
            else:
                arr[arr[(n + 3) % len(arr)] % len(arr)] = parameters[0] * parameters[1]
            n += 4

        elif s[-1] == '3':
            if len(s) == 3:
                arr[(arr[(n + 1) % len(arr)] + relative_base) % len(arr)] = input_int
            else:
                arr[arr[(n + 1) % len(arr)] % len(arr)] = input_int
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
                if len(s) == 5 and s[0] == '2':
                    arr[(arr[(n + 3) % len(arr)] + relative_base) % len(arr)] = 1
                else:
                    arr[arr[(n + 3) % len(arr)] % len(arr)] = 1
            else:
                if len(s) == 5 and s[0] == '2':
                    arr[(arr[(n + 3) % len(arr)] + relative_base) % len(arr)] = 0
                else:
                    arr[arr[(n + 3) % len(arr)] % len(arr)] = 0
            n += 4

        elif s[-1] == '8':
            if parameters[0] == parameters[1]:
                if len(s) == 5 and s[0] == '2':
                    arr[(arr[(n + 3) % len(arr)] + relative_base) % len(arr)] = 1
                else:
                    arr[arr[(n + 3) % len(arr)] % len(arr)] = 1
            else:
                if len(s) == 5 and s[0] == '2':
                    arr[(arr[(n + 3) % len(arr)] + relative_base) % len(arr)] = 0
                else:
                    arr[arr[(n + 3) % len(arr)] % len(arr)] = 0
            n += 4

        elif s[-1] == '9':
            if s == '99':
                return
            else:
                relative_base += parameters[0]
                n += 2


# Retrieving the data
input_array = []
f = open('inputs/day9.txt', 'r')

for elem in f.read().split(','):
    input_array.append(int(elem))

f.close()

# Part 1
intcode_computer(input_array, 1)

# Part 2
intcode_computer(input_array, 2)
