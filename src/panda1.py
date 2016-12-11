#!/usr/bin/python
# coding:utf8

"""
@version: 0.1
@author: jin_chongjiu
@license: 
@contact: 
@site: http://www.gowild.com
@software: PyCharm
@file: panda.py
@time: 16/11/19 下午8:14
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY, YEARLY
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc, candlestick2_ochl


# 定义产生分组索引的函数，比如我们要计算的周期是 20 天，则按照日期，20 个交易日一组
def gen_item_group_index(total, group_len):
    """ generate an item group index array

    suppose total = 10, unitlen = 2, then we will return array [0 0 1 1 2 2 3 3 4 4]
    """

    group_count = total / group_len
    group_index = np.arange(total)
    for i in range(group_count):
        group_index[i * group_len: (i + 1) * group_len] = i
    group_index[(i + 1) * group_len: total] = i + 1
    return group_index.tolist()


path = "../data/enter/SZ#300001.csv"
names = ['date',
         'opening_price',
         'ceiling_price',
         'floor_price',
         'closing_price',
         'volume',
         'amount']
# 读取数据时，我们以日期为索引，并解析成日期格式
qdhr = pd.read_csv(path, names=names, header=None, index_col='date', parse_dates=True)
l = len(qdhr)
start = qdhr.iloc[0:1].index.tolist()[0]
end = qdhr.iloc[l - 1: l].index.tolist()[0]
idx = pd.date_range(start=start, end=end)
# print idx
data = qdhr.reindex(idx)
zvalues = data.loc[~(data.volume > 0)].loc[:, ['volume', 'amount']]
data.update(zvalues.fillna(0))
data.fillna(method='ffill', inplace=True)

idx_name = data.index.name
dat = data.reset_index()[[idx_name, "Open", "High", "Low", "Close"]]
dat[data.index.name] = dat[data.index.name].map(mdates.date2num)
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter(fmt))
plt.xticks(rotation=45)
_ = candlestick_ohlc(ax, dat.values, width=.6, colorup='g', alpha=1)


DOCHLV = zip(Date, barsa.open, barsa.close, barsa.high, barsa.low, volume)
fig = plt.figure()
fig.subplots_adjust(bottom=0.1)
ax = fig.add_subplot(111)
plt.title("Candlestick chart")
candlestick_ohlc(ax, DOCHLV, width=0.6, colorup='g', colordown='r', alpha=1.0)
plt.show()
pass
