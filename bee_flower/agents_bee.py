from mesa import Agent
from bee_flower.random_walk import RandomWalker
from bee_flower.random_stand import RandomStill


class Bee(RandomWalker):
    """
    A Bee that flies randomly, when sit on flower it produces honey and gain Energy
    """
    energy = None

    def __init__(self, unique_id, pos, model, energy=None):
        super().__init__(unique_id, pos, model)
        self.energy = energy

    def step(self):
        self.random_move()



class Flower_1(RandomStill):
    """
    Flower which give small portion of honey, can reproduce randomly and die after few steps
    """
    energy = None

    def __init__(self, unique_id, pos, model, energy=None):
        super().__init__(unique_id, pos, model)
        self.energy = energy

class Flower_2(RandomStill):
    """
    Flower which give medium portion of honey, can reproduce randomly and die after few steps
    """
    energy = None

    def __init__(self, unique_id, pos, model, energy=None):
        super().__init__(unique_id, pos, model)
        self.energy = energy

class Flower_3(RandomStill):
    """
    Flower which give large portion of honey, can reproduce randomly and die after few steps
    """
    energy = None

    def __init__(self, unique_id, pos, model, energy=None):
        super().__init__(unique_id, pos, model)
        self.energy = energy
