from model_hexogonal import EvacuationModel
from mesa.visualization.modules import CanvasHexGrid
from mesa.visualization.ModularVisualization import ModularServer

from mesa.visualization.UserParam import UserSettableParameter
from mesa.visualization.modules import ChartModule
from matplotlib import cm, colors

from agent_hexogonal import Pedestrian, Wall, Exit

def agent_portrayal(agent):

    if type(agent) is Pedestrian:
        if agent.push > 0:
            portrayal = {"Shape": "circle",
                         "Filled": "true",
                         "Layer": 1,
                         "Color": "red",
                         "r": 0.5}
        else:
            portrayal = {"Shape": "circle",
                         "Filled": "true",
                         "Layer": 1,
                         "Color": "green",
                         "r": 0.5}
    elif type(agent) is Exit:
        portrayal = {"Shape": "hex",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": "yellow",
                     "r": 0.5}

    elif type(agent) is Wall:
        portrayal = {"Shape": "hex",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": "blue",
                     "r": 0.5}
    return portrayal

evacueesChart = ChartModule(
[{"Label": "Evacuees", "Color": "Red"}],
    data_collector_name='data_collector'
)

evacuatedChart = ChartModule(
[{"Label": "Evacuated", "Color": "Green"}],
    data_collector_name='data_collector'
)

grid = CanvasHexGrid(agent_portrayal, 25, 25, 500, 500)

element_list = [grid, evacueesChart, evacuatedChart]

server = ModularServer(EvacuationModel, element_list, "Evacuation Model", {"N":250, "width":25, "height":25})

'''
server = ModularServer(EvacuationModel,
                       [grid],
                       "Evacuation Model",
                       {"N":1, "width":11, "height":11})
'''
server.port = 8422 # The default
server.launch()
