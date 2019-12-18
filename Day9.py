def check_for_modes(array, number, relative_base):
    """
    Modified version of the method in Day5. Added mode 2 (relative mode)



    """
    index1, index2 = array[number + 1], array[number + 2]
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
        elif s[0] == '2':
            parameters.append(array[(index2 + relative_base) % len(array)])
        else:
            parameters.append(array[index2 % len(array)])
        return parameters


def intcode_computer(arr):
    """
    Modified version of the method in Day 5. Added opcode 9


    """
    input_int = 1
    relative_base = 0
    n = 0
    while True:
        print(arr)
        n = n % len(arr)
        print(n)
        parameters = check_for_modes(arr, n, relative_base)
        s = str(arr[n])
        if s[-1] == '1':
            arr[arr[n + 3] % len(arr)] = parameters[0] + parameters[1]
            n += 4
        elif s[-1] == '2':
            arr[arr[n + 3] % len(arr)] = parameters[0] * parameters[1]
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
                arr[arr[n + 3] % len(arr)] = 1
            else:
                arr[arr[n + 3] % len(arr)] = 0
            n += 4
        elif s[-1] == '8':
            if parameters[0] == parameters[1]:
                arr[arr[n + 3] % len(arr)] = 1
            else:
                arr[arr[n + 3] % len(arr)] = 0
            n += 4
        elif s[-1] == '9':
            if s == '99':
                return
            else:
                relative_base += parameters[0]
            n += 2


# Retrieving the data
input_array = []
f = open('inputs/day7.txt', 'r')
for elem in f.read().split(','):
    input_array.append(int(elem))
f.close()

intcode_computer([109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99])
