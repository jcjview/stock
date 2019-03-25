#!/usr/bin/env python
# coding=utf-8

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from datetime import datetime,date
import time
import tushare as ts
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY, YEARLY, date2num
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc,candlestick2_ochl

import numpy as np

from util.util import moving_average


def not_empty(s):
    return s and s.strip()

def accu_price(price_change):
    accu = []
    value=1
    accu.append(1)
    for i in range(1,len(price_change)):
        value=value*(1+price_change[i]/100)
        accu.append(value)
    return accu
def diff_price(price):
    diff=[]
    diff.append(0)
    for i in range (1,len(price)):
        value=(price[i]-price[i-1])/price[i-1]*100
        diff.append(value)
    return diff
def cut_date(quotes, date1, date2):
    ret=[]
    for q in quotes:
        if date1<q[0]<date2:
            ret.append(q)
    return ret
def main(stock):
    hist_data = ts.get_hist_data(stock)
    quotes = []
    print(hist_data.head())
    hist_data.sort(columns ='')
    for dates, row in hist_data.iterrows():
        # 将时间转换为数字
        date_time = datetime.strptime(dates, '%Y-%m-%d')
        t = date2num(date_time)
        # open, high, low, close,volume = row[:5]
        # datas = (t, open, high, low, close,volume)
        quotes.append((t, row['open'], row['high'], row['low'], row['close'], row['volume'],row['p_change']))  # Date,Open,High,Low,Close,Volume

        # quotes.append(datas)

    date1 = date2num(date(2017, 9, 1)) # 起始日期，格式：(年，月，日)元组
    date2 = date2num(date(2018, 6, 1))  # 结束日期，格式：(年，月，日)元组
    quotes = cut_date(quotes, date1, date2)#Date,Open,High,Low,Close,Volume,Adj Close
    dates = [q[0] for q in quotes]
    opens = [q[1] for q in quotes]
    highs=[q[2] for q in quotes]
    lows=[q[3] for q in quotes]
    closes=[q[4] for q in quotes]
    price_change=[q[6] for q in quotes]

    # price_change=diff_price(closes)
    # accu=accu_price(price_change)
    # print(price_change)
    # print(accu)
    # print(closes)
    ma20 = moving_average(closes, 20)
    fig, ax = plt.subplots()

    fig.subplots_adjust(bottom=0.2)

    # ax.xaxis_date()
    ma5 = moving_average(closes, 5)
    ma30 = moving_average(closes, 30)
    # ax.plot_date(dates, accu, 'r-')
    ax.plot_date(dates, ma30, '-')
    candlestick_ohlc(ax, quotes, width=0.6, colorup='r', colordown='g')
    ax.grid(True)
    plt.title(stock)
    plt.show()
    return


if __name__ == '__main__':
    main("600519")
