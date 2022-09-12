import random

class Node():
    def __init__(self, val):
        self.val = val
        self._generate_connections()
    
    def _generate_connections(self):
        self.connection_a = random.randint(-10, 10) / 10
        self.connection_b = random.randint(-10, 10) / 10
        self.connection_c = random.randint(-10, 10) / 10
        self.connection_d = random.randint(-10, 10) / 10
        self.connection_e = random.randint(-10, 10) / 10
        

class Layer1():
    pass


class NeuralNetwork():
    pass

