from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter

from bee_flower.agents_bee import Bee, Flower_1, Flower_2, Flower_3, Honey
from bee_flower.model import BeeFlower


def bee_flower_portrayal(agent):
    if agent is None:
        return

    portrayal = {}

    if type(agent) is Flower_1:
        portrayal["Shape"] = "bee_flower/resources/flower_1.png"
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 0

    if type(agent) is Flower_2:
        portrayal["Shape"] = "bee_flower/resources/flower_2.png"
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 0

    if type(agent) is Flower_3:
        portrayal["Shape"] = "bee_flower/resources/flower_3.png"
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 0

    elif type(agent) is Bee:
        portrayal["Shape"] = "bee_flower/resources/bee.png"
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 1

    return portrayal


canvas_element = CanvasGrid(bee_flower_portrayal, 30, 30, 500, 500)
chart_element = ChartModule(
    [#{"Label": "Bee", "Color": "#AA0000"},
     {"Label": "Flower_1", "Color": "#666666"},
     {"Label": "Flower_2", "Color": "#AA4444"},
     {"Label": "Flower_3", "Color": "#AA8888"}]
)

model_params = {
    "initial_bees": UserSettableParameter(
        "slider", "Initial Bees Population", 50, 10, 200
    ),
    "initial_flowers_1": UserSettableParameter(
        "slider", "Initial Flowers_1 Population", 20, 5, 100
    ),
    "initial_flowers_2": UserSettableParameter(
        "slider", "Initial Flowers_2 Population", 20, 5, 100
    ),
    "initial_flowers_3": UserSettableParameter(
        "slider", "Initial Flowers_3 Population", 20, 5, 100
    ),
    "flowers_1_reproduce": UserSettableParameter(
        "slider", "Flowers_1 Reproduction Rate", 0.05, 0.01, 1.0, 0.01
    ),
    "flowers_2_reproduce": UserSettableParameter(
        "slider", "Flowers_2 Reproduction Rate", 0.05, 0.01, 1.0, 0.01
    ),
    "flowers_3_reproduce": UserSettableParameter(
        "slider", "flowers_3 Reproduction Rate", 0.05, 0.01, 1.0, 0.01
    ),
}

server = ModularServer(
    BeeFlower, [canvas_element, chart_element], "Bee Production", model_params
)
server.port = 8521
