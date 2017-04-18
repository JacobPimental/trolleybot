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

    def updateSynapses( self, delta ):
        for s in range( len( delta ) ):
            self.synapses[s].weight += delta[s]


def act_func( data ):
    ans = float( 1/(1 + math.pow(math.e, -data) ) )
    return ans

def deriv_act_func( data ):
    ans = float( math.pow(math.e, data) / math.pow( math.pow(math.e, data) + 1, 2 ) )
    return ans

if __name__ == "__main__":

    expected = 0
    weights = [[0.23]]
    endNode = OutputNode(act_func)
    hiddenLayer = HiddenLayer( 1, act_func, endNode, None, weights )
    inputLayer = InputLayer( [23, 32], hiddenLayer)

    inputLayer.list_nodes()
    inputLayer.send_data()

    hiddenLayer.list_nodes()
    hiddenLayer.send_data()

    print( endNode )

    error = endNode.data - expected
    deltaSum = deriv_act_func( endNode.data ) * error

    inputLayer.backProp( deltaSum )
    hiddenLayer.backProp( deltaSum )
    
    inputLayer.list_nodes()
    hiddenLayer.list_nodes()
    
