import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page.lc_examPage import lc_exam
from time import sleep

'''
project:页面测试
'''

class TestLCloginExam(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.url = 'http://117.187.20.71:28080/lc_exam_web/page/manage/login_login.html'
		self.lc_exampage = lc_exam(self.driver, self.url, u'企业知识管理系统')
		self.lc_exampage.open()

	def test_direct_login(self):
		"""不输入任何信息点击登录"""
		try:
			self.lc_exampage.click_button()
			self.assertEqual(self.lc_exampage.get_checkback(), '手机号错误')
		except Exception as e:
			self.lc_exampage.img_screenshot(u'不输入任何信息点击登录')
			raise e
	def test_unpassword_login(self):
		"""不输入密码信息点击登录"""
		try:
			self.lc_exampage.input_account("18096074797")
			self.lc_exampage.click_button()
			self.assertEqual(self.lc_exampage.get_checkback(), '密码不能为空')
		except Exception as e:
			self.lc_exampage.img_screenshot(u'不输入密码信息点击登录')
			raise e
	def test_erroracount_login(self):
		"""输入错误账号信息点击登录"""
		try:
			self.lc_exampage.input_account("xxxxxxx")
			self.lc_exampage.click_button()
			self.assertEqual(self.lc_exampage.get_checkback(), '手机号错误')
		except Exception as e:
			self.lc_exampage.img_screenshot(u'输入错误账号信息点击登录')
			raise e
	def test_success_login(self):
		"""正确登录考试系统"""
		try:
			self.lc_exampage.input_account("18096074797")
			self.lc_exampage.input_password("074797")
			self.lc_exampage.click_button()
			self.assertEqual(self.lc_exampage.find_element(By.XPATH,('''//*[@id="lay-head"]/p''')).text, "企业知识管理系统"
			                                                                                      "")
		except Exception as e:
			self.lc_exampage.img_screenshot(u'正确登录考试系统')
			raise e

	def tearDown(self):
		self.driver.close()