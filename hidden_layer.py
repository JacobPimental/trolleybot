#!/usr/bin/python3

from hidden_node import *
from synapses import *
import random

class HiddenLayer:
   
    weights = []
    myNodes = []
    act_func = None
    numNodes = 0
    nextLayer = None
    endNode = None

    def __init__(self, numNodes, act_func, endNode, nextLayer, weights=[]):
        self.weights = weights[:]
        self.numNodes = numNodes
        self.endNode = endNode
        self.act_func = act_func
        self.nextLayer = nextLayer
        self.init_nodes()

    def init_nodes(self):
        for i in range( 0, self.numNodes ):
            self.myNodes.append( HiddenNode( self.formulate_synapses(i), self.act_func) )

    def send_data(self):
        for n in self.myNodes:
            n.pass_through()

    def formulate_synapses(self, curNode):
        lst = []
        print( str( self.weights ) + " " + str( curNode ) )
        if not self.nextLayer == None:
            for n in range(0, len(self.nextLayer.myNodes)):
                if len( self.weights ) == 0:
                    lst.append( Synapse( random.random(), self.nextLayer.myNodes[n] ) )
                else:
                    lst.append( Synapse( self.weights[curNode][n], self.nextLayer.myNodes[n] ) )
        
        else:
            if len( self.weights ) == 0:
                lst.append( Synapse( random.random(), self.endNode ) )
            else:
                lst.append( Synapse( self.weights[curNode][0], self.endNode ) )

        return lst

    def list_nodes(self):
        for n in self.myNodes:
            print( n )


