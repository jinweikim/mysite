from .stations import stations
import requests
from .models import Train

class train:

    f = ''
    t = ''
    d = ''

    def __init__(self,from_station,to_station,date):
        self.f = from_station
        self.t = to_station
        self.d = date

    def search(self):
        from_station = stations[self.f]
        to_station = stations[self.t]
        print(from_station)
        print(to_station)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
        url = 'http://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=' + self.d + '&leftTicketDTO.from_station=' + from_station + '&leftTicketDTO.to_station=' + to_station + '&purpose_codes=ADULT'
        req = requests.get(url, verify=False, headers=headers)
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
            train_id = str.split('|')[3]
            start = maps[str.split('|')[6]]
            dest = maps[str.split('|')[7]]
            time = str.split('|')[8]
            # train = Train()
            # train.train_id = train_id
            # train.start = start
            # train.dest = dest
            # train.time = time
            # train.save()
            # print("车次号:" + id + " 出发站: " + start + " 目的站： " + dest + " 时间：" + time)
            Train.objects.get_or_create(train_id=train_id,start=start,dest=dest,time=time,date=self.d)



