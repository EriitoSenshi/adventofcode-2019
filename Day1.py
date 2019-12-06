import math


def get_fuel_sum(mass):
    fuel_sum = 0
    while mass >= 0:
        mass = math.floor(mass / 3) - 2
        if mass > 0:
            fuel_sum += mass
    return fuel_sum


f = open('inputs/day1.txt', 'r')
x = 0
for line in f:
    y = get_fuel_sum(float(line))
    x += y
f.close()
print(x)
