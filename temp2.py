import numpy as np
import matplotlib.pyplot as plt
import math
import itertools
import pandas as pd

'''
Used to create plots for variation in number of pedestrians.
'''
# change name to swapping plt


#pushers = [ 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1] # ratio of pushers
#N = [30,40,50,60,70,80,90,100,110,120]
pushers = [0.3,0.5,0.7,1]
agents = [30,60,90,120]
ls = itertools.cycle(["-",":","--","-.",])
mark = itertools.cycle(["s", "8", "d", ">", "x"])
colors = itertools.cycle(["red", "green", "blue", "k", "violet"])

for push in pushers:
    
    for N in agents:
        l = next(ls)
        m = next(mark)
        col = next(colors)

        print(push, N)
        # Load data
        
        fileName = 'data/HEX100_N'+str(N)+'_h71_w71_pr'+ str(push) + '.npy'
        data = np.load(fileName)
        df = pd.DataFrame(data)
        
        mean_swaps = df.mean(axis = 0)
        std_swaps = df.std(axis=0)

        t = np.arange(0, len(mean_swaps), 1)
        plt.plot(t, mean_swaps, c=col, marker=m, markerfacecolor='k', markersize=6, ls=l, label="N = {}".format(N))
        plt.errorbar(t, mean_swaps, yerr=std_swaps)

    plt.title("push ratio={}".format(push))
    plt.legend()
    plt.savefig("swapping_ratio{}.png".format(push))
    plt.show()

    #ax.plot(pushers, max_val, c=col, marker=m, markerfacecolor='k', markersize=6, ls=l, label="Push Prob = {}".format(prob))
    #ax2.plot(pushers, mean_val, c=col, marker=m, markerfacecolor='k', markersize=6, ls=l, label="Push Prob = {}".format(prob))
    #ax3.plot(pushers, std_val, c=col, marker=m, markerfacecolor='k', markersize=6, ls=l, label="Push Prob = {}".format(prob))
   
