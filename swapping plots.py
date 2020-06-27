import numpy as np
import matplotlib.pyplot as plt
import math
import itertools


#change name 
'''
Used to create plots for variation in number of pedestrians.
'''

pushers = [0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1] # ratio of pushers
#push_prob = [0.1, 0.35, 0.6, 0.85, 1]    # for calm, flustered-push=0.5
push_prob = [0.1, 0.5, 1] # for flustered, calm-pushed = 1
ls = itertools.cycle(["-",":","--","-.",])
mark = itertools.cycle(["s", "8", "d", ">", "x"])
colors = itertools.cycle(["red", "green", "blue", "k", "violet"])
fig, ax = plt.subplots(1, 1, figsize=(7,5))
fig1, ax2 = plt.subplots(1, 1, figsize=(7,5))
fig2, ax3 = plt.subplots(1, 1, figsize=(7,5))
fig3, ax4 = plt.subplots(1, 1, figsize=(7,5))

for prob in push_prob:
    
    min_val = []
    min_std = []

    max_val = []
    max_std = []

    mean_val = []
    mean_std = []

    std_val = []
    std_std = []

    #if prob==0.1:
    #    p = [0.2, 0.4, 0.6, 0.8, 1]
    #else:
    #    p = [0.2, 0.4, 0.6, 0.8]
    l = next(ls)
    m = next(mark)
    col = next(colors) 

    for pusher in pushers:
        print(pusher, prob)
        # Load data
        if prob ==0.5:
            fileName = 'data/old/HEX100_N300_h25_w25_pr'+ str(pusher) + '_push1.npy'
            file = np.load(fileName)
        else:
            fileName = 'data/old/HEX100_N300_h25_w25_pr'+ str(pusher) + '_push_f'+ str(prob) +'.npy'
            file = np.load(fileName)

        # Mean, min, max and stds for each run for given parameters
        means = []
        mins = []
        maxs = []
        stds = []
        for line in file:
            means.append(np.mean(line))
            mins.append(min(line))
            maxs.append(max(line))
            stds.append(np.std(line))

        # Mean, min, max, std etc. for all runs for all parameters
        mean_val.append(np.mean(means))
        mean_std.append(np.std(means))

        std_val.append(np.mean(stds))
        std_std.append(np.std(stds))

        min_val.append(np.mean(mins))
        min_std.append(np.std(mins))

        max_val.append(np.mean(maxs))
        max_std.append(np.std(maxs))

        #if prob==0.1 and pusher==1:
        #    store = max_val[-1]
        #    print("hey, store", store)
        #elif prob!=0.1 and pusher==0.8:
        #    max_val.append(store)
        #    print(len(max_val))

    ax.plot(pushers, max_val, c=col, marker=m, markerfacecolor='k', markersize=6, ls=l, label="Push Prob = {}".format(prob))
    ax2.plot(pushers, mean_val, c=col, marker=m, markerfacecolor='k', markersize=6, ls=l, label="Push Prob = {}".format(prob))
    ax3.plot(pushers, std_val, c=col, marker=m, markerfacecolor='k', markersize=6, ls=l, label="Push Prob = {}".format(prob))
    ax4.plot(pushers, min_val, c=col, marker=m, markerfacecolor='k', markersize=6, ls=l, label="Push Prob = {}".format(prob))


    # Exit times histogram
    #plt.figure()
    #plt.hist(exit_data, bin_list, edgecolor="k")
    #plt.title(str(param) + ' Pedestrians')
    #plt.xlabel("Escape time")
    #plt.savefig('plots/pedestrians/escape_times_' + str(param))
    #plt.show()
ax.set_xlabel('Ratio of Pushers')
ax.set_ylabel('Maximum Escape Time')
ax2.set_xlabel('Ratio of Pushers')
ax2.set_ylabel('Mean Escape Time')
ax3.set_xlabel('Ratio of Pushers')
ax3.set_ylabel('Stan Dev Escape Time')
ax4.set_xlabel('Ratio of Pushers')
ax4.set_ylabel('Min Escape Time')
ax3.legend()
ax.legend()
ax2.legend()
ax4.legend()
fig.savefig('Max_flust_pushing_changed.png')
fig1.savefig('Mean_flust_pushing_changed.png')
fig2.savefig('std_flust_pushing_changed.png')
fig3.savefig('min_flust_pushing_changed.png')
plt.show()
# Plot mean, min, max, std etc.
#plt.figure()

