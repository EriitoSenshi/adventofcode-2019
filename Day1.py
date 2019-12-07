import math


def get_fuel_sum(mass):
    """
    Function that returns the fuel required of a module based on its mass


    """
    fuel_sum = 0
    while mass >= 0:
        mass = math.floor(mass / 3) - 2
        if mass > 0:
            fuel_sum += mass
    return fuel_sum


# Opening the input file for reading
f = open('inputs/day1.txt', 'r')

fuel_total_1 = 0
fuel_total_2 = 0

# Looping through the modules
for module in f:
    # This represents part 1, which is getting the "starting" fuel required
    fuel_required_1 = math.floor(float(module) / 3) - 2
    fuel_total_1 += fuel_required_1
    # This represents part 2, which is getting the actual fuel required
    fuel_required_2 = get_fuel_sum(float(module))
    fuel_total_2 += fuel_required_2
f.close()
print(fuel_total_1, fuel_total_2)
