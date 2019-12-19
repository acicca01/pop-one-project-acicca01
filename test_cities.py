import pytest
from cities import *

class Test_compute_total_distance:
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
        assert compute_total_distance(road_map)==pytest.approx(27131.83,0.001)

'''
def test_swap_cities():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    assert swap_cities(road_map1,1,3)==[("Minnesota", "Saint Paul", 44.95 -93.094),("Delaware", "Dover", 39.161921, -75.526755),("Kentucky", "Frankfort", 38.197274, -84.86311)]   

def test_shift_cities1():
    road_map1 = []
    assert shift_cities(road_map1) == []

def test_shift_cities2():
    road_map1 = [("Pennsylvania", "Philly",29.333,-99),\
                 (("New York State","NYC",30.983,-98))]
    road_map1[0] , road_map1[1] = road_map1[1] , road_map1[0]             
    assert shift_cities(road_map1) == road_map1 
'''

