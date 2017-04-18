#!/usr/bin/python3 

from synapses import *
from hidden_node import *
from output_node import *
from hidden_layer import *
from input_layer import *
from input_node import *
import random
import math


class Brain:
    input_layer = None
    hidden_layers = []
    endNode = None
    expected = []
    data = []

    def __init__(self, act_func, numHiddenLayers, weight_text = "", train_text = ""):
        allweights = []
        numHiddenNodes = []
        if not weight_text == "":
            f = open( weight_text, 'r' )
            for line in f:
                weights = f.split(" ")
                allweights.append( weights )
        else:
            for i in range(0, numHiddenLayers):
                num = random.randint(1, 6)
                weights = []
                for i in range(0, num):
                    weights.append( random.random() )
                allweights.append( weights )


        for w in allweights:
            numHiddenNodes.append( len( w ) )

        self.endNode = OutputNode( act_func )
        self.hidden_layers = [None] * numHiddenLayers
        for i in range(numHiddenLayers - 1, -1, -1):
            if i == numHiddenLayers - 1:
                self.hidden_layers[i] = ( HiddenLayer( numHiddenNodes[i], act_func, self.endNode, None, allweights[i] ) )
            else:
                self.hidden_layers[i] = ( HiddenLayer( numHiddenNodes[i], act_func, self.endNode, self.hidden_layers[i+1], allweights[i] ) )
        
        if train_text == "":
            self.data = [[random.randint(0, 10), random.randint(0,10)]]
            print( 'Testing with inputs: ' + data[0] + ' ' + data[1] )

        else:
            f = open(train_text, 'r')
            for line in f:
                parts = line.split(' ')
                self.data.append([parts[0], parts[1]])
                self.expected.append(parts[2])
        self.input_layer = InputLayer( self.data[0], self.hidden_layers[0], allweights[0] )

    def train(self, act_func):
        for i in range( 0, len(self.data)):
            self.input_layer.update_data( self.data[i] )
            self.input_layer.list_nodes()
            self.input_layer.send_data()
            for h in self.hidden_layers:
                h.list_nodes()
                h.send_data()
            print( self.endNode )

def act_func( data ):
    ans = float( 1/(1 + math.pow(math.e, -data) ) )
    return ans

if __name__ == "__main__":
    myBrain = Brain( act_func, 1, "", "train.txt")
    myBrain.train( act_func )


