# Opening the input file for reading
f = open('inputs/day2.txt', 'r')

int_code_1 = []
int_code_2 = []

# Retrieving the numbers
for line in f:
    line = line.strip('\n').split(',')
    for num in line:
        int_code_1.append(int(num))

f.close()
int_code_2 = list(int_code_1)
int_code_2[1] = 12
int_code_2[2] = 2


def intcode_computer(arr):
    """
    This function works with 4 positions at a time. The first position is the opcode.
    An opcode of 1 means that we take the values of positions 2 and 3 as indexes.
    Then, we add the values at those indexes and output the result to the index
    representing the value of the 4th position. Same thing for opcode of 2 but multiplying instead of adding.
    An opcode of 99 halts the function.

    This function takes in an array and returns the value at index 0

    """
    for n in range(0, len(arr), 4):
        if arr[n] == 1:
            x = arr[n + 1]
            y = arr[n + 2]
            z = arr[n + 3]
            arr[z] = arr[x] + arr[y]
        elif arr[n] == 2:
            x = arr[n + 1]
            y = arr[n + 2]
            z = arr[n + 3]
            arr[z] = arr[x] * arr[y]
        elif arr[n] == 99:
            return arr[0]
    return arr[0]


print(intcode_computer(int_code_2))

# Trying pairs of values for positions 1 and 2, calling the function, and checking which gives the desired output
for i in range(100):
    for j in range(100):
        int_code_2 = list(int_code_1)
        int_code_2[1] = i
        int_code_2[2] = j
        result = intcode_computer(int_code_2)
        if result == 19690720:
            total = 100 * int_code_2[1] + int_code_2[2]
            print(total)
            break
