# from selenium import webdriver
# #
# # dr = webdriver.Firefox()
# # dr.get("https://www.baidu.com/")
# # ss= dr.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/a[2]').text
# # print(dr.title)
# import os
# from random import choice
#
# from openpyxl import load_workbook
#
# from test_p.Base import get_area
# from test_p .Base import distance
# import numpy as np
# from datetime import datetime
# project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)[0]), '.'))
# print (project_path)
# from math import radians, cos, sin, asin, sqrt
#
# #计算两点间距离-m  经度 longitude 纬度 latitude
# def geodistance(lng1,lat1,lng2,lat2):
#     lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])
#     dlon=lng2-lng1
#     dlat=lat2-lat1
#     a=sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
#     dis=2*asin(sqrt(a))*6371*1000
#     return dis
#
#
# print(geodistance(lng1 =float("106.611991"),lng2=float("106.616211"),lat1=float("26.631627"),lat2=float("26.629346")))
#
# # b=0
# # for i  in range(797,946):
# # 	print(i)
# # 	print(b)
# # 	b +=1
# lis = [1,2,3,4]
# print(lis.pop(1))
# print(lis)
# def describe_pet(animal_type, pet_name):
# 	""" 显示宠物的信息 """
# 	print("\nI have a " + animal_type + ".")
# 	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet('hamster', 'harry')
# describe_pet('xiaog','22d')
# ss = ('mushrooms', 'green peppers', 'extra cheese')
# print(ss[0])


class  Dog(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def sit(self):
		print(self.name.title()+ 'is now sitting')

	def roll_over(self):
		print(self.name.title() +'rolled over')

dog1 = Dog(name = '123',age = 1)
print(dog1.name)



class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.modle = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		long_name = str(self.year)+' '+self.make+' '+self.modle
		return  long_name

	def read_odometer(self):
		print('this  car has '+str(self.odometer_reading)+'miles on it')


mycar = Car('audi','1.6',2016)
mycar.make = 'dazhong'
print(mycar.get_descriptive_name())
mycar.odometer_reading = 100
mycar.read_odometer()

