#!/usr/bin/python3 

class OutputNode:
    synapses = []
    data = 0.0
    act_func = None
    act_data = 0.0

    def __init__(self, synapses, act_func):
        self.act_func = act_func
        self.synapses = synapses

    def retrieve_data(self, data):
        self.data += data
        self.act_data = self.act_func( self.data )

    def __repr__(self):
        return "Output Node:\n\tData: " + str(self.data)
