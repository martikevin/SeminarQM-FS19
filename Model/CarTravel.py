# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 16:06:00 2019

@author: kevin
"""

class CarTravel:
    ID = -1
    departure_node = -1
    arrival_node = -1
    departure_time = -1
    arrival_time = -1
    
    def __init__(self, ID, departure_node, arrival_node,departure_time, arrival_time):
        self.ID = ID
        self.departure_node = departure_node
        self.arrival_node = arrival_node
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def get_id(self):
	    return self.ID
    
    def get_arrival_time(self):
        return self.arrival_time

    def get_departure_time(self):
        return self.departure_time