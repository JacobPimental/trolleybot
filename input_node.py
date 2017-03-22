#!/usr/bin/python3 

from synapses import *

class InputNode:

    synapses = []
    data = 0

    #sets up the data in our input node
    #parameters:
    #   data: our starting input
    #   synapses: our synapses that connect to other nodes
    #
    def __init__(self, data, synapses):
        self.data = data
        self.synapses = synapses
        for s in self.synapses:
            s.start = self

    
    def calculate( self ):
        for s in self.synapses:
            s.pass_data( self.data )

    def __str__(self):
        return "Input Node:\n\tData: " + str(self.data) + "\n\tSynapses: " + str(self.synapses)


if __name__ == "__main__":
    mysynapses = []
    mysynapses.append( Synapse( 2 ) )
    
    mysynapses.append( Synapse( 3 ) )
    
    input_node = InputNode( 52, mysynapses )
    
    print( input_node )







