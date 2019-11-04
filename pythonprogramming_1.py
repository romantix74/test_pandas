#C:\Users\ro\AppData\Local\Programs\Python\Python37\Scripts\;C:\Users\ro\AppData\Local\Programs\Python\Python37\;C:\Users\ro\AppData\Local\Programs\Python\Python35\Scripts\;C:\Users\ro\AppData\Local\Programs\Python\Python37\;C:\Users\ro\AppData\Local\Programs\Python\Python37\Scripts\;C:\Users\ro\AppData\Local\Programs\Python\Python37\;C:\Users\ro\AppData\Local\atom\bin
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2016, 1, 1)
end = dt.datetime.now()
df = web.DataReader("USD000UTSTOM", 'moex', start, end)
# df.reset_index(inplace=True)
# df.set_index("Date", inplace=True)
# df = df.drop("Symbol", axis=1)

print(df.head(10))

df.to_csv('TSLA.csv')
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
#df['Adj Close'].plot()
df.plot()
plt.show()