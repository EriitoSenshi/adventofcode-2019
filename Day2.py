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

# Part 1
int_code_2 = list(int_code_1)
int_code_2[1] = 12
int_code_2[2] = 2


def intcode_computer(arr):
    """
    Function used to represent the intcode program. Returns the value at 0 at the end.


    """
    for n in range(0, len(arr), 4):
        if arr[n] == 1:
            index1, index2, index3 = arr[n + 1], arr[n + 2], arr[n + 3]
            arr[index3] = arr[index1] + arr[index2]

        elif arr[n] == 2:
            index1, index2, index3 = arr[n + 1], arr[n + 2], arr[n + 3]
            arr[index3] = arr[index1] * arr[index2]

        elif arr[n] == 99:
            return arr[0]

    return arr[0]


print(intcode_computer(int_code_2))

# Part 2
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
