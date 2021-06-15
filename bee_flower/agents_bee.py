from mesa import Agent
from bee_flower.random_walk import RandomWalker
from bee_flower.random_stand import RandomStill


class Bee(RandomWalker):
    """
    A Bee that flies randomly, and sits on flowers
    """

    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)

    def step(self):
        self.random_move()
        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        flower_patch = [obj for obj in this_cell if isinstance(obj, (Flower_1, Flower_2, Flower_3))]
        for i in flower_patch:
            i.repr += 0.01


class Flower_1(RandomStill):
    """
    Flower, can reproduce randomly and die after few steps
    """
    energy = None
    repr = 0

    def __init__(self, unique_id, pos, model, energy=None):
        super().__init__(unique_id, pos, model)
        self.energy = energy


    def step(self):
        living = True
        self.energy -= 1

        # Death
        if self.energy < 0:
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule.remove(self)
            living = False

        elif self.random.random() < self.model.flowers_1_reproduce:
            x = self.random.randrange(self.model.width)
            y = self.random.randrange(self.model.height)
            energy = self.random.randrange(*self.model.flowers_1_existance)
            lamb = Flower_1(
                self.model.next_id(), (x,y), self.model, energy
            )
            self.model.grid.place_agent(lamb, (x,y))
            self.model.schedule.add(lamb)


class Flower_2(RandomStill):
    """
    Flower, can reproduce randomly and die after few steps
    """
    energy = None
    repr = 0

    def __init__(self, unique_id, pos, model, energy=None):
        super().__init__(unique_id, pos, model)
        self.energy = energy

    def step(self):
        living = True
        self.energy -= 1

        # Death
        if self.energy < 0:
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule.remove(self)
            living = False

        elif self.random.random() < self.model.flowers_2_reproduce:
            x = self.random.randrange(self.model.width)
            y = self.random.randrange(self.model.height)
            energy = self.random.randrange(*self.model.flowers_2_existance)
            lamb = Flower_2(
                self.model.next_id(), (x, y), self.model, energy
            )
            self.model.grid.place_agent(lamb, (x, y))
            self.model.schedule.add(lamb)


class Flower_3(RandomStill):
    """
    Flower, can reproduce randomly and die after few steps
    """
    energy = None
    repr = 0

    def __init__(self, unique_id, pos, model, energy=None):
        super().__init__(unique_id, pos, model)
        self.energy = energy

    def step(self):
        living = True
        self.energy -= 1

        # Death
        if self.energy < 0:
            self.model.grid._remove_agent(self.pos, self)
            self.model.schedule.remove(self)
            living = False

        elif self.random.random() < self.model.flowers_3_reproduce:
            x = self.random.randrange(self.model.width)
            y = self.random.randrange(self.model.height)
            energy = self.random.randrange(*self.model.flowers_3_existance)
            lamb = Flower_3(
                self.model.next_id(), (x, y), self.model, energy
            )
            self.model.grid.place_agent(lamb, (x, y))
            self.model.schedule.add(lamb)
