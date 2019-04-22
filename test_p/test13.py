import os
from random import choice

from openpyxl import load_workbook

from test_p.Base import get_area
from test_p .Base import distance
import numpy as np
from datetime import datetime
project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)[0]), '.'))
print (project_path)
from math import radians, cos, sin, asin, sqrt

#计算两点间距离-m  经度 longitude 纬度 latitude
def geodistance(lng1,lat1,lng2,lat2):
    lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])
    dlon=lng2-lng1
    dlat=lat2-lat1
    a=sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    dis=2*asin(sqrt(a))*6371*1000
    return dis

TIME2=[]
mm = ['01','02','03','04','05','06','07','08','09']
while True:
	ss = '2019-2-06'+ ' ' + str(choice(range(7, 24))) + ':' + str(choice(range(00, 60)))
	if ss not in TIME2:
		TIME2.append(ss)
		print(len(ss))
	else:
		continue
	if len(TIME2) == 1000:
		break

arr = np.array(TIME2)
res = arr[np.argsort([datetime.strptime(i,'%Y-%m-%d %H:%M') for i in TIME2])].tolist()  #排序
print(res)
ss = sorted(TIME2)
print(len(TIME2))


#元数据
addr = r"C:\Users\ASUS\Desktop\aa.xlsx"

wb = load_workbook(addr)

ws = wb.get_sheet_by_name("phone")
#天数列表
TIME1 = ['2019-2-06','2019-2-07','2019-2-08','2019-2-09','2019-2-10','2019-2-11'
        , '2019-2-12']
# TIME2 = []
#黑车电话生成
heiphone = []
for i  in range(649,650):
    if i%10 ==0:
        heiphone.append("18096075"+str(i))
    elif i%10 ==1:
        heiphone.append("13381865"+str(i))
    elif i%10 ==2:
        heiphone.append("15140851"+str(i))
    elif i%10 ==3:
        heiphone.append("13980865"+str(i))
    elif i%10 ==4:
        heiphone.append("17780951"+str(i))
    elif i%10 ==5:
        heiphone.append("18180955"+str(i))
    else:
        heiphone.append("15680859"+str(i))
#取不重复的时间点
TIME2=[]
mm = ['01','02','03','04','05','06','07','08','09']
while True:
	ss = '2019-2-06'+ ' ' + str(choice(range(7, 24))) + ':' + str(choice(range(00, 60)))
	if ss not in TIME2:
		TIME2.append(ss)
		print(len(ss))
	else:
		continue
	if len(TIME2) == 1000:
		break

arr = np.array(TIME2)
res = arr[np.argsort([datetime.strptime(i,'%Y-%m-%d %H:%M') for i in TIME2])].tolist()  #排序
print(res)


	# print(len(TIME))
time1 = TIME2
for  x  in heiphone:
    for i in range(400):
        if i<=280:
            TIME = time1[i]
            phome =x
            positoin1 = "26.62"+str(choice(range(3441,8592)))+','+"106.6"+str(choice(range(76334,85328)))
            ws.append([phome, TIME, positoin1])
        else:
            TIME = time1[i]
            phome = x
            positoin1 = "26.6" + str(choice(range(33441, 77792))) + ',' + "106." + str(choice(range(595445, 706481)))
            ws.append([phome, TIME, positoin1])
wb.save(addr)
