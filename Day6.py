# This class represents an object. It has a name, a list of other objects representing its orbits,
# an int representing how many orbits it has, as well as another object that it's the orbit of.
class Obj:
    def __init__(self, name):
        self.name = name
        self.orbit_count = 0
        self.orbit_list = []
        self.orbit_of = None

    def add_orbit(self, orbit):
        self.orbit_list.append(orbit)
        self.orbit_count += 1

    def __str__(self):
        return self.name + ',' + str(self.orbit_count)

    def print_orbits(self):
        for o in self.orbit_list:
            print(o.__str__())


def count_orbits(o):
    """
    Function used to count how many direct and indirect orbits an object has


    """
    x = o.orbit_count
    for orbit in o.orbit_list:
        x += count_orbits(orbit)
    return x


# Retrieving the objects using a dictionary
objects = {}
f = open('inputs/day6.txt', 'r')
for line in f:
    line = line.strip('\n').split(')')
    obj_name_1 = line[0]
    obj_name_2 = line[1]
    if obj_name_1 not in objects:
        objects[obj_name_1] = Obj(obj_name_1)
    if obj_name_2 not in objects:
        objects[obj_name_2] = Obj(obj_name_2)
    objects[obj_name_1].add_orbit(objects[obj_name_2])
    objects[obj_name_2].orbit_of = objects[obj_name_1]
f.close()
# Part 1: Counting all the direct and indirect connections for the whole graph of orbits
counter = 0
for obj in objects.values():
    counter += count_orbits(obj)
print(counter)

# Part 2: Counting how many objects are between 'YOU' and 'SAN'
you = objects['YOU']
san = objects['SAN']
you_object_names = []
san_object_names = []

while you.name != 'COM':
    you = you.orbit_of
    you_object_names.append(you.name)

while san.name != 'COM':
    san = san.orbit_of
    san_object_names.append(san.name)

for obj_name in you_object_names:
    if obj_name in san_object_names:
        print(you_object_names.index(obj_name) + san_object_names.index(obj_name))
        break
