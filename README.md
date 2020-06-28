# CSS15

The repository for this project can be found @ https://github.com/AnneHS/CSS15.git

It contains the following scripts needed to run our simulations:

agent_merge.py
model_merge.py
visualization_merge.py
main.py

The visualization file can be run as is to see a simulation of the evacuation. This is for a 2D grid using clustering of the agents at the opposite side of the exit. The merge follows can run either a hexagonal grid or a Moore grid. This is currently set to hexagonal grid; To change it to Moore, you can set HEX to false in line 13 of the file.

main.py is used to run multiple iterations of each simulation, and it in turn saves all the resulting data from it. The parameters within main are changed to set for number of iterations and parameter values. You can change N, which is the number of agents, pr, whch is the ratio of aggrevated pedestrians that push ahead on the grid, so called "pushers", which can swap places with the agents in front of them, and the specifications of the grid (h=height, w=width, and hex). The fluster and calm factor can also be changed in main as ff and fc.

The data files are automatically stored in the data folder. The plotting py's take the data from here and can be run to read in the files. The paths are changed manually, after the simulations. We suggest you to run the main and visualization to see that it works, and then run one of the plotting files to see the graphs from the data we produced.

The plots we produced are available in this submitted folder.

swap_2D.py plots the #of swaps per timestep in the 2D scenario with flustering and calming dynamics set to 0. The powerlaw fitting was obtained from this script but by uncommenting and commenting out the fit for the plot lines.

vis.py is to look plots the regression test on alpha for the powerlaw fits we performed and all the data we had available after our simulations.

Escape_time_push_flustered.py plots the escape times for mean max and stand dev of the crowd as the pushing probability of flustered agents increases.

1D can be set in model_merge from lines 27 to 34. You must uncomment the 1D and comment out the 2D.
