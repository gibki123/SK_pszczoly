from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter

from bee_flower.agents_bee import Bee, Flower_1, Flower_2, Flower_3
from bee_flower.model import BeeFlower


def bee_flower_portrayal(agent):
    if agent is None:
        return

    portrayal = {}

    if type(agent) is Flower_1:
        portrayal["Shape"] = "bee_flower/resources/flower_1.png"
        portrayal["scale"] = 0.1
        portrayal["Layer"] = 0

    if type(agent) is Flower_2:
        portrayal["Shape"] = "bee_flower/resources/flower_2.png"
        portrayal["scale"] = 0.1
        portrayal["Layer"] = 0

    if type(agent) is Flower_3:
        portrayal["Shape"] = "bee_flower/resources/flower_3.png"
        portrayal["scale"] = 0.1
        portrayal["Layer"] = 0

    if type(agent) is Bee:
        portrayal["Shape"] = "wolf_sheep/resources/bee.png"
        portrayal["scale"] = 0.1
        portrayal["Layer"] = 1

    elif type(agent) is Wolf:
        portrayal["Shape"] = "wolf_sheep/resources/wolf.png"
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 2
        portrayal["text"] = round(agent.energy, 1)
        portrayal["text_color"] = "White"

    return portrayal


canvas_element = CanvasGrid(bee_flower_portrayal, 20, 20, 500, 500)
chart_element = ChartModule(
    [{"Label": "Wolves", "Color": "#AA0000"}, {"Label": "Sheep", "Color": "#666666"}]
)

model_params = {
    "grass": UserSettableParameter("checkbox", "Grass Enabled", True),
    "grass_regrowth_time": UserSettableParameter(
        "slider", "Grass Regrowth Time", 20, 1, 50
    ),
    "initial_sheep": UserSettableParameter(
        "slider", "Initial Sheep Population", 100, 10, 300
    ),
    "sheep_reproduce": UserSettableParameter(
        "slider", "Sheep Reproduction Rate", 0.04, 0.01, 1.0, 0.01
    ),
    "initial_wolves": UserSettableParameter(
        "slider", "Initial Wolf Population", 50, 10, 300
    ),
    "wolf_reproduce": UserSettableParameter(
        "slider",
        "Wolf Reproduction Rate",
        0.05,
        0.01,
        1.0,
        0.01,
        description="The rate at which wolf agents reproduce.",
    ),
    "wolf_gain_from_food": UserSettableParameter(
        "slider", "Wolf Gain From Food Rate", 20, 1, 50
    ),
    "sheep_gain_from_food": UserSettableParameter(
        "slider", "Sheep Gain From Food", 4, 1, 10
    ),
}

server = ModularServer(
    WolfSheep, [canvas_element, chart_element], "Wolf Sheep Predation", model_params
)
server.port = 8521
