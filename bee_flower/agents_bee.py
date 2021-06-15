from mesa import Agent
from bee_flower.random_walk import RandomWalker
from bee_flower.random_stand import RandomStill


class Bee(RandomWalker):
    """
    A Bee that flies randomly, when sit on flower it produces honey and gain Energy
    """
    pylek = None

    def __init__(self, unique_id, pos, model, pylek = 0):
        super().__init__(unique_id, pos, model)
        self.pylek = pylek

    def step(self):

        self.random_move()

        # If there is grass available, eat it
        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        flower_patch = [obj for obj in this_cell if isinstance(obj, Flower_1)]
        if flower_patch:
            self.pylek += 1



class Honey(RandomStill):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)



class Flower_1(RandomStill):
    """
    Flower which give small portion of honey, can reproduce randomly and die after few steps
    """
    energy = None
    repr = 0

    def __init__(self, unique_id, pos, model, energy=None):
        super().__init__(unique_id, pos, model)
        self.energy = energy

    def step(self):
        living = True
        self.energy -= 1

        # If there is grass available, eat it
        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        bee_patch = [obj for obj in this_cell if isinstance(obj, Bee)]
        if bee_patch:
            self.energy += 50

        # Death
        if self.energy < 0:
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule.remove(self)
            living = False
        """
        elif self.random.random() + repr < self.model.flower_1_reproduce:
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            lamb = Flower_1(
                self.model.next_id(), (x,y), self.model, self.moore, self.energy
            )
            self.model.grid.place_agent(lamb, self.pos)
            self.model.schedule.add(lamb)
        """



class Flower_2(RandomStill):
    """
    Flower which give medium portion of honey, can reproduce randomly and die after few steps
    """
    energy = None

    def __init__(self, unique_id, pos, model, energy=None):
        super().__init__(unique_id, pos, model)
        self.energy = energy

    def step(self):
        living = True
        self.energy -= 1

        # If there is grass available, eat it
        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        bee_patch = [obj for obj in this_cell if isinstance(obj, Bee)]
        if bee_patch:
            self.energy += 50

        # Death
        if self.energy < 0:
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule.remove(self)
            living = False

class Flower_3(RandomStill):
    """
    Flower which give large portion of honey, can reproduce randomly and die after few steps
    """
    energy = None

    def __init__(self, unique_id, pos, model, energy=None):
        super().__init__(unique_id, pos, model)
        self.energy = energy

    def step(self):
        living = True
        self.energy -= 1

        # If there is grass available, eat it
        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        bee_patch = [obj for obj in this_cell if isinstance(obj, Bee)]
        if bee_patch:
            self.energy += 50

        # Death
        if self.energy < 0:
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule.remove(self)
            living = False


