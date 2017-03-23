#!/usr/bin/python3
from hidden_node import *
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
        
        init_nodes()

    def init_nodes(self):
        for i in range( 0, self.numNodes ):
            myNodes.append( HiddenNode( formulate_synapses(), self.act_func) )

    def send_data(self):
        for n in myNodes:
            n.pass_through

    def formulate_synapses(self):
        lst = []
        if not nextLayer == None:
            for n in nextLayer.myNodes:
                lst.append( Synapse( random.random(), n )





