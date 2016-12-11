#!/usr/bin/python
#coding:utf8

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

# 定义产生分组索引的函数，比如我们要计算的周期是 20 天，则按照日期，20 个交易日一组
def gen_item_group_index(total, group_len):
    """ generate an item group index array

    suppose total = 10, unitlen = 2, then we will return array [0 0 1 1 2 2 3 3 4 4]
    """

    group_count = total / group_len
    group_index = np.arange(total)
    for i in range(group_count):
        group_index[i * group_len: (i + 1) * group_len] = i
    group_index[(i + 1) * group_len : total] = i + 1
    return group_index.tolist()

path="../data/enter/SZ#300001.csv"
names = ['date',
         'opening_price',
         'ceiling_price',
         'floor_price',
         'closing_price',
         'volume',
         'amount']
# 读取数据时，我们以日期为索引，并解析成日期格式
qdhr = pd.read_csv(path, names=names, header=None, index_col='date', parse_dates=True)
# print qdhr.head()
l = len(qdhr)
start = qdhr.iloc[0:1].index.tolist()[0]
end = qdhr.iloc[l - 1: l].index.tolist()[0]
idx = pd.date_range(start=start, end=end)
# print idx
data = qdhr.reindex(idx)
zvalues = data.loc[~(data.volume > 0)].loc[:, ['volume', 'amount']]
data.update(zvalues.fillna(0))
data.fillna(method='ffill', inplace=True)
# print data.head()
period = 30

group_index = gen_item_group_index(len(data), period)
# 把分组索引数据添加到股票数据里
data['group_index'] = group_index
print len(data)
data.head().append(data.tail())




pass