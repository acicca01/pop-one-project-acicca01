from copy import copy
from math import sqrt, floor
from random import random

# Read in the cities from the given file_name, and return them as a list of four-tuples:
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

# Prints a list of cities, along with their locations.
def print_cities(road_map):
    print("State\t", "City\t", "Latitude\t", "Longitude\t")
    print("-------------------------------------------")
    for i in range(len(road_map)):
        for j in range(4):
            print(road_map[i][j], end="\t")
        print()

# Returns, as a floating point number, the sum of the distances of all the connections in the road_map.
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

# Take the city at location index in the road_map, and the city at location index2,
# swap their positions in the road_map, compute the new total distance,
# and return the tuple
def swap_cities(road_map, index1, index2):
    """Creates a copy of road_map and applies the swap to the copy and not to the original"""
    if max(index1, index2) >= len(road_map):
        raise Exception(f"At least one of your indexes exceeds {len(road_map) - 1}. What were you thinking ?")
    new_road_map = copy(road_map)
    new_road_map[index1], new_road_map[index2] = road_map[index2], road_map[index1]

    return (new_road_map, compute_total_distance(new_road_map))

# For every index i in the road_map, the city at the position i moves to the position i+1.
def shift_cities(road_map):
    # modifies map in place
    l = len(road_map)
    assert (l > 1), f"The map you passed to shift_cities() has {l} cities. That is not enough."
    road_map[0], road_map[1:] = road_map[l - 1], road_map[:(l - 1)]
    return road_map

# Using a combination of swap_cities and shift_cities,return the best cycle found so far
def find_best_cycle(road_map, doit=10000):
    # recording best path found so far and its total distance
    record_map = copy(road_map)
    # length of shortest path found so far
    record = compute_total_distance(record_map)
    done = False
    # initialize iteration number
    it_number = 0
    # initialize portfolio. This is a set of maps configuration the algorithm has found so far.
    portfolio = set()
    portfolio.add(tuple(record_map))
    # If a configuration has already been used shift the current map
    while not done:
        it_number += 1
        random_swap = (floor(len(record_map) * random()), floor(len(record_map) * random()))
        # the algorithm can 'stall' if random swap consider maps already explored in previous iterations
        if swap_cities(record_map, *random_swap)[1] < record:
            record = swap_cities(record_map, *random_swap)[1]
            record_map = copy(swap_cities(record_map, *random_swap)[0])
            portfolio.add(tuple(record_map))
        # if a map has already been found shift cities and try again
        elif tuple(swap_cities(record_map, *random_swap)[0]) in portfolio:
            shift_cities(record_map)
        if it_number > doit:
            done = True
    return record_map

# Prints, in an easily understandable textual format,
# the cities and their connections, along with the cost for each connection and the total cost.
def print_map(road_map):
    padding = abs(len(road_map[1][1] + road_map[1][0]) - len(road_map[0][1] + road_map[0][0])) - 2
    l = len(road_map)
    for i in range(len(road_map)):
        repeat = min(len(road_map[i % l][1]), len(road_map[(i + 1) % l][1]))
        if i == 0:
            print(road_map[i % l][1], '(' + road_map[i % l][0] + ')', sep=' ')
        print()
        # Define a rolling map consisting of 2 cities.
        # This way the distance can be computed between the last city and the first.
        submap = [road_map[i % l], road_map[(i + 1) % l]]
        cost = compute_total_distance(submap)
        print(repeat * "↓", "cost = ", round(cost, 2))
        print()
        print(road_map[(i + 1) % l][1], '(' + road_map[(i + 1) % l][0] + ')', sep=' ')
    print()
    print(repeat * "-")
    print("Total cost of map = ", round(compute_total_distance(road_map), 2))

# Prints the grid representing road_map to working/directory/visualise.txt
# Highly recommended to open the file in Pycharm. IDLE works also fine. Other text editors may loose line wrapping
def visualise(road_map):
    # Initialise dictionary. This is used to retrieve city's position in a map based on its (latitude ,longitude)
    map_dic = dict()

    # Initialise temporary lists of all latitudes longitudes values found in the map. The idea is to determine
    # dimensions of the map based on overall map max(latitude) max(longitude) .
    # The 2 lists will streamline the min/max computation
    latitudes = []
    longitudes = []

    # Load dictionary map_dic with key (latitude, longitude) and value position on map
    # Create ranges for latitude / longitude and load them into tuple
    for i in range(len(road_map)):
        # Using discrete space representation implies we can have collisions
        # If coordinates already busy introduce a random fuzz factor 'fuzz' with 1<=fuzz<2 in else block
        if (round(road_map[i][2]), round(road_map[i][3])) not in map_dic:
            map_dic[(round(road_map[i][2]), round(road_map[i][3]))] = i
            latitudes.append(round(road_map[i][2]))
            longitudes.append(round(road_map[i][3]))
        else:
            map_dic[(round(road_map[i][2]+random()+1), round(road_map[i][3]+random()+1))] = i
            latitudes.append(round(road_map[i][2]+random()+1))
            longitudes.append(round(road_map[i][3]+random()+1))
        # load latitude-longitude ranges into tuple
        lat_range = (min(latitudes), max(latitudes) + 1)
        long_range = (min(longitudes), max(longitudes) + 1)
    with open('visualise.txt', 'w') as outfile:
        # Create a reference longitudes row. This will appear on the top of the grid.
        print('      ', end='', file = outfile )
        for i in range(*long_range):
            if len(str(i)) == 4:
                print(i, end='  ' , file = outfile)
            elif len(str(i)) == 3:
                print(i, end='   ', file = outfile)
            elif len(str(i)) == 2:
                print(i, end='    ', file = outfile)
            elif len(str(i)) == 1:
                print(i, end='     ', file = outfile)
        print(file = outfile)

        # Building reference latitude column. This will appear on the left of the grid.
        # Building a 'Grid' based on the retrieved values for position from the dictionary map_dic. (j,i) used as key.
        for j in range(*lat_range):
            # Some basic alignment work
            if len(str(j)) == 3:
                print('   ', end='', file = outfile)
            if len(str(j)) == 2:
                print('  ', end='', file = outfile)
            for i in range(*long_range):
                print('  ', ' ', sep='|', end='  ', file = outfile)
            print( file = outfile)
            for i in range(*long_range):
                # Create latitude column
                if i == long_range[0]:
                    print(j, end='   ', file = outfile)
                # If a city appear at a given (latitude,longitude) print its position on the grid
                if (j, i) in map_dic:
                    tmp = str(map_dic[(j, i)] + 1)
                    if len(tmp) == 1:
                        print('  ', ' ', sep=tmp, end='  ', file = outfile)
                    if len(tmp) == 2:
                        print(' ', ' ', sep=tmp, end='  ', file = outfile)
                    if len(tmp) == 3:
                        print('', ' ', sep=tmp, end='  ', file = outfile)
                    if len(tmp) == 4:
                        print('', '', sep=tmp, end='  ', file = outfile)
                # Print a '-' if no city in the map with the given (j , i) coordinates
                else:
                    print(f"{'-':^6}", end='', file = outfile)
            print(file=outfile)
    return map_dic

#     """
#     Reads in, and prints out, the city data, then creates the "best"
#     cycle and prints it out.
#     """
def main():
    input_file = input("Enter file name for map:> ")
    amap = read_cities(input_file)
    banner = '''  ____   _   _     _                  _       _         _     
 / ___| (_) | |_  (_)   ___   ___    | |     (_)  ___  | |_   
| |     | | | __| | |  / _ \ / __|   | |     | | / __| | __|  
| |___  | | | |_  | | |  __/ \__ \   | |___  | | \__ \ | |_   
 \____| |_|  \__| |_|  \___| |___/   |_____| |_| |___/  \__|  '''
    print(banner)
    print()

    print_cities(read_cities(input_file,rounding=2))
    banner = ''' ____    _____   ____    _____      ____  __   __   ____   _       _____     _____    ___    _   _   _   _   ____  
| __ )  | ____| / ___|  |_   _|    / ___| \ \ / /  / ___| | |     | ____|   |  ___|  / _ \  | | | | | \ | | |  _ \ 
|  _ \  |  _|   \___ \    | |     | |      \ V /  | |     | |     |  _|     | |_    | | | | | | | | |  \| | | | | |
| |_) | | |___   ___) |   | |     | |___    | |   | |___  | |___  | |___    |  _|   | |_| | | |_| | | |\  | | |_| |
|____/  |_____| |____/    |_|      \____|   |_|    \____| |_____| |_____|   |_|      \___/   \___/  |_| \_| |____/ '''

    print(banner)
    print()

    best_map = find_best_cycle(amap)
    print_map(best_map)
    print ()
    visualise(best_map)
    print ()
    print("To check the grid open visualise.txt in your working directory")
    print("To do that it's highly recommended to use Pycharm (although IDLE works just fine)")




if __name__ == "__main__":  # keep this in
    main()
