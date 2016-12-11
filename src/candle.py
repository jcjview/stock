#!/usr/bin/env python
# coding=utf-8

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from datetime import datetime,date
import time

from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY, YEARLY
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc,candlestick2_ochl

import numpy as np

def not_empty(s):
    return s and s.strip()


def cut_date(quotes, date1, date2):
    ret=[]
    for q in quotes:
        if date1<q[0]<date2:
            ret.append(q)
    return ret
def main(path):
    r = open(path)
    count = -1
    quotes=[]
    for line in r:
        try:
            count += 1
            if count == 0:
                line = line.replace(" ", "\t").strip()
                lines = line.split("\t")
                lines1 = filter(not_empty, lines)
                code = lines1[0]
                name = lines1[1]
                print code, name
            elif count == 1:
                continue
            else:
                line = line.strip()
                lines = line.split(";")  # 日期	    开盘	    最高	    最低	    收盘	    成交量	    成交额
                d= datetime.strptime(lines[0],'%Y/%m/%d')
                dates=time.mktime(d.timetuple())
                opens=float(lines[1])
                highs=float(lines[2])
                lows=float(lines[3])
                closes=float(lines[4])
                volume=float(lines[5])
                quotes.append((dates,opens,highs,lows,closes,volume))#Date,Open,High,Low,Close,Volume
        except ValueError as e:
            pass
    date1 = time.mktime(date(2015, 11, 1).timetuple())  # 起始日期，格式：(年，月，日)元组
    date2 = time.mktime(date(2015, 12, 10).timetuple())  # 结束日期，格式：(年，月，日)元组

    quotes = cut_date(quotes, date1, date2)#Date,Open,High,Low,Close,Volume,Adj Close

    dates = [q[0] for q in quotes]
    opens = [q[1] for q in quotes]
    highs=[q[2] for q in quotes]
    lows=[q[3] for q in quotes]
    closes=[q[4] for q in quotes]

    fig, ax = plt.subplots()

    fig.subplots_adjust(bottom=0.2)

    # ax.xaxis_date()

    ax.plot_date(dates, opens, '.')
    # candlestick_ohlc(ax, quotes, width=0.6, colorup='r', colordown='g')
    # candlestick2_ochl(ax, opens,closes,highs,lows,width=0.6, colorup='r', colordown='g')
    # ax.xaxis_date()
    # ax.autoscale_view()
    # plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

    ax.grid(True)
    plt.title(path)
    plt.show()
    return


if __name__ == '__main__':
    main("../data/enter/SZ#300001.txt")
