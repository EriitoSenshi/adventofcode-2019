from sympy import Segment, intersection


# This class represents a wire. It has a set of coordinates and segments
class Wire:
    def __init__(self):
        self.coordinates = [(0, 0)]
        self.segments = []
        self.x = 0
        self.y = 0

    def move(self, movement):
        if movement[0] == 'U':
            self.y += int(movement[1:])
            self.coordinates.append((self.x, self.y))
        elif movement[0] == 'D':
            self.y -= int(movement[1:])
            self.coordinates.append((self.x, self.y))
        elif movement[0] == 'R':
            self.x += int(movement[1:])
            self.coordinates.append((self.x, self.y))
        elif movement[0] == 'L':
            self.x -= int(movement[1:])
            self.coordinates.append((self.x, self.y))

    def add_segments(self):
        for i in range(len(self.coordinates) - 1):
            self.segments.append(Segment(self.coordinates[i], self.coordinates[i + 1]))

    def get_intersections(self, wire):
        inters = []
        for segment1 in self.segments:
            for segment2 in wire.segments:
                if intersection(segment1, segment2):
                    inters.append(intersection(segment1, segment2)[0])
        return inters


# Retrieving the data
f = open('inputs/day3.txt', 'r')
movements = []
for line in f:
    path = []
    line = line.strip('\n').split(',')
    for p in line:
        path.append(p)
    movements.append(path)
f.close()

wire1 = Wire()
wire2 = Wire()

for movement1 in movements[0]:
    wire1.move(movement1)
for movement2 in movements[1]:
    wire2.move(movement2)

wire1.add_segments()
wire2.add_segments()

intersections = wire1.get_intersections(wire2)
intersections.remove(intersections[0])

# Part 1: computing the minimum Manhattan distance
distances_part_1 = []
for inter in intersections:
    distances_part_1.append(abs(inter[0]) + abs(inter[1]))
print(min(distances_part_1))

# Part 2: computing the shortest added path length for both wires to an intersection
distances_part_2 = []
for inter in intersections:
    path_length_1 = 0
    for segment_1 in wire1.segments:
        if segment_1.contains(inter):
            path_length_1 += segment_1.points[0].distance(inter)
            break
        else:
            path_length_1 += segment_1.length

    path_length_2 = 0
    for segment_2 in wire2.segments:
        if segment_2.contains(inter):
            path_length_2 += segment_2.points[0].distance(inter)
            break
        else:
            path_length_2 += segment_2.length

    distances_part_2.append(path_length_1 + path_length_2)
print(min(distances_part_2))
