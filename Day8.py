width, height = 25, 6

# Retrieving the data
layers = []
f = open('inputs/day8.txt', 'r')

for line in f:
    line = line.strip('\n')
    for i in range(0, len(line), width * height):
        layers.append(line[i:i + width * height])

f.close()


def get_digits(digit):
    """
    Function used to retrieve the amount of a specific digit for each layer. Used in Part 1


    """
    digit_count_array = []
    for layer in layers:
        digit_count = 0
        for j in range(len(layer)):
            if int(layer[j]) == digit:
                digit_count += 1
        digit_count_array.append(digit_count)

    return digit_count_array


def get_image_pixel(index):
    """
    Function used to get the first non-transparent pixel in the index of an image


    """
    for pixels in layers:
        if pixels[index] != '2':
            return pixels[index]


# Part 1
zeros, ones, twos = get_digits(0), get_digits(1), get_digits(2)
min_zeros = min(zeros)

result = ones[zeros.index(min_zeros)] * twos[zeros.index(min_zeros)]
print(result)

# Part 2
image = ''
for i in range(width * height):
    image += get_image_pixel(i)

message = []
for i in range(0, len(image), width):
    message.append(image[i:i + width])

for string in message:
    string = string.replace('0', ' ')
    string = string.replace('1', '#')
    print(string)
