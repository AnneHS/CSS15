from model_merge import EvacuationModel
from mesa.visualization.modules import CanvasHexGrid
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from mesa.visualization.UserParam import UserSettableParameter
from mesa.visualization.modules import ChartModule
from matplotlib import cm, colors

from agent_merge import Pedestrian, Wall

HEX = True

model_params = {
    "N": UserSettableParameter('slider', 'Population size', value=250, min_value=1, max_value=500),
    "height": 25,
    "width": 25,
    "hexogonal": HEX,
    "push_ratio": UserSettableParameter('slider', 'Push ratio', value=0.5, min_value=0, max_value=1, step=0.05),
    "fluster_factor": UserSettableParameter('slider', 'Fluster factor', value=0.5, min_value=0, max_value=1, step=0.05),
    "calm_factor": UserSettableParameter('slider', 'Calm factor', value=0.5, min_value=0, max_value=1, step=0.05),
}

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
    grid = CanvasHexGrid(agent_portrayal, 51, 51, 500, 500)
else:
    grid = CanvasGrid(agent_portrayal, 51, 51, 500, 500)

element_list = [grid, evacueesChart, evacuatedChart]

server = ModularServer(EvacuationModel, element_list, "Evacuation Model", {"N":150, "width":51, "height":51, "hexogonal": HEX})


server.port = 8422 # The default
server.launch()
