class Obj:
    def __init__(self, name):
        self.name = name
        self.orbits = 0
        self.orbit_list = []

    def add_orbit(self, orbit):
        self.orbit_list.append(orbit)

    def get_orbit_names(self):
        orbit_names = []
        for o in self.orbit_list:
            orbit_names.append(o.name)
        return orbit_names

    def __str__(self):
        return self.name + ',' + str(self.orbits)

    def print_orbits(self):
        for o in self.orbit_list:
            print(o.__str__())


def count_orbits(o):
    x = o.orbits
    for orbit in o.orbit_list:
        x += count_orbits(orbit)
    return x


object_dict = {}
f = open('inputs/day6.txt', 'r')
for line in f:
    line = line.strip('\n').split(')')
    obj1 = Obj(line[0])
    obj2 = Obj(line[1])
    if obj1.name not in object_dict.keys():
        object_dict[obj1.name] = obj1
        object_dict[obj1.name].add_orbit(obj2)
        object_dict[obj1.name].orbits += 1

    else:
        if obj2.name not in object_dict[obj1.name].get_orbit_names():
            object_dict[obj1.name].add_orbit(obj2)
            object_dict[obj1.name].orbits += 1


