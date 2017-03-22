#!/usr/bin/python3 

class Synapse:
    start = None
    end = None
    weight = 0

    def __init__(self, weight):
        self.weight = weight

    def pass_data(self, data ):
        new_data = data * self.weight
        self.end.retrieve_data( new_data )

    def __repr__(self):
        return "Synapse:\n\tWeight: " + str(self.weight) + "\n\tStart: " + repr(self.start) + "\n\tEnd: " + repr(self.end) 
