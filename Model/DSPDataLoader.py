import pandas as pd
import numpy as np
from Duty import *
from CarTravel import *

# -*- coding: utf-8 -*-
"""

Is an interface with specific utility methods for the DSPSC Model. For further information
see the paper of Perumal et al. (2019). 

Created on Sun Mar 17 16:09:46 2019

@author: kevin
"""
#creates 2D dictionary with binary values
def create_dictionary (left_index, right_index, df, column_name):
    dictionary = {}
    temp_line = []
    
    for i in left_index:
        temp_line = np.zeros(len(right_index), dtype= int).tolist()
        if(not df[column_name].isnull()[i]): #catches empty lists
            temp_values = list(map(int, str(df[column_name].loc[i]).replace(",","").split()))
            for value in temp_values:
                temp_line[right_index.index(value)] = 1
        dictionary[i] = dict(zip(right_index, temp_line))
    assert(len(dictionary)>0)
        
    return dictionary
	

#creates 2D ditionary with binary values for the special H matrix
def create_H_dictionary(car_travels, H_tuples):
    dictionary = {}
    temp_line = []
    for i in car_travels:
        temp_line = np.zeros(len(car_travels), dtype=int).tolist()
        dictionary[i] = dict(zip(car_travels, temp_line))
    for tuple in H_tuples:
        dictionary[tuple[0]][tuple[1]] = 1

    return dictionary


#creates list of tuples of matching car travels
def create_H_tuples (car_matches_df):
    tuple_list = []
    for match in range(len(car_matches_df)):
        tuple_list.append((car_matches_df["Departure carTravelID"][match],car_matches_df["Arrival carTravelID"][match]))
    
    return tuple_list

	
#creates list of duty objects @see Duty from a duties data frame @see Pandas.df
def load_duties(duties_df):
    duty_objects = {}
    for row in duties_df.iterrows():
        if(type(row[1][2]) ==float): #checking if empty
            idx = []
        else:
            idx = row[1][2].replace(",","").split()
        duty_objects[row[0]] = Duty(row[0],row[1][0],list(map(int,row[1][1].replace(",","").split())), list(map(int,idx)))

    return duty_objects
	
	

# Returns dictionary of Car Travels with "CarTravelID" as Index
def load_car_travels(car_travels_df):
    car_travel_objects = {}
    for row in car_travels_df.iterrows():
        car_travel_objects[row[0]] = (CarTravel(row[0],row[1][0],row[1][1],row[1][2],row[1][3]))
    return car_travel_objects

