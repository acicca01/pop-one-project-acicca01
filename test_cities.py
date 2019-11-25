import pytest
from cities import *


def test_compute_total_distance1():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)

def test_compute_total_distance2():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)] 
    assert compute_total_distance(road_map1)==5.3 

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


