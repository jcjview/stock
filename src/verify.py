import pandas as pd
import tushare as ts

from util.util import moving_average

df = pd.read_csv('../pe_pb_sort_all.csv', delimiter='\t')

print(df.head())
there_price = []
now_price = []
ma90list = []
min90list = []
for dates, row in df.iterrows():
    stock = str(row['code'])
    while len(stock) < len('600519'):
        stock = '0' + stock
    print(stock)
    df1 = ts.get_k_data(stock, ktype='D', start='2018-02-30', end='2018-06-30')
    close=[0]*30
    try:
        close=list(df1['close'].values)
    except:
        pass
    if not close:
        close=[0]*30
    # ma90 = moving_average(close, 30)
    try:
        print(close[0])
        print(close[-1])
    except :
        pass
    there_price.append(close[0])
    now_price.append(close[-1])
    max90=max(close)
    min90=min(close)
    ma90list.append(max90)
    min90list.append(min90)
    # break

df['there_price']=there_price
df['now_price']=now_price
df['max90']=ma90list
df['min90']=min90list

df.to_csv("verify.csv",index=False)