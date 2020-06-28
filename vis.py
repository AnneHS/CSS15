import matplotlib.pyplot as plt
import numpy as np 
import powerlaw
from scipy import stats
fc = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]


def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth


all_values = np.zeros((len(fc), len(fc), 100, 1500))
for i in range(len(fc)):
	values = np.zeros((len(fc), 100, 1500))
	for j in range(len(fc)):
		file1Name = f'data/RIGHT/HEX100_N100_h71_w71_pr0.1_f{fc[i]}_c{fc[j]}.npy'

		all_values[i,j,:, :] = np.load(file1Name)



time_first_peak = np.zeros((11,11))
loc_first_peak = np.zeros((11,11))

time_second_peak = np.zeros((11,11))
loc_second_peak = np.zeros((11,11))



for i in range(len(fc)):
	
	#plt.figure()
	for j in range(len(fc)):
		vals = all_values[i,j,:,:500]
		mean = np.mean(vals, axis = 0)
		
		y_smooth = smooth(mean, 10)
		min_first = np.where(y_smooth==np.min(y_smooth[2:100]))[0][0]
		print(min_first)

		# get min_first peak
		max_1_y = np.max(mean[:min_first])
		max_1_x = np.where(mean == max_1_y)[0][0]
		
		time_first_peak[i,j] = max_1_x
		loc_first_peak[i,j] = max_1_y
		# get second peak
		
		
		y_smooth_cut = y_smooth[min_first:]
		max_y = np.max(y_smooth_cut) 
		
		max_x = np.where(y_smooth_cut==max_y)[0][0] + min_first

		time_second_peak[i,j] = max_x
		loc_second_peak[i,j] = max_1_y
		print(max_y, max_x)
		plt.plot(mean, alpha = 0.5, color = 'red', label=f'f{fc[i]} c{fc[j]}')
		plt.plot(y_smooth, alpha = 0.7, color = 'blue')
		plt.scatter([min_first],[4], s = 10)
		plt.scatter([max_x], [max_y], color = 'black', s= 10)
		plt.scatter([max_1_x], [max_1_y], color = 'green', s=10)
	plt.legend()
	#plt.show()	


# NAME = 0

# plt.figure()
# x = [i * 0.1 for i in range(1,11) ]
# print(x)
# for i in range(11):
# 	plt.scatter(x,time_second_peak[i,1:], label = str(i))
# 	plt.plot(x,time_second_peak[i,1:], alpha =0.1)
# 	plt.xscale('log')
# 	plt.yscale('log')
# 	plt.xlabel('calm factor')
# 	plt.ylabel('time of second peak')

# plt.legend()
# plt.savefig(f'Power{NAME}.png')
# NAME += 1
# plt.show()

# plt.figure()

# for i in range(11):
# 	plt.scatter(x,time_second_peak[1:, i], label = str(i))
# 	plt.plot(x,time_second_peak[1:,i], alpha =0.1)
# 	plt.xscale('log')
# 	plt.yscale('log')
# 	plt.xlabel('fluster factor')
# 	plt.ylabel('time of second peak')
# 	fit = powerlaw.Fit(mean_swaps[0:75],discrete=True)

# plt.legend()
# plt.savefig(f'Power{NAME}.png')
# NAME += 1
# plt.show()


plt.figure()
x = np.array([i*0.1 for i in range(1,11)])
print(x)

def lingres(dots, slope, intercept):
	
	return np.exp(slope * np.log(dots) + intercept)  

for i in range(0,11,3):
	plt.scatter(x,loc_second_peak[1:, i ], label = 'calming factor =' + str(fc[i]))
	slope, intercept, r_value, p_value, std_err = stats.linregress(np.log(x[:-1]),np.log(loc_second_peak[1:-1,i]))
	print(np.log(x[:-1]),np.log(loc_second_peak[i,1:-1]))
	print(slope, intercept)
	dots = np.linspace(0.1,1,1000)
	plt.plot(x[:-1], lingres(x[:-1], slope, intercept))
	plt.xscale('log')
	plt.yscale('log')
	plt.xlabel('fluster factor')
	plt.ylabel('height of second peak')
	print(p_value)
plt.legend()
plt.savefig(f'Power_final.png')
#NAME += 1
plt.show()




# z=np.arange(1, len(x)+1) #start at 1, to avoid error from log(0)

# logA = np.log(z) #no need for list comprehension since all z values >= 1
# logB = np.log(y)

# m, c = np.polyfit(logA, logB, 1) # fit log(y) = m*log(x) + c
# y_fit = np.exp(m*logA + c) # calculate the fitted values of y 

# plt.plot(z, y, color = 'r')
# plt.plot(z, y_fit, ':')

# plt.figure()

# for i in range(11):
# 	plt.scatter(x,loc_second_peak[1:, i], label = str(0.1 * i))
# 	plt.plot(x,loc_second_peak[1:,i], alpha =0.1)
# 	plt.xscale('log')
# 	plt.yscale('log')
# 	plt.xlabel('fluster factor')
# 	plt.ylabel('height of second peak')
# plt.legend()
# plt.savefig(f'Power{NAME}.png')
# NAME += 1
# plt.show()


# plt.figure()
# for i in range(11):
# 	plt.scatter(x,loc_first_peak[i,1:], label = str(i))
# 	plt.plot(x,loc_first_peak[i,1:], alpha =0.1)
# 	plt.xscale('log')
# 	plt.yscale('log')
# 	plt.xlabel('calm factor')
# 	plt.ylabel('height of first peak')
# plt.legend()
# plt.savefig(f'Power{NAME}.png')
# NAME += 1
# plt.show()

# plt.figure()

# for i in range(11):
# 	plt.scatter(x,loc_first_peak[1:, i], label = str(0.1 * i))
# 	plt.plot(x,loc_first_peak[1:,i], alpha =0.1)
# 	plt.xscale('log')
# 	plt.yscale('log')
# 	plt.xlabel('fluster factor')
# 	plt.ylabel('height of first peak')
# plt.legend()
# plt.savefig(f'Power{NAME}.png')
# NAME += 1
# plt.show()


# plt.figure()
# x = [i * 0.1 for i in range(1,11) ]
# print(x)
# for i in range(11):
# 	plt.scatter(x,time_first_peak[i,1:], label = str(i))
# 	plt.plot(x,time_first_peak[i,1:], alpha =0.1)
# 	plt.xscale('log')
# 	plt.yscale('log')
# 	plt.xlabel('calm factor')
# 	plt.ylabel('time of first peak')
# plt.legend()
# plt.savefig(f'Power{NAME}.png')
# NAME += 1
# plt.show()

# plt.figure()

# for i in range(11):
# 	plt.scatter(x,time_first_peak[1:, i], label = str(i))
# 	plt.plot(x,time_first_peak[1:,i], alpha =0.1)
# 	plt.xscale('log')
# 	plt.yscale('log')
# 	plt.xlabel('fluster factor')
# 	plt.ylabel('time of first peak')
# plt.legend()
# plt.savefig(f'Power{NAME}.png')
# NAME += 1
# plt.show()

# col = 'green'

# for i in range(11):
# 	# try:
# 	# 	fit = powerlaw.Fit(time_second_peak[i,:],discrete=True)
# 	# 	fit.power_law.plot_pdf( color= 'k' ,linestyle='-', label='fit ccdf')
# 	# 	fit.plot_pdf( color= col, label='original')
# 	# 	print('alpha= ',fit.power_law.alpha,'  sigma= ',fit.power_law.sigma)
# 	# 	plt.show()
# 	# except:
# 	# 	pass
# 	# try:
# 	# 	fit = powerlaw.Fit(time_second_peak[:,i],discrete=True)
# 	# 	fit.power_law.plot_pdf( color= 'k' ,linestyle='-', label='fit ccdf')
# 	# 	fit.plot_pdf( color= col, label='original')
# 	# 	print('alpha= ',fit.power_law.alpha,'  sigma= ',fit.power_law.sigma)
# 	# 	plt.show()
# 	# except:
# 	# 	pass
# 	try:
# 		fit = powerlaw.Fit(loc_second_peak[i,:],discrete=True)
# 		fit.power_law.plot_pdf( color= 'k' ,linestyle='-', label='fit ccdf')
# 		fit.plot_pdf( color= col, label='original')
# 		print('alpha= ',fit.power_law.alpha,'  sigma= ',fit.power_law.sigma)
# 		plt.show()
# 	except:
# 		pass
# 	try:
# 		fit = powerlaw.Fit(loc_second_peak[:,i],discrete=True)
# 		fit.power_law.plot_pdf( color= 'k' ,linestyle='-', label='fit ccdf')
# 		fit.plot_pdf( color= col, label='original')
# 		print('alpha= ',fit.power_law.alpha,'  sigma= ',fit.power_law.sigma)
# 		plt.show()
# 	except:
# 		pass
# plt.figure()

# for i in range(11):
# 	plt.scatter(x,loc_second_peak[i,:], label = str(i))
# 	plt.xscale('log')
# 	plt.yscale('log')
# plt.legend()
# plt.show()

# plt.figure()

# for i in range(11):
# 	plt.scatter(x,loc_second_peak[:, i], label = str(i))
# 	plt.xscale('log')
# 	plt.yscale('log')
# plt.legend()
# plt.show()

# plt.figure()

# for i in range(11):
# 	plt.scatter(x,time_first_peak[i,:], label = str(i))
# 	plt.xscale('log')
# 	plt.yscale('log')
# plt.legend()
# plt.show()

# plt.figure()

# for i in range(11):
# 	plt.scatter(x,time_first_peak[:,i], label = str(i))
# 	plt.xscale('log')
# 	plt.yscale('log')
# plt.legend()
# plt.show()

# plt.figure()

# for i in range(11):
# 	plt.scatter(x,loc_first_peak[i,:], label = str(i))
# plt.legend()
# plt.show()

# plt.figure()

# for i in range(11):
# 	plt.scatter(loc_first_peak[:, i], label = str(i))
# plt.legend()
# plt.show()


# plt.figure()
# x = [i*0.1 for i in range(11) ]
# for i in range(11):
# 	plt.scatter(x,time_second_peak[i,:], label = str(i))
# plt.legend()
# plt.show()

# plt.figure()

# for i in range(11):
# 	plt.plot(x,time_second_peak[:,i], label = str(i))
# plt.legend()
# plt.show()

# plt.figure()

# for i in range(11):
# 	plt.scatter(x,loc_second_peak[i,:], label = str(i))
# plt.legend()
# plt.show()

# plt.figure()

# for i in range(11):
# 	plt.scatter(x,loc_second_peak[:, i], label = str(i))
# plt.legend()
# plt.show()

# plt.figure()

# for i in range(11):
# 	plt.scatter(x,time_first_peak[i,:], label = str(i))
# 	plt.xscale('log')
# 	plt.yscale('log')
# plt.legend()
# plt.show()

# plt.figure()

# for i in range(11):
# 	plt.scatter(x,time_first_peak[:,i], label = str(i))
# 	plt.xscale('log')
# 	plt.yscale('log')
# plt.legend()
# plt.show()

# plt.figure()

# for i in range(11):
# 	plt.scatter(loc_first_peak[i,:], label = str(i))
# 	plt.xscale('log')
# 	plt.yscale('log')
# plt.legend()
# plt.show()

# plt.figure()

# for i in range(11):
# 	plt.scatter(loc_first_peak[:, i], label = str(i))
# 	plt.xscale('log')
# 	plt.yscale('log')
# plt.legend()
# plt.show()