from matplotlib import pyplot as plt
import math
import numpy as np

#plt.style.use("seaborn")
#print(plt.style.available) #Show available styles

#plt.xkcd() #Comic style

#Create 3 lists of points
x = np.arange(-4*math.pi, 4*math.pi, math.pi/16)
sin_y = [math.sin(i) for i in x]
cos_y = [math.cos(i) for i in x]

#Plot lists
plt.plot(x,sin_y, color='#3bfa3e', linewidth=3, label='Sin(x)')
plt.plot(x,cos_y, label='Cos(x)')

#Display plot
plt.title("Sin/Cos graph") # Show name of the graph
plt.legend() #Show lables
plt.tight_layout() #Make the graph more accurate
plt.grid(True) #Show Grid

#plt.savefig('plot.png') #Save the plot as .png to current directory

plt.show()
