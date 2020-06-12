from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

p1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
p2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
p3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['Player1', 'Player2', 'Player3']
colors = ['#6d904f', '#fc4f30', '#008fd5']

plt.stackplot(minutes, p1, p2, p3, labels=labels, colors=colors)

plt.title("My Stack Plot")
plt.legend(loc=(0.07, 0.05)) # plt.legend(loc = 'upper left')
plt.tight_layout()
plt.show()
