from math import sqrt, ceil
from copy import copy
from random import random


# TODO create all-combo distances Matrix
def read_cities(file_name, rounding=100):
    # TODO cover file not found error in read_cities()

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


def print_cities(road_map):
    # TODO check if there is a way to print in a tabular format
    print("State\t", "City\t", "Latitude\t", "Longitude\t")
    print("-------------------------------------------")
    for i in range(len(road_map)):
        for j in range(4):
            print(road_map[i][j], end="\t")
        print("", end='\n')


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
    """Creates a copy of road_map and applies the swap to the copy not the original"""
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


def find_best_cycle(road_map,doit = 3):
    """
    Using a combination of `swap_cities` and `shift_cities`,
    try `10000` swaps/shifts, and each time keep the best cycle found so far.
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    # builds a swapping tuple
    random_list1 = []
    random_list2 = []
    for i in range(len(road_map)):
        random_list1.append((ceil(len(road_map) * random())))
        random_list2.append((ceil(len(road_map) * random())))
    indexes = tuple(zip(random_list1,random_list2))
    done = False
    # initialize operation number
    op_number = 0
    opt_map = []
    while not done:
        print ("Heeeeeey")
        op_number += 1
        for i in range(10000):
            if i == 1:
                opt_map = swap_cities(road_map, *indexes)
            else:
                opt_map = swap_cities(opt_map, *indexes)
        shift_cities(opt_map)
        if op_number > doit:
            done = True
    return opt_map



def print_map(road_map):
    # TODO add parameter for matrix cost
    # TODO Use F-strings from Lecture Slide
    # TODO Check to see if can display in circular way (or sort of S snake shaped)
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """

    padding = abs(len(road_map[1][1] + road_map[1][0]) - len(road_map[0][1] + road_map[0][0])) - 2

    L = len(road_map)
    for i in range(len(road_map)):
        repeat = min(len(road_map[i % L][1]), len(road_map[(i + 1) % L][1]))
        # padding = - len(road_map[(i+1)%L][1]+road_map[(i+1)%L][0]) + len(road_map[i%L][1]+road_map[i%L][0]) )
        if i == 0:
            print(road_map[i % L][1], '(' + road_map[i % L][0] + ')', sep=' ')
        print()
        print(repeat * "↓", "cost = ", 10)
        print()
        print(road_map[(i + 1) % L][1], '(' + road_map[(i + 1) % L][0] + ')', sep=' ')
    print("cost = ", 1000)


def main():
    # TODO check number of connection == len(map)
    # TODO prompt for input file functionality
    print_cities(read_cities('city-data.txt', 2))

    """ 
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    pass


if __name__ == "__main__":  # keep this in
    main()
