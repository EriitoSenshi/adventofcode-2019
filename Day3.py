from sympy import Point2D
from sympy import Segment2D
from sympy import intersection


class Wire:
    def __init__(self):
        self.coordinates = []
        self.segments = []
        self.x = 0
        self.y = 0

    def move(self, movement):
        if movement[0] == 'U':
            self.y += int(movement[1:])
            self.coordinates.append(Point2D(self.x, self.y))
        elif movement[0] == 'D':
            self.y -= int(movement[1:])
            self.coordinates.append(Point2D(self.x, self.y))
        elif movement[0] == 'R':
            self.x += int(movement[1:])
            self.coordinates.append(Point2D(self.x, self.y))
        elif movement[0] == 'L':
            self.x -= int(movement[1:])
            self.coordinates.append(Point2D(self.x, self.y))

    def add_segments(self):
        for i in range(len(self.coordinates) - 1):
            self.segments.append(Segment2D(self.coordinates[i], self.coordinates[i + 1]))

    def get_intersection(self, wire):
        inters = []
        for segment1 in self.segments:
            for segment2 in wire.segments:
                inters.append(intersection(segment1, segment2))
        return inters


f = open('inputs/day3.txt', 'r')
paths = []
for line in f:
    path = []
    line = line.strip('\n').split(',')
    for p in line:
        path.append(p)
    paths.append(path)
f.close()

wire1 = Wire()
wire2 = Wire()

for movement1 in paths[0]:
    wire1.move(movement1)
for movement2 in paths[1]:
    wire2.move(movement2)

wire1.add_segments()
wire2.add_segments()

intersections = wire1.get_intersection(wire2)
distances = []
for inter in intersections:
    distances.append(abs(inter[0]) + abs(inter[1]))

min_distance = min(distances)