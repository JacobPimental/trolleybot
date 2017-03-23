#!/usr/bin/python3 

from synapses import *
from hidden_node import *
from output_node import *
import math

class InputNode:

    synapses = []
    data = 0.0

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


def act_func( data ):
    print( "Using activation function on " + str( data ) )
    ans = float( 1/(1 + math.pow(math.e, -data) ) )
    print( "Got: " + str(ans) )
    return ans

if __name__ == "__main__":
    mysynapses = []
    mysynapses.append( Synapse( 0.02 ) )
    mysynapses.append( Synapse( 0.03 ) )
    
    mysynapses2 = []
    mysynapses2.append( Synapse( 0.03 ) )
 
    input_node = InputNode( 1, mysynapses )
    output_node = OutputNode( mysynapses2, act_func )
    hidden_node = HiddenNode( mysynapses, mysynapses2, act_func, output_node )
    

    input_node.calculate()
    hidden_node.pass_through()
    
    print( output_node )







