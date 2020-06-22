import numpy as np
import matplotlib.pyplot as plt
import math

'''
Used to create plots for variation in number of pedestrians.
'''

#params = [100, 150, 200, 250, 300, 350, 400, 450, 500] # Nr of agents
params = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1] # Push ratio

min_val = []
min_std = []

max_val = []
max_std = []

mean_val = []
mean_std = []

std_val = []
std_std = []

for param in params:

    # Load data
    fileName = 'data/HEX100_N300_h25_w25_pr' +  str(param) + '.npy'
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


    # HISTOGRAM
    data = file.flatten()
    exit_data = np.sort(data)

    # Exit times bins of size 5
    L = exit_data[-1]
    bin_size = 5
    min_edge = 0
    max_edge = math.ceil(L/bin_size) * bin_size
    N = int((max_edge-min_edge)/bin_size)
    Nplus1 = N+1
    bin_list = np.linspace(min_edge, max_edge, Nplus1)

    # Exit times histogram
    plt.figure()
    plt.hist(exit_data, bin_list, edgecolor="k")
    plt.title('Push ratio: ' + str(param))
    plt.xlabel("Escape time")
    variable_name = str(int(param * 10))
    print(variable_name)
    plt.savefig('plots/push_ratios/escape_times_' + variable_name)
    plt.show()

# Plot mean, min, max, std etc.
plt.figure()

#x = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
#x = [100, 150, 200, 250, 300, 350, 400, 450, 500] # Nr. of agent
x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1] # Push ratio

plt.plot(x, mean_val, color = 'black', label='mean')
plt.errorbar(x,mean_val, color = 'black',yerr = mean_std)

plt.plot(x, std_val, color = 'blue', label='std within run' )
plt.errorbar(x,std_val, color = 'blue', yerr = std_std)

plt.plot(x, max_val, color = 'red', label='max' )
plt.errorbar(x,max_val, color = 'red', yerr = max_std)

plt.plot(x, min_val, color = 'green', label='min' )
plt.errorbar(x,min_val, color = 'green', yerr = min_std)

plt.legend()
plt.xlabel('Push ratio')
plt.ylabel('escape time')
plt.savefig('plots/push_ratios/push_ratio_variation_values')
plt.show()
