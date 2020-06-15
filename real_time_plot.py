import pandas as pd
from itertools import count
import random
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn')

x = []
y = []

index = count()

def animate(i):
    data = pd.read_csv('data_gen.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()
    plt.plot(x,y1, label='Stock #1')
    plt.plot(x,y2, label='Stock #2')

    plt.legend(loc = 'upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
