import datetime
import pandas as pd
import numpy as np
import requests
import json
from pandas import json_normalize
import os

def outjson(a,b,c):
    jsonurl= a
    r = requests.get(jsonurl)
    data = r.json()
    f = open("{c}/{b}.json".format(c=c,b=b), "w")
    json.dump(data, f)
    f.close()
    print('done',b)
x = pd.read_csv("price.csv",header=0,encoding = "big5")
origin='https://twland.ronny.tw/index/search?lands[]='
temp=''
j=0
b=0
for i in range(415001,415031) :
    temp+=str(x['Address'][i])
    j+=1
    if j != 32 : temp+='&lands[]='
    if j == 32:
        k=str(x['Address'][i])
        b+=1
        j=0
        if b%200==1:
            p=x['Address'][i]
            os.mkdir(p)
        outjson(origin+temp,k[3::],p)
        temp=''