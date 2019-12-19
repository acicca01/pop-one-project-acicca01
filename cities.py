from math import *


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
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    if max(index1,index2) >= len(road_map):
        raise Exception(f"At least one of your indexes exceeds {len(road_map)-1}. What were you thinking ?")
    road_map[index1] , road_map[index2] = road_map[index2] , road_map[index1]

    return (road_map,compute_total_distance(road_map))


def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
    return road_map


def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    pass


def print_map(road_map):
    # TODO add parameter for matrix cost
    # TODO Use F-strings from Lecture Slide
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
    # print_cities(read_cities('city-data.txt',2))
    print_map(read_cities('city-data.txt'))
    """ 
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    pass


if __name__ == "__main__":  # keep this in
    main()
