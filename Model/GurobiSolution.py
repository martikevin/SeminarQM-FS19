import math
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 16:06:00 2019

@author: kevin
"""

class GurobiSolution:

	time = math.inf
	OFV = math.inf
	mip_gap = math.inf
	
	#Decision variables
	variables = []
    
	def __init__(self, time, OFV, mip_gap, variables):
		self.time = time
		self.OFV = OFV
		self.mip_gap = mip_gap
		self.variables = variables
		
	def set_time(self, time):
		self.time = time