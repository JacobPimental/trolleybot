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
                weights = line.split(" ")
                for w in range(0, len(weights)):
                    weights[w] = float( weights[w] )
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
                self.expected.append(float(parts[2]))
        self.input_layer = InputLayer( self.data[0], self.hidden_layers[0], allweights[0] )

    def train(self, act_func, deriv_func, cycles):
        for n in range( 0, cycles ):
            for i in range( 0, len(self.data)):
                
                for h in self.hidden_layers:
                    h.reset()
                self.endNode.reset()

                print( 'TESTING: ' + str( self.data[i][0] ) + ' ' + str( self.data[i][1] ) )
                self.input_layer.update_data( self.data[i] )
                self.input_layer.send_data()
            
                for h in self.hidden_layers:
                    h.send_data()
                print( 'GOT: ' + str(self.endNode.act_data) + ' EXPECTED: ' + str(self.expected[i]) )

                error = self.expected[i] - self.endNode.data
                deltaSum = deriv_func( self.endNode.act_data ) * error
                self.input_layer.backProp( deltaSum )
                for h in self.hidden_layers:
                    h.backProp( deltaSum )

def act_func( data ):
    ans = float( 1/(1 + math.pow(math.e, -data) ) )
    return ans
def deriv_func( data ):
    ans = act_func( data ) * ( 1 - act_func(data) )
    return ans

if __name__ == "__main__":
    myBrain = Brain( act_func, 2, "weights.txt", "train.txt")
    myBrain.train( act_func, deriv_func, 100000000 )

