f = open('inputs/day2.txt', 'r')

int_code_1 = []
int_code_2 = []
for line in f:
    line = line.strip('\n').split(',')
    for num in line:
        int_code_1.append(int(num))

f.close()
int_code_2 = list(int_code_1)
int_code_2[1] = 12
int_code_2[2] = 2


def intcode_computer(arr):
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
