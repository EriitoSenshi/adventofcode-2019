import itertools
from Day5 import check_for_modes


def intcode_computer(arr, first_input, second_input):
    """
    Modified version of the method in Day 5, this time taking 2 inputs


    """
    use_second_input = False
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
            if not use_second_input:
                arr[arr[n + 1]] = first_input
                use_second_input = True
            else:
                arr[arr[n + 1]] = second_input
            n += 2
        elif s[-1] == '4':
            return parameters[0]
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


# Retrieving the data
input_array = []
f = open('inputs/day7.txt', 'r')
for char in f.read().split(','):
    input_array.append(int(char))
f.close()


def get_sequences(string):
    """
    Function used to retrieve the sequences used for the amplifier programs


    """
    strings = []
    for subset in itertools.permutations(string, 5):
        string = ''
        for elem in subset:
            string += elem
        strings.append(string)
    return strings


# Part 1
def amplifier_program(length, string):
    """
    Function used for part 1. Loops through the amplifiers once


    """
    if length == 0:
        return intcode_computer(input_array, int(string[length]), 0)
    return intcode_computer(input_array, int(string[length]), amplifier_program(length - 1, string))


result_1 = []
for sequence in get_sequences('01234'):
    result_1.append(amplifier_program(len(sequence) - 1, sequence))
print(max(result_1))


# Part 2
def feedback_loop(length, string):
    """
    Function used for part 2. Loops through the amplifiers until they halt


    """
    actual_result = 0
    input_int = 0
    while input_int is not None:
        result = intcode_computer(input_array, int(string[length]), amplifier_program(length, string, input_int))
        input_int = result
        if input_int is not None:
            actual_result = input_int
    return actual_result


'''result_2 = []
for s in get_sequences('56789'):
    result_2.append(feedback_loop(len(s) - 1, s))
print(max(result_2))'''
