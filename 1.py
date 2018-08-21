import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

import datetime

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2013, 1, 27)

#f = web.DataReader('F', 'morningstar', start, end)
#print f.head()

f = web.DataReader('USD000UTSTOM', 'moex', start='2017-07-01', end='2017-07-31')
print f.head()

# import pandas_datareader as pdr
# import datetime 
# aapl = pdr.get_data_yahoo('AAPL', 
                          # start=datetime.datetime(2006, 10, 1), 
                          #end=datetime.datetime(2012, 1, 1))