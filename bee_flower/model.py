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

from agents_bee.agents_bee import Bee, Flower_1, Flower_2, Flower_3
from agents_bee.schedule import RandomActivationByBreed


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
        flowers_1_reproduce=0.05,
        flowers_2_reproduce=0.05,
        flowers_3_reproduce=0.05,
    ):
        """
        Create a new Wolf-Sheep model with the given parameters.

        Args:
            initial_bees: Number of sheep to start with
            initial_flowers_1: Number of wolves to start with
            sheep_reproduce: Probability of each sheep reproducing each step
            wolf_reproduce: Probability of each wolf reproducing each step
            wolf_gain_from_food: Energy a wolf gains from eating a sheep
            grass: Whether to have the sheep eat grass for energy
            grass_regrowth_time: How long it takes for a grass patch to regrow
                                 once it is eaten
            sheep_gain_from_food: Energy sheep gain from grass, if enabled.
        """
        super().__init__()
        # Set parameters
        self.height = height
        self.width = width
        self.initial_bees = initial_bees
        self.initial_flowers_1 = initial_flowers_1
        self.initial_flowers_2 = initial_flowers_2
        self.initial_flowers_3 = initial_flowers_3
        self.flowers_1_reproduce = flowers_1_reproduce
        self.flowers_2_reproduce = flowers_2_reproduce
        self.flowers_3_reproduce = flowers_3_reproduce

        self.schedule = RandomActivationByBreed(self)
        self.grid = MultiGrid(self.height, self.width, torus=True)
        self.datacollector = DataCollector(
            {
                "Wolves": lambda m: m.schedule.get_breed_count(Wolf),
                "Sheep": lambda m: m.schedule.get_breed_count(Sheep),
            }
        )

        # Create sheep:
        for i in range(self.initial_bees):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            energy = self.random.randrange(2 * self.sheep_gain_from_food)
            sheep = Sheep(self.next_id(), (x, y), self, True, energy)
            self.grid.place_agent(sheep, (x, y))
            self.schedule.add(sheep)

        # Create wolves
        for i in range(self.initial_flowers_1):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            energy = self.random.randrange(2 * self.wolf_gain_from_food)
            wolf = Wolf(self.next_id(), (x, y), self, True, energy)
            self.grid.place_agent(wolf, (x, y))
            self.schedule.add(wolf)

        # Create grass patches
        if self.grass:
            for agent, x, y in self.grid.coord_iter():

                fully_grown = self.random.choice([True, False])

                if fully_grown:
                    countdown = self.grass_regrowth_time
                else:
                    countdown = self.random.randrange(self.grass_regrowth_time)

                patch = GrassPatch(self.next_id(), (x, y), self, fully_grown, countdown)
                self.grid.place_agent(patch, (x, y))
                self.schedule.add(patch)

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
                    self.schedule.get_breed_count(Wolf),
                    self.schedule.get_breed_count(Sheep),
                ]
            )

    def run_model(self, step_count=200):

        if self.verbose:
            print("Initial number wolves: ", self.schedule.get_breed_count(Wolf))
            print("Initial number sheep: ", self.schedule.get_breed_count(Sheep))

        for i in range(step_count):
            self.step()

        if self.verbose:
            print("")
            print("Final number wolves: ", self.schedule.get_breed_count(Wolf))
            print("Final number sheep: ", self.schedule.get_breed_count(Sheep))
