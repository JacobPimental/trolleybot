#!/usr/bin/python3 

class Synapse:
    end = None
    weight = 0

    def __init__(self, weight, end):
        self.weight = weight
        self.end = end

    def pass_data(self, data ):
        new_data = float(data) * float(self.weight)
        self.end.retrieve_data( new_data )

    def __repr__(self):
        return "Synapse:\n\tWeight: " + str(self.weight) +  "\n\tEnd: " + repr(self.end) 
