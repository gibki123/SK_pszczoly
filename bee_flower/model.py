"""
Wolf-Sheep Predation Model
================================

Replication of the model found in NetLogo:
    Wilensky, U. (1997). NetLogo Wolf Sheep Predation model.
    http://ccl.northwestern.edu/netlogo/models/WolfSheepPredation.
    Center for Connected Learning and Computer-Based Modeling,
    Northwestern University, Evanston, IL.
"""

from mesa import Model
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from bee_flower.agents_bee import Bee, Flower_1, Flower_2, Flower_3, Honey
from bee_flower.schedule import RandomActivationByBreed


class BeeFlower(Model):
    """
    Wolf-Sheep Predation Model
    """

    height = 30
    width = 30

    initial_bees = 50
    initial_flowers_1 = 20
    initial_flowers_2 = 20
    initial_flowers_3 = 20

    flowers_1_reproduce = 0.05
    flowers_2_reproduce = 0.05
    flowers_3_reproduce = 0.05

    flowers_1_existance = (10,20)
    flowers_2_existance = (10,20)
    flowers_3_existance = (10,20)

    initial_honey = 1

    verbose = False  # Print-monitoring

    description = (
        "A model for simulating bee productive power based on flower species accumulation."
    )

    def __init__(
        self,
        height=30,
        width=30,
        initial_bees=50,
        initial_flowers_1=20,
        initial_flowers_2=20,
        initial_flowers_3=20,
        initial_honey=1,
        flowers_1_reproduce=0.05,
        flowers_2_reproduce=0.05,
        flowers_3_reproduce=0.05,
        flowers_1_existance=(10,20),
        flowers_2_existance=(10,20),
        flowers_3_existance=(10,20),
    ):
        """
        Create a new Wolf-Sheep model with the given parameters.

        Args:
            initial_bees: Number of bees to start with
            initial_flowers_1: Number of flowers_1 to start with
            initial_flowers_2: Number of flowers_2 to start with
            initial_flowers_3: Number of flowers_3 to start with
            flowers_1_reproduce: Probability of each flower reproducing each step
            flowers_2_reproduce: Probability of each flower reproducing each step
            flowers_3_reproduce: Probability of each flower reproducing each step
            flowers_1_existance: Step range of flower existance
            flowers_2_existance: Step range of flower existance
            flowers_3_existance: Step range of flower existance
        """
        super().__init__()
        # Set parameters
        self.height = height
        self.width = width
        self.initial_bees = initial_bees
        self.initial_flowers_1 = initial_flowers_1
        self.initial_flowers_2 = initial_flowers_2
        self.initial_flowers_3 = initial_flowers_3
        self.initial_honey = initial_honey
        self.flowers_1_reproduce = flowers_1_reproduce
        self.flowers_2_reproduce = flowers_2_reproduce
        self.flowers_3_reproduce = flowers_3_reproduce
        self.flowers_1_existance = flowers_1_existance
        self.flowers_2_existance = flowers_2_existance
        self.flowers_3_existance = flowers_3_existance

        self.schedule = RandomActivationByBreed(self)
        self.grid = MultiGrid(self.height, self.width, torus=True)
        self.datacollector = DataCollector(
            {
                "Bee": lambda m: m.schedule.get_breed_count(Bee),
                "Flower_1": lambda m: m.schedule.get_breed_count(Flower_1),
                "Flower_2": lambda m: m.schedule.get_breed_count(Flower_2),
                "Flower_3": lambda m: m.schedule.get_breed_count(Flower_3),
                "Honey": lambda m: m.schedule.get_breed_count(Honey),
            }
        )

        # Create Flower_1:
        for i in range(self.initial_flowers_1):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            energy = self.random.randrange(*self.flowers_1_existance)
            flower = Flower_1(self.next_id(), (x, y), self, energy)
            self.grid.place_agent(flower, (x, y))
            self.schedule.add(flower)

        # Create Flower_2:
        for i in range(self.initial_flowers_2):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            energy = self.random.randrange(*self.flowers_2_existance)
            flower = Flower_2(self.next_id(), (x, y), self, energy)
            self.grid.place_agent(flower, (x, y))
            self.schedule.add(flower)

        # Create Flower_3:
        for i in range(self.initial_flowers_3):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            energy = self.random.randrange(*self.flowers_3_existance)
            flower = Flower_3(self.next_id(), (x, y), self, energy)
            self.grid.place_agent(flower, (x, y))
            self.schedule.add(flower)

        # Create Bee:
        for i in range(self.initial_bees):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            self.pylek = 0
            bee = Bee(self.next_id(), (x, y), self)
            self.grid.place_agent(bee, (x, y))
            self.schedule.add(bee)

        self.running = True
        self.datacollector.collect(self)

    def step(self):

        self.schedule.step()
        # collect data
        self.datacollector.collect(self)
        if self.verbose:
            print(
                [
                    self.schedule.time,
                    self.schedule.get_breed_count(Bee),
                    self.schedule.get_breed_count(Flower_1),
                    self.schedule.get_breed_count(Flower_2),
                    self.schedule.get_breed_count(Flower_3),
                ]
            )





    def run_model(self, step_count=200):
        for i in range(step_count):
            self.step()


