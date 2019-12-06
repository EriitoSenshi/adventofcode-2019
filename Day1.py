import math


def get_fuel_sum(mass):
    fuel_sum = 0
    while mass >= 0:
        mass = math.floor(mass / 3) - 2
        if mass > 0:
            fuel_sum += mass
    return fuel_sum


f = open('inputs/day1.txt', 'r')
fuel_total_1 = 0
fuel_total_2 = 0
for line in f:
    fuel_required_1 = math.floor(float(line) / 3) - 2
    fuel_total_1 += fuel_required_1
    fuel_required_2 = get_fuel_sum(float(line))
    fuel_total_2 += fuel_required_2
f.close()
print(fuel_total_1, fuel_total_2)
