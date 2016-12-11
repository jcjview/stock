#!/usr/bin/python
#coding:utf8

"""
@version: 0.1
@author: jin_chongjiu
@license: 
@contact: 
@site: http://www.gowild.com
@software: PyCharm
@file: load_file.py
@time: 16/11/19 下午7:41
"""

def not_empty(s):
    return s and s.strip()



def load_stock(path):
    code=""
    name=""

    r=open(path)
    w=open(path.replace(".txt",".csv"),"w")
    count=-1
    for line in r:
        count+=1
        if count ==0 :
            line=line.replace(" ","\t").strip()
            lines=line.split("\t")
            lines1=filter(not_empty,lines)
            code=lines1[0]
            name=lines1[1]
            print code,name
        elif count==1:
            continue
        else:
            line = line.strip()
            lines = line.split(";")#日期	    开盘	    最高	    最低	    收盘	    成交量	    成交额
            l=",".join(lines)
            w.write(l+"\n")
    r.close()
    w.close()


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    path="../data/enter/SZ#300001.txt"
    load_stock(path)
    pass