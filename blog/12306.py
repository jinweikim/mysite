from stations import stations
import requests
import json
import pprint
import warnings
import ssl
str = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-11-10&leftTicketDTO.from_station=NJH&leftTicketDTO.to_station=BJP&purpose_codes=ADULT'
# f = input('请输入出发城市：\n')
# t = input('请输入到达城市:\n')
# d = input('请输入时间(格式：2017-02-08）：\n')
f = '昆山'
t = '南京'
d = '2017-11-13'
from_station = stations[f]
to_station = stations[t]
print(from_station)
print(to_station)
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
url = 'http://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date='+ d +'&leftTicketDTO.from_station='+from_station+'&leftTicketDTO.to_station='+to_station+'&purpose_codes=ADULT'
req = requests.get(url,verify = False,headers=headers)
# context = ssl._create_unverified_context()
# req = request.Request(url,headers=headers)
# r =request.urlopen(req,context=context)
# print(r.read())
# session = requests.session()
# file = open("/home/out.json","w")
# file.write(req)
dic = req.json()
data = dic['data']
maps = data['map']
# print(maps)
for key in data['result']:
    str = key
    id = str.split('|')[3]
    start = maps[str.split('|')[6]]
    dest = maps[str.split('|')[7]]
    time = str.split('|')[8]
    # print("车次号:" + id + " 出发站: " + start + " 目的站： " + dest + " 时间：" + time)

# trains = req.json()['data']
# print(data)
# for train in trains:
#     t = train[0]
    # print('车次：'+t['station_train_code']+' '+'出发站：'+t['from_station_name'] +' '+ '到达站: ' +t['to_station_name'])
# result = trains['result']
# print(result[0])

#NKH