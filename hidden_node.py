class HiddenNode:
    
    synapses = []
    act_func = None
    data = 0.0
    act_data = 0.0

    def __init__(self, synapses, act_func):
        self.act_func = act_func
        self.synapses = synapses

    def retrieve_data(self, data):
        self.data += data
        self.act_data = self.act_func( self.data )

    def pass_through(self):
        for s in self.synapses:
            s.pass_data( self.act_data )

    def __repr__(self):
        return "Hidden Node:\n\tData: " + str(self.act_data) + "\n\tSynapses " + str(self.synapses)
