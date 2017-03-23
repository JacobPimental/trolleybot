#!/usr/bin/python3 

from synapses import *
from hidden_node import *
from output_node import *
from hidden_layer import *
from input_layer import *
import random
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
    ans = float( 1/(1 + math.pow(math.e, -data) ) )
    return ans

if __name__ == "__main__":

    endNode = OutputNode(act_func)
    hiddenLayer = HiddenLayer( 1, act_func, endNode, None )
    inputLayer = InputLayer( [23, 32], 2, hiddenLayer)

    inputLayer.list_nodes()
    inputLayer.send_data()

    hiddenLayer.list_nodes()
    hiddenLayer.send_data()

    print( endNode )







