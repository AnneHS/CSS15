from model import EvacuationModel
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from agent import Pedestrian, Wall, Exit

def agent_portrayal(agent):

    if type(agent) is Pedestrian:
        portrayal = {"Shape": "circle",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": "red",
                     "r": 0.5}

    elif type(agent) is Wall:
        portrayal = {"Shape": "rect",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": "blue",
                     "w": 1,
                     "h": 1}

    elif type(agent) is Exit:
        portrayal = {"Shape": "rect",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": "white",
                     "w": 1,
                     "h": 1}
    return portrayal

grid = CanvasGrid(agent_portrayal, 21, 21, 500, 500)
server = ModularServer(EvacuationModel,
                       [grid],
                       "Evacuation Model",
                       {"N":22, "width":11, "height":11})
server.port = 8488 # The default
server.launch()
