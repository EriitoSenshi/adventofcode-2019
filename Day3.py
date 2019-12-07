import math

f = open('inputs/day3.txt', 'r')

paths = []
for line in f:
    path = []
    line = line.strip('\n').split(',')
    for p in line:
        path.append(p)
    paths.append(path)
f.close()

coordinates_1 = [(0, 0)]
coordinates_2 = [(0, 0)]


def get_coordinates(coordinates, n):
    for pa in paths[n]:
        if pa[0] == 'R':
            x0 = coordinates[len(coordinates) - 1][0]
            x1 = x0 + int(pa[1:len(pa)])
            y = coordinates[len(coordinates) - 1][1]
            for x in range(x0 + 1, x1 + 1):
                if (x, y) not in coordinates:
                    coordinates.append((x, y))
        elif pa[0] == 'L':
            x0 = coordinates[len(coordinates) - 1][0]
            x1 = x0 - int(pa[1:len(pa)])
            y = coordinates[len(coordinates) - 1][1]
            for x in range(x0 - 1, x1 - 1, -1):
                if (x, y) not in coordinates:
                    coordinates.append((x, y))
        elif pa[0] == 'U':
            x = coordinates[len(coordinates) - 1][0]
            y0 = coordinates[len(coordinates) - 1][1]
            y1 = y0 + int(pa[1:len(pa)])
            for y in range(y0 + 1, y1 + 1):
                if (x, y) not in coordinates:
                    coordinates.append((x, y))
        elif pa[0] == 'D':
            x = coordinates[len(coordinates) - 1][0]
            y0 = coordinates[len(coordinates) - 1][1]
            y1 = y0 - int(pa[1:len(pa)])
            for y in range(y0 - 1, y1 - 1, -1):
                if (x, y) not in coordinates:
                    coordinates.append((x, y))


def get_manhattan_distance(coord):
    return math.fabs(coord[0]) + math.fabs(coord[1])


def get_path_length(coord):
    return coordinates_1.index(coord) + 1 + coordinates_2.index(coord) + 1


get_coordinates(coordinates_1, 0)
get_coordinates(coordinates_2, 1)
intersections = []
path_lengths = []
coordinates_1.remove(coordinates_1[0])
coordinates_2.remove(coordinates_2[0])

# This takes a while
for coordinate in coordinates_1:
    if coordinate in coordinates_2:
        intersections.append(coordinate)

min_distance = get_manhattan_distance(intersections[0])
min_path_length = get_path_length(intersections[0])
for intersection in intersections:
    distance = get_manhattan_distance(intersection)
    if distance < min_distance:
        min_distance = distance
    path_length = get_path_length(intersection)
    if path_length < min_path_length:
        min_path_length = path_length

print(min_distance)
print(min_path_length)
