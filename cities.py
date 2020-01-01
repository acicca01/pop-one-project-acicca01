from math import sqrt, floor
from copy import copy
from random import random


def read_cities(file_name, rounding=100):
    try:
        # importing a map in a list
        with open(file_name) as input_file:
            amap = input_file.readlines()
        # converting amap location elements to tuples
        for location_index in range(len(amap)):
            # to string
            amap[location_index] = amap[location_index].rstrip('\n')
            amap[location_index] = amap[location_index].split('\t')
            # to float
            amap[location_index][2] = round(float(amap[location_index][2]), rounding)
            amap[location_index][3] = round(float(amap[location_index][3]), rounding)
            amap[location_index] = tuple(amap[location_index])
        return amap
    except OSError:
        print(f"Input file {file_name} not found")


def print_cities(road_map):
    # TODO check if there is a way to print in a tabular format
    print("State\t", "City\t", "Latitude\t", "Longitude\t")
    print("-------------------------------------------")
    for i in range(len(road_map)):
        for j in range(4):
            print(road_map[i][j], end="\t")
        print("", end='\n'


def compute_total_distance(road_map):
    roadmap_length = len(road_map)
    assert (roadmap_length > 1), "Compute distance will run on a map with at least 2 cities."
    tot = 0
    if roadmap_length == 2:
        tot = sqrt((road_map[1][2] - road_map[0][2]) ** 2 + (road_map[1][3] - road_map[0][3]) ** 2)
    else:
        for i in range(roadmap_length):
            tot += sqrt((road_map[(i + 1) % roadmap_length][2] - road_map[i % roadmap_length][2]) ** 2 + (
                    road_map[(i + 1) % roadmap_length][3] - road_map[i % roadmap_length][3]) ** 2)

    return tot


def swap_cities(road_map, index1, index2):
    """Creates a copy of road_map and applies the swap to the copy and not to the original"""
    # TODO check how to destroy shallow copy
    if max(index1, index2) >= len(road_map):
        raise Exception(f"At least one of your indexes exceeds {len(road_map) - 1}. What were you thinking ?")
    new_road_map = copy(road_map)
    new_road_map[index1], new_road_map[index2] = road_map[index2], road_map[index1]

    return (new_road_map, compute_total_distance(new_road_map))


def shift_cities(road_map):
    # modifies map in place
    l = len(road_map)
    assert (l > 1), f"The map you passed to shift_cities() has {l} cities. That is not enough."
    road_map[0], road_map[1:] = road_map[l - 1], road_map[:(l - 1)]
    return road_map


def find_best_cycle(road_map, doit=10000):
    # recording best path found so far and its total distance
    record_map = copy(road_map)
    # length of shortest path found so far
    record = compute_total_distance(record_map)
    done = False
    # initialize operation number
    op_number = 0
    # initialize portfolio. This is a set of maps configuration the algo has found so far.
    portfolio = set()
    portfolio.add(tuple(record_map))
    # If a configuration has already been used shift the current map
    while not done:
        op_number += 1
        random_swap = (floor(len(record_map) * random()), floor(len(record_map) * random()))
        if swap_cities(record_map, *random_swap)[1] < record:
            record = swap_cities(record_map, *random_swap)[1]
            record_map = copy(swap_cities(record_map, *random_swap)[0])
            portfolio.add(tuple(record_map))
        elif tuple(swap_cities(record_map, *random_swap)[0]) in portfolio:
            shift_cities(record_map)
        if op_number > doit:
            done = True

    return record_map


def print_map(road_map):
    # TODO add parameter for matrix cost
    # TODO Use F-strings from Lecture Slide
    # TODO Check to see if can display in circular way (or sort of S snake shaped)
    padding = abs(len(road_map[1][1] + road_map[1][0]) - len(road_map[0][1] + road_map[0][0])) - 2

    l = len(road_map)
    for i in range(len(road_map)):
        repeat = min(len(road_map[i % l][1]), len(road_map[(i + 1) % l][1]))
        if i == 0:
            print(road_map[i % l][1], '(' + road_map[i % l][0] + ')', sep=' ')
        print()
        # define a rolling map consisting of 2 cities
        submap = [road_map[i % l], road_map[(i + 1) % l]]
        cost = compute_total_distance(submap)
        print(repeat * "↓", "cost = ", round(cost, 2))
        print()
        print(road_map[(i + 1) % l][1], '(' + road_map[(i + 1) % l][0] + ')', sep=' ')
    print()
    print(repeat * "-")
    print("Total cost of map = ", round(compute_total_distance(road_map), 2))


def main():
    # TODO check number of connection == len(map)
    input_file = input("Enter file name for map")
    hell = read_cities("input_file")
    hell = [0, 2, 1]
    # best = find_best_cycle(amap, doit=100)
    # the_map = read_cities(input_file)
    # print_map(the_map)

    """ 
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """


if __name__ == "__main__":  # keep this in
    main()
