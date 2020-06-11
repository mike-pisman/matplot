from matplotlib import pyplot as plt

plt.style.use("seaborn")

slices = [60, 40, 20, 10]
labels = ['Sixty', 'Forty', 'Twenty', 'Ten']
colors = ['#0000ff', 'red', 'green', 'yellow']
explode = [0, 0, 0, 0.1]
plt.pie(slices, labels = labels, colors = colors, explode=explode, shadow = True, startangle = 90, autopct = '%.2f%%', wedgeprops={'edgecolor': 'black'})

plt.title("My Pie Chart")
plt.tight_layout()
plt.show()
