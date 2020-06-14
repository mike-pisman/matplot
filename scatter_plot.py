import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('youtube-data.csv')
views = data['view_count']
likes = data['likes']
ratio = data['ratio']



plt.scatter(views, likes, c=ratio, cmap='summer', edgecolor='black', linewidth=1, alpha=0.75)
plt.xscale('log')
plt.yscale('log')

cbar = plt.colorbar()
cbar.set_label('Like/Dislike ratio')

plt.title('Views to Likes ratio')
plt.xlabel('Total Views')
plt.ylabel('Total likes')

plt.tight_layout()

plt.show()
