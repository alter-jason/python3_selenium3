import yaml
from common import log
from config import  proterty
from selenium.webdriver.common.by import By

class get_locater(object):
	def __init__(self,path):
		self.path = path
		self.mylog = log.log()
	def open1(self,key):
		path1 = proterty.locator_path + self.path+'.yaml'
		type_2 = By.ID
		try:
			sf =open(path1,'r', encoding='utf-8')
			f= yaml.load(sf.read())
		except Exception as e:
			self.mylog.info(u"打开读取yaml文件有误")
		try:
			#获取定位方式
			type_1 = f[key]['type']
			if type_1 =='id':
			    type_2 = By.ID
			elif type_1 =='xpath':
				type_2 = By.XPATH
			elif type_1 =='css':
				type_2 = By.CSS_SELECTOR
			elif type_1 =='text':
				type_2 = By.LINK_TEXT
			elif type_1 =='name':
				type_2 = By.NAME
			#获取元素信息
			value_1 = f[key]['value']
		except Exception as e:
			self.mylog.info(u"获取元素失败")
		return type_2, value_1
