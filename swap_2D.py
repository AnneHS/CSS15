import numpy as np
import matplotlib.pyplot as plt
import math
import itertools
import pandas as pd
import powerlaw

'''
Used to create plots for variation in number of pedestrians and the ratio of pushers.
'''


pushers = [0.3,0.5,0.7,1]
agents = [30,60,90,120]
ls = itertools.cycle(["-",":","--","-.",])
#mark = itertools.cycle(["s", "8", "d", ">", "x"])
colors = itertools.cycle(["red", "green", "blue", "coral", "violet", "grey"])

for push in pushers:
    #agents = [120]
    for N in agents:
        l = next(ls)
        #m = next(mark)
        col = next(colors)

        # Load data
        
        fileName = 'data/HEX100_N'+str(N)+'_h71_w71_pr'+ str(push) + '.npy'
        data = np.load(fileName)
        df = pd.DataFrame(data)
        
        mean_swaps = df.mean(axis = 0)
        std_swaps = df.std(axis=0)

        t = np.arange(0, len(mean_swaps), 1)
        plt.plot(t[0:350], mean_swaps[0:350], c=col, ls=l, label="N = {}".format(N))
        #plt.errorbar(t, std_swaps, yerr=std_swaps)
        #fit = powerlaw.Fit(mean_swaps[0:75],xmin=0,discrete=True)
        #fit.power_law.plot_pdf( color= 'k' ,linestyle=l, label='power-law fit')
        #fit.plot_pdf( color= col, label='original')
        #print('alpha= ',fit.power_law.alpha,'  sigma= ',fit.power_law.sigma)


    #plt.xlim(0,300)
    #plt.xscale('log')
    #plt.yscale('log')
    plt.ylabel("Swaps")
    plt.xlabel("Time in steps")
    plt.title("pusher's ratio={}".format(push))
    plt.legend()
    plt.savefig("swapping_ratio{}.png".format(push))
    plt.show()

    #ax.plot(pushers, max_val, c=col, marker=m, markerfacecolor='k', markersize=6, ls=l, label="Push Prob = {}".format(prob))
    #ax2.plot(pushers, mean_val, c=col, marker=m, markerfacecolor='k', markersize=6, ls=l, label="Push Prob = {}".format(prob))
    #ax3.plot(pushers, std_val, c=col, marker=m, markerfacecolor='k', markersize=6, ls=l, label="Push Prob = {}".format(prob))
   
