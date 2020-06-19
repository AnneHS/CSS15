import numpy as np
import matplotlib.pyplot as plt
import glob



names = ['data/HEX100_N300_h25_w25_pr0.5_f*_c0.1.np[yz]', 'data/HEX100_N300_h25_w25_pr0.5_f0.1_*.np[yz]','data/HEX100_N300_h25_w25_pr0.1_f*_c0.1.np[yz]' ]
#locs = [[32:35], [37:40]]
var_names = ['fluster = ', 'calm =', 'fluster = ']


for param in range(3):
	
	min_val = []
	min_std = []

	max_val = []
	max_std = []

	mean_val = []
	mean_std = []

	std_val = []
	std_std = []

	x = []
	for np_name in glob.glob(names[param]):
	    if param == 0 or param == 2:
	    	x.append(float(np_name[32:35]))
	    else:
	    	x.append(float(np_name[37:40]))

	    file = np.load(np_name)
	    
	    means = []
	    mins = []
	    maxs = []
	    stds = []
	    for line in file:
	    	means.append(np.mean(line))
	    	mins.append(min(line))
	    	maxs.append(max(line))
	    	stds.append(np.std(line))

	    mean_val.append(np.mean(means))
	    mean_std.append(np.std(means))

	    std_val.append(np.mean(stds))
	    std_std.append(np.std(stds))

	    min_val.append(np.mean(mins))
	    min_std.append(np.std(mins))

	    max_val.append(np.mean(maxs))
	    max_std.append(np.std(maxs))

	print(max_val)
	print(min_val)
	plt.figure()

	#x = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
	plt.plot(x, mean_val, color = 'black', label='mean')
	plt.errorbar(x,mean_val, color = 'black',yerr = mean_std)

	plt.plot(x, std_val, color = 'blue', label='std within run' )
	plt.errorbar(x,std_val, color = 'blue', yerr = std_std)

	plt.plot(x, max_val, color = 'red', label='max' )
	plt.errorbar(x,max_val, color = 'red', yerr = max_std)

	plt.plot(x, min_val, color = 'green', label='min' )
	plt.errorbar(x,min_val, color = 'green', yerr = min_std)

	plt.legend()
	plt.xlabel(var_names[param])
	plt.ylabel('escape time')
	plt.savefig(f'variation{param}_values.png')
	plt.show()


	bins = [i*15 for i in range(60)]
	
	plt.figure()
	al = 1.
	i = 1
	for np_name in glob.glob(names[param]):
		
		print(al)
		if param == 0:
			f = np_name[32:35]
		else:
			f = np_name[37:40]
		file = np.load(np_name)
		one_d = file.flatten()
		print(one_d)
		plt.subplot(3,4,i)
		plt.hist(one_d, bins, alpha = al, label = var_names[param] + f)
		i += 1
		#al -= 0.09
	
	plt.show()	

	# plt.legend()
	# plt.xlabel('escape time')
	# plt.savefig(f'hist{param}_values.png')
	# plt.show()

	i = 1
	for np_name in glob.glob(names[param]):
		
		print(al)
		if param == 0:
			f = np_name[32:35]
		else:
			f = np_name[37:40]
		file = np.load(np_name)
		differences = []
		for line in file:
			for v in range(len(line)):
				if v == 0:
					differences.append(v)
				else:
					differences.append(line[v] - line[v-1])

		plt.subplot(3,4,i)
		plt.hist(differences, label = var_names[param] + f)
		i += 1
		#al -= 0.09
	
	plt.show()

	# plt.legend()
	# plt.xlabel('escape time')
	# plt.savefig(f'difference_hist{param}_values.png')
	# plt.show()
