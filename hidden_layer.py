#!/usr/bin/python3

from hidden_node import *
from synapses import *
import random

class HiddenLayer:
    
    myNodes = []
    act_func = None
    numNodes = 0
    nextLayer = None
    endNode = None

    def __init__(self, numNodes, act_func, endNode, nextLayer):
        self.numNodes = numNodes
        self.endNode = endNode
        self.act_func = act_func
        self.nextLayer = nextLayer
        self.init_nodes()

    def init_nodes(self):
        for i in range( 0, self.numNodes ):
            self.myNodes.append( HiddenNode( self.formulate_synapses(), self.act_func) )

    def send_data(self):
        for n in self.myNodes:
            n.pass_through()

    def formulate_synapses(self):
        lst = []
        if not self.nextLayer == None:
            for n in self.nextLayer.myNodes:
                lst.append( Synapse( random.random(), n ) )

        else:
            lst.append( Synapse( random.random(), self.endNode ) )

        return lst

    def list_nodes(self):
        for n in self.myNodes:
            print( n )


