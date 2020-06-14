import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mdates

plt.style.use('seaborn')

data = pd.read_csv('time_data.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace = True)

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle='solid')

# Get current figure, auto format to fate
plt.gcf().autofmt_xdate()

date_format = mdates.DateFormatter('%b, %d %Y')

#get current access, set date format
plt.gca().xaxis.set_major_formatter(date_format)

plt.tight_layout()
plt.title('Bitcoin Price')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()
