# The main element
class Hole:
    def __init__(self, volt, position=None):
        self.volt= volt
        self.position = position
    
    def walk(self, component):
        self.position = component.vin
        cost = component.activate(node, self.volt)
        if cost:
            self.position = component.gnd
            self.volt += cost


class Board:
    def __init__(self, row=4, col=4):
        # additional middle row
        row += 1
        self.charge = object()
        self.circuit = set()

        self.port = [[0 for c in range(col)] for i in range(row)]
        # populate middle row as ic devider
        self.port[row//2] = ['X' for _ in range(col)] 

    def vin(self, power, loc):
        self.charge = Hole(power, loc)

    def connect(self, component):
        vin = component.vin
        gnd = component.gnd
        if not self.port[vin[0]][vin[1]] and not self.port[gnd[0]][gnd[1]]:
            self.circuit.add(component)

    def activate(self):
        sr, sc = self.charge.position
        for component in self.circuit:
            if component.vin[0] == sr and component.vin[1] == sc:
                self.charge.walk(component)
                self.circuit.remove(component)
                er, ec = self.charge.position
                self.port[er][ec] = self.charge.volt
        
                
                
                

