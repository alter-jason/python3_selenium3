from selenium.webdriver.common.by import By

from common.Base_Page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from common.locator import get_locater


class lc_exam(BasePage):
	# 定位器
	yaml_name = 'li_exam'
	locator = get_locater(yaml_name).open1


	#   打开页面
	def open(self):
		self._open(self.url, self.title)
	# 输入账号
	def input_account(self,keywords):
		self.find_element(*self.locator("accoutn")).send_keys(keywords)
	#输入密码
	def input_password(self,keywords):
		self.find_element(*self.locator("pass_word")).send_keys(keywords)
	#点击登录
	def click_button(self):
		self.find_element(*self.locator("login_button")).click()
	#获取返回消息
	def get_checkback(self):
		Cresult = self.find_element(*self.locator("check_result")).text
		return Cresult