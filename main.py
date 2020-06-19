import sys
sys.path.append('code')
sys.path.append('data')

import pandas as pd
import numpy as np

from model_merge import EvacuationModel

def main(iter, N, h, w, hex, pr):

    number_of_agents = [100, 150, 200, 250, 300, 350, 400, 450, 500]
    for N in number_of_agents:

        print("RUNNING Evacution model for " + str(iter) + ' ITERATION(S)\n' +
        "N: " + str(N) + "\n"
        "Height: " + str(h) + "\n"
        "Width: " + str(h) + "\n"
        "Hexogonal: " + str(hex) + "\n"
        "Push Ratio: " + str(pr))

        exit_times = np.zeros((iter, N))
        for i in range(iter):
            evacModel = EvacuationModel(N, w, h, hex, pr)
            exit_times_current_run = evacModel.run_model()
            exit_times[i] = exit_times_current_run

        # Name of .npy file to save exit times.
        if hex:
            fileName = f'data/HEX{iter}_N{N}_h{h}_w{w}_pr{pr}.npy' # HexGrid
        else:
            fileName = f'data/MULTI{iter}_N{N}_h{h}_w{w}_pr{pr}.npy' # MultiGrid

        # Save exit_times of all runs to one .npy file
        np.save(fileName, exit_times)

if __name__ == '__main__':
    main(iter=100, N=50, h=25, w=25, hex=True, pr=0.5)
