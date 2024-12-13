import math
import matplotlib.pyplot as plt
import numpy as np


times = 1
maxnum = int(input("max       : "))
run_times = int(input("run times : "))

c = 0
d = 1
a = 0
plot_x = [0]
pie_x = []





def detectPlot_x():
	if a in plot_x:
		return 0
	else:
		pie_x.insert(len(pie_x), a)
		





while c < run_times:
	b = math.lcm(maxnum, times, )
	a = b / times
	print(d, " : ", a, "times")
	detectPlot_x()
	plot_x.insert(len(plot_x), a)
	
	c += 1
	times += 1
	d += 1





max_plot_x = max(plot_x)

#plot
plt.subplot(1, 2, 1)
plt.plot(plot_x)
plt.ylim(0, max_plot_x)
plt.xlim(0, times)
plt.title("plot")


#pie

plt.subplot(1, 2, 2)
plt.pie(pie_x, labels= pie_x, autopct='%.1f%%')
plt.title("pie")



plt.show()