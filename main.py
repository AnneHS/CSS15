import sys
sys.path.append('code')

import pandas as pd

from model import EvacuationModel

def main(iter, N, h, w, pr):

    print("RUNNING Evacution model for " + str(iter) + ' ITERATION(S)\n' +
    "N: " + str(N) + "\n"
    "Height: " + str(h) + "\n"
    "Width: " + str(h) + "\n"
    "Push Ratio: " + str(pr))

    '''
    for i in range(iter):
        evacModel = EvacuationModel(N, w, h, pr)
        evacModel.step()
    '''

if __name__ == '__main__':
    main(iter=2, N=50, h=10, w=10, pr=0.5)
