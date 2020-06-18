from model_merge import EvacuationModel
from mesa.visualization.modules import CanvasHexGrid
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from mesa.visualization.UserParam import UserSettableParameter
from mesa.visualization.modules import ChartModule
from matplotlib import cm, colors

from agent_merge import Pedestrian, Wall

HEX = False

def agent_portrayal(agent):

    if type(agent) is Pedestrian:
        portrayal = {"Shape": "circle",
                     "Filled": "true",
                     "Layer": 1,
                     "Color": "red" if agent.push else "green",
                     "r": 0.5}


    elif type(agent) is Wall:
        if HEX:
            portrayal = {"Shape": "hex",
                         "Filled": "true",
                         "Layer": 0,
                         "Color": "blue",
                         "r": 0.5}
        else:
            portrayal = {"Shape": "rect",
                         "Filled": "true",
                         "Layer": 0,
                         "Color": "blue",
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

if HEX:
    grid = CanvasHexGrid(agent_portrayal, 21, 21, 500, 500)
else:
    grid = CanvasGrid(agent_portrayal, 21, 21, 500, 500)

element_list = [grid, evacueesChart, evacuatedChart]

server = ModularServer(EvacuationModel, element_list, "Evacuation Model", {"N":10, "width":10, "height":10, "hexogonal": HEX})


server.port = 8422 # The default
server.launch()
