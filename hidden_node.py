class HiddenNode:
    
    synapses1 = []
    synapses2 = []
    act_func = None
    data = 0.0
    act_data = 0.0

    def __init__(self, synapses1, synapses2, act_func):
       
        self.act_func = act_func
        self.synapses1 = synapses1
        self.synapses2 = synapses2

        for s in self.synapses1:
            s.end = self
       
        for s in self.synapses2:
            s.start = self

    def retrieve_data(self, data):
        self.data += data
        self.act_data = self.act_func( self.data )

    def pass_through(self):
        for s in self.synapses2:
            s.pass_data( self.data )

    def __repr__(self):
        return "Hidden Node:\n\tData: " + str(self.data) + "\n\tSynapses " + str(self.synapses1) + " " + str(self.synapses2)
