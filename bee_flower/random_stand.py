"""
Generalized behavior for random walking, one grid cell at a time.
"""

from mesa import Agent


class RandomStill(Agent):
    """
    Class implementing random walker methods in a generalized manner.

    Not indended to be used on its own, but to inherit its methods to multiple
    other agents.

    """

    grid = None
    x = None
    y = None

    def __init__(self, unique_id, pos, model):
        """
        grid: The MultiGrid object in which the agent lives.
        x: The agent's current x coordinate
        y: The agent's current y coordinate
        """
        super().__init__(unique_id, model)
        self.pos = pos
