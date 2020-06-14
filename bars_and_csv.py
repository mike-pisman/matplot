from matplotlib import pyplot as plt
import numpy as np
import csv
import pandas as pd
from collections import Counter
#iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

#with open('iris.csv', 'r') as data_file:
#    reader = csv.DictReader(data_file)
#    sepal_length = Counter([row['sepal_length'] for row in reader])

plt.style.use("seaborn")

data  = pd.read_csv('iris.csv')
sepal_length = Counter(data['sepal_length'])

x, y = zip(*sepal_length.items())

plt.bar(tuple(map(str, x)), y, width = 0.1)


#plt.tight_layout()
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.title("Iris Data")

plt.show()
