import sys
sys.path.append('code')
sys.path.append('data')

import pandas as pd
import numpy as np

from model_merge import EvacuationModel

def main(iter, N, h, w, hex, pr):

    push_ratio = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    
    for pr in push_ratio:

        print("RUNNING Evacution model for " + str(iter) + ' ITERATION(S)\n' +
        "N: " + str(N) + "\n"
        "Height: " + str(h) + "\n"
        "Width: " + str(h) + "\n"
        "Hexogonal: " + str(hex) + "\n"
        "Push Ratio: " + str(pr))

        swap_times = np.zeros((iter, 1500))
        for i in range(iter):
            evacModel = EvacuationModel(N, w, h, hex, pr) 
            swap_times_current_run = evacModel.run_model()[1]
            for a in swap_times_current_run:
                swap_times[i][a] += 1
            #swap_times[i] = swap_times_current_run
            
        #print(exit_times)
        # Name of .npy file to save exit times.
        #print(swap_times)
        if hex:
            fileName = f'data/HEX{iter}_N{N}_h{h}_w{w}_pr{pr}.npy' # HexGrid
        else:
            fileName = f'data/MULTI{iter}_N{N}_h{h}_w{w}_pr{pr}.npy' # MultiGrid

        # Save exit_times of all runs to one .npy file
        np.save(fileName, swap_times)

if __name__ == '__main__':
    N = [30,40,50,60,70,80,90,100,110,120,130,140]
    for i in N:
        main(iter=100, N=i, h=71, w=71, hex=True, pr=0.5)
