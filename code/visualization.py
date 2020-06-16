from model import EvacuationModel
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from mesa.visualization.UserParam import UserSettableParameter
from mesa.visualization.modules import ChartModule
from matplotlib import cm, colors

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

evacueesChart = ChartModule(
[{"Label": "Evacuees", "Color": "Red"}],
    data_collector_name='data_collector'
)

evacuatedChart = ChartModule(
[{"Label": "Evacuated", "Color": "Green"}],
    data_collector_name='data_collector'
)

grid = CanvasGrid(agent_portrayal, 21, 21, 500, 500)

element_list = [grid, evacueesChart, evacuatedChart]

server = ModularServer(EvacuationModel, element_list, "Evacuation Model", {"N":20, "width":11, "height":11})

'''
server = ModularServer(EvacuationModel,
                       [grid],
                       "Evacuation Model",
                       {"N":1, "width":11, "height":11})
'''
server.port = 8421 # The default
server.launch()
