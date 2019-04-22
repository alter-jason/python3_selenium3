"""随机范围内生成经纬度数据"""

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
TIME1 = ['2019-2-06','2019-2-07','2019-2-08','2019-2-09','2019-2-10','2019-2-11'
        , '2019-2-12']
TIME2=[]
mm = ['01','02','03','04','05','06','07','08','09']
for i in range(7000):
	for  i in TIME1:
		ss = i+ ' ' + str(choice(range(7, 24))) + ':' + str(choice(range(00, 60)))
		if len(TIME2) ==7000:
			break
		if ss not in TIME2:
			TIME2.append(ss)
			# print(len(ss))
		else:
			continue
		if len(TIME2) ==7000:
			break

arr = np.array(TIME2)
res = arr[np.argsort([datetime.strptime(i,'%Y-%m-%d %H:%M') for i in TIME2])].tolist()  #排序
print(res)
print(len(res))

addr = r"C:\Users\ASUS\Desktop\aa.xlsx"

wb = load_workbook(addr)

ws = wb.get_sheet_by_name("phone")

heiphone = []
for i  in range(946,947):
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
time1 = res
for  x  in heiphone:
	# 初始经纬度
	lat1 = "26.6" + str(choice(range(10342, 55624)))  # 维度   106.656343,26.669144    106.655624,26.600342
	ln1 = "106." + str(choice(range(591234, 696012)))  # 经度   106.591234,26.635047   106.696012,26.626134
	for i in range(len(time1)):
		if i<=7000:
			TIME = time1[i]
			phome =x
			xi = True
			print(i)
			while xi:
				lat2 = "26.6" + str(choice(range(10342, 55624)))
				ln2 = "106." + str(choice(range(591234, 696012)))
				if geodistance(lng1 =float(ln1),lng2=float(ln2),lat1=float(lat1),lat2=float(lat2)) <= 500:
					positoin1 = ln2+','+lat2
					lat1 = lat2
					ln1 = ln2
					print(positoin1)
					ws.append([phome, TIME, positoin1])
					xi =False
				else:
					pass
		# else:
		# 	TIME = time1[i]
		# 	phome = x
		# 	positoin1 = "26.6" + str(choice(range(33441, 77792))) + ',' + "106." + str(choice(range(595445, 706481)))
		# 	ws.append([phome, TIME, positoin1])
wb.save(addr)