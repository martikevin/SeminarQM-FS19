# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 15:58:56 2019

@author: kevin
"""
class Duty:
    ID = -1
    cost = 0
    trips = []
    car_travels = []
    
    def __init__(self, ID, cost, trips, car_travels):
        self.ID = ID
        self.cost = cost
        self.trips = trips
        self.car_travels = car_travels
        
    #computes cost function of duty as c_d + beta(I_d - J_d + K_d) @see Perumal et. al
    def delta_cost_function(self, bus_trips_covered, beta):
        intersection = set(bus_trips_covered).intersection(self.trips)
        residue = set(self.trips).difference(intersection)

        return self.cost + beta*(len(intersection) - len(residue) + len(self.car_travels))
		

    def get_cost(self):
        return self.cost

    def toString (self):
        return str(self.ID) + ",   " + str(self.cost) + ",  " + str(self.trips) + ",   " + str(self.car_travels)
	    
		
    def get_bus_trips(self):
        return self.trips
		
    def get_car_travels(self):
        return self.car_travels
    def get_id(self):
	    return self.ID

