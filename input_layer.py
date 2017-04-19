#!/usr/bin/python3 

from input_node import *

class InputLayer:
    
    myData = []
    myNodes = []
    numNodes = 0
    nextLayer = None
    weights = []

    def __init__(self, data, nextLayer, weights):
        self.myData = data
        self.numNodes = len( data ) 
        self.nextLayer = nextLayer
        self.weights = weights[:] 
        self.init_nodes()

    def update_data( self, newData ):
        self.myData = newData[:]
        for i in range( 0, len( newData ) ):
            self.myNodes[i].data = newData[i]

    def init_nodes(self):
        for i in range( 0, self.numNodes ):
            self.myNodes.append( InputNode( self.myData[i], self.formulate_synapses() ) )

    def formulate_synapses(self):
        lst = []
        for n in range(0, len(self.nextLayer.myNodes)):
            lst.append( Synapse( self.weights[n], self.nextLayer.myNodes[n] ) )

        return lst

    def send_data(self):
        for n in self.myNodes:
            n.calculate()

    def list_nodes(self):
        for n in self.myNodes:
            print( n )

    def backProp( self, deltaSum ):
        for s in self.myNodes:
            lst = []
            for n in self.nextLayer.myNodes:
                lst.append( deltaSum * float(s.data) )
            s.updateSynapses( lst )

