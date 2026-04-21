from mininet.topo import Topo

class SimpleTopo(Topo):
    def build(self):
        # Add a single switch
        switch = self.addSwitch('s1')

        # Add three hosts 
        h1 = self.addHost('h1', ip='10.0.0.1')
        h2 = self.addHost('h2', ip='10.0.0.2')
        h3 = self.addHost('h3', ip='10.0.0.3')

        # Connect hosts to the switch
        self.addLink(h1, switch)
        self.addLink(h2, switch)
        self.addLink(h3, switch)

topos = {'simpletopo': (lambda: SimpleTopo())}
