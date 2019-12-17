import itertools
from Day5 import add_op, multiply_op, output_op, jump_if_true, jump_if_false, less_than, equals


def intcode_computer(arr, first_input, second_input):
    """
    Modified version of the method in Day 5, this time taking 2 inputs


    """
    use_second_input = False
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
            if not use_second_input:
                arr[index] = first_input
                use_second_input = True
            else:
                arr[index] = second_input
            n += 2
        elif s[-1] == '4':
            return output_op(n, arr)
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
def amplifier_program(length, string, first_input):
    """
    Function used for part 1. Loops through the amplifiers once


    """
    if length == 0:
        return intcode_computer(input_array, int(string[length]), first_input)
    return intcode_computer(input_array, int(string[length]), amplifier_program(length - 1, string, first_input))


result_1 = []
for s in get_sequences('01234'):
    result_1.append(amplifier_program(len(s) - 1, s, 0))
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


result_2 = []
for s in get_sequences('56789'):
    result_2.append(feedback_loop(len(s) - 1, s))
print(max(result_2))
