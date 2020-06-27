# CSS15

The repository for this project can be found @ https://github.com/AnneHS/CSS15.git

It contains the following scripts needed to run our simulations:

agent_merge.py
model_merge.py
visualization_merge.py
main.py

The merge follows can run either a hexagonal grid or a Moore grid.
The visualization file can be run as is to see a simulation of the evacuation. This is for a 2D grid using clustering at the other side of the exit and right now this is set to hexagonal grid, to change it to Moore, you can set HEX to false in line 13 of the file.

main.py is used to run multiple iterations of each simulation, and it in turn saves all the resulting data from it. The parameters within main are changed to set how for number of iterations and parameter values. Within it you can change N which is the number of agents, pr, whch is the ratio of "pushers" or aggrevated people that push, and the specifications of the grid (h=height, w=width, and hex). The fluster and calm factor have to be changed in model_merge.py in line 30.

The data files are automatically stored in the data folder. The plotting py's take the data from here and can be run to read in the files. The paths are changed manually, after the simulations. I suggest you to run the main and visualization to see that it works, and then run one of the plotting files to see it produces graphs from the data we produced.

The plots we also produced are available in this submitted folder.

swap_2D.py plots the #of swaps per timestep in the 2D scenario with flustering and calming dynamics set to 0.