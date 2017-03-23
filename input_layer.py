#!/usr/bin/python3 

from input_node import *

class InputLayer:
    
    myData = []
    myNodes = []
    numNodes = 0
    nextLayer = None

    def __init__(self, data, numNodes, nextLayer):
        self.myData = data
        self.numNodes = numNodes
        self.nextLayer = nextLayer
        self.init_nodes()

    def init_nodes(self):
        for i in range( 0, self.numNodes ):
            self.myNodes.append( InputNode( self.myData[i], self.formulate_synapses() ) )

    def formulate_synapses(self):
        lst = []
        for n in self.nextLayer.myNodes:
            lst.append( Synapse( random.random(), n ) )

        return lst

    def send_data(self):
        for n in self.myNodes:
            n.calculate()

    def list_nodes(self):
        for n in self.myNodes:
            print( n )

