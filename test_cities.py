from copy import deepcopy

import pytest
from cities import *

class Test_compute_total_distance:
    # TODO 2 cities on the list located in same place
    def test_one(self):
        road_map = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                    ("Delaware", "Dover", 39.161921, -75.526755),\
                    ("Minnesota", "Saint Paul", 44.95, -93.094)]
        assert compute_total_distance(road_map)==pytest.approx(9.386+18.496+10.646,0.001)
    def test_two(self):
        road_map = [("A", "City", 1, 0),\
                    ("A", "City", 1, 0),\
                    ("A", "City", 1, 0)]
        assert compute_total_distance(road_map)==pytest.approx(0)
    def test_three(self):
        road_map = [("Zero", "Zero", 0, 0),\
                    ("Zero", "Zero", 0, 0),\
                    ("Something", "Zero", 4, 0)]
        assert compute_total_distance(road_map)==pytest.approx(8)
    def test_four(self):
        road_map = [("A" , "City" , 3.054,-99.002),\
                    ("Another" , "City" , 3.9843, -45.39940051)]
        assert compute_total_distance(road_map)==pytest.approx(53.61067,0.001)
    def test_five(self):
        road_map = read_cities('city-data.txt')
        assert compute_total_distance(road_map)==pytest.approx(1060.171,0.001)

class Test_swap_cities:
    def test_one(self):
        road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                     ("Delaware", "Dover", 39.161921, -75.526755),\
                     ("Minnesota", "Saint Paul", 44.95, -93.094)]
        assert swap_cities(road_map1,1,3)[0]==[("Minnesota", "Saint Paul", 44.95 , -93.094),\
                                               ("Delaware", "Dover", 39.161921, -75.526755),\
                                               ("Kentucky", "Frankfort", 38.197274, -84.86311)]
    def test_two(self):
        road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                     ("Delaware", "Dover", 39.161921, -75.526755),\
                     ("Minnesota", "Saint Paul", 44.95, -93.094)]
        assert swap_cities(road_map1,0,2)[0]==[("Minnesota", "Saint Paul", 44.95 , -93.094),\
                                            ("Delaware", "Dover", 39.161921, -75.526755),\
                                            ("Kentucky", "Frankfort", 38.197274, -84.86311)]
    def test_three(self):
        road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                     ("Delaware", "Dover", 39.161921, -75.526755),\
                     ("Minnesota", "Saint Paul", 44.95, -93.094)]
        assert swap_cities(road_map1,1,1)[0]==[("Kentucky", "Frankfort", 38.197274, -84.86311),\
                                            ("Delaware", "Dover", 39.161921, -75.526755),\
                                            ("Minnesota", "Saint Paul", 44.95, -93.094)]
    def test_four(self):
        test_map = read_cities('city-data.txt')
        swap_map = read_cities('city-sub.txt')
        assert swap_cities(test_map,0,31)[0] == swap_map
        assert swap_cities(test_map,0,31)[1] == pytest.approx(1065.63,0.001)
    def test_five(self):
        test_map = read_cities('city-data.txt')
        swap_map = read_cities('city-sub.txt')
        my_swap = swap_cities(test_map,0,31)
        assert my_swap[0] == swap_map
        assert my_swap[1] == pytest.approx(1065.63,0.001)
    def test_six(self):
        test_map = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                    ("Delaware", "Dover", 39.161921, -75.526755),\
                    ("Minnesota", "Saint Paul", 44.95, -93.094)]
        swap_map = [("Minnesota", "Saint Paul", 44.95 , -93.094),\
                    ("Delaware", "Dover", 39.161921, -75.526755),\
                    ("Kentucky", "Frankfort", 38.197274, -84.86311)]
        tuple_swap = (swap_cities(test_map,0,2)[0] ,swap_cities(test_map,0,2)[0])
        assert tuple_swap== (swap_map , swap_map)
    def test_seven(self):
        test_map = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                    ("Delaware", "Dover", 39.161921, -75.526755),\
                    ("Minnesota", "Saint Paul", 44.95, -93.094)]
        swap_map = [("Minnesota", "Saint Paul", 44.95 , -93.094),\
                    ("Delaware", "Dover", 39.161921, -75.526755),\
                    ("Kentucky", "Frankfort", 38.197274, -84.86311)]
        assert swap_cities(test_map,0,2)[0] == swap_map
        assert swap_cities(test_map,0,2)[0] == swap_map

class Test_shift_cities:
    def test_one(self):
        road_map1 = []
        assert shift_cities(road_map1) == []
    def test_two(self):
        road_map1 = [("Pennsylvania", "Philly",29.333,-99),\
                     (("New York State","NYC",30.983,-98))]
        road_map1[0] , road_map1[1] = road_map1[1] , road_map1[0]
        assert shift_cities(road_map1) == road_map1
    def test_three(self):
        test_map =  [("Kentucky", "Frankfort", 38.197274, -84.86311),
                     ("Delaware", "Dover", 39.161921, -75.526755),
                     ("Minnesota", "Saint Paul", 44.95, -93.094)]
        shift_map = [("Minnesota", "Saint Paul", 44.95, -93.094),
                     ("Kentucky", "Frankfort", 38.197274, -84.86311),
                     ("Delaware", "Dover", 39.161921, -75.526755)]
        assert shift_cities(test_map) == shift_map
    def test_four(self):
        # TODO destroy road_map
        test_map = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                     ("Delaware", "Dover", 39.161921, -75.526755),
                     ("Minnesota", "Saint Paul", 44.95, -93.094)]
        road_map = deepcopy(test_map)
        for i in range(3):
            test_map = shift_cities(test_map)
        assert test_map == road_map
    def test_five(self):
        test_map = read_cities('city-data.txt')
        road_map = deepcopy(test_map)
        for i in range(len(test_map)):
            test_map = shift_cities(test_map)
        assert test_map == road_map



