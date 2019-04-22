import unittest
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.Base_Page import BasePage
from page.baidu_loginPage import BaiduPage
from time import sleep

'''
project:百度页面测试
'''


class TestBaiduSearch(unittest.TestCase):
    def setUp(self):  #
        self.driver = webdriver.Firefox()
        self.url = 'https://www.baidu.com/'
        # self.keyword = 'python'
        self.baidu_page = BaiduPage(self.driver, self.url, u'百度')

    def test_baidu_search(self):
        u'''百度搜索'''
        try:
            self.baidu_page.open()
            self.baidu_page.input_keywords('python')
            self.baidu_page.click_submit()
            self.baidu_page.click_python_known()
            sleep(1)
            self.baidu_page.next_window()
            print(self.baidu_page.title_python_known())
            self.assertIn(self.driver.title, 'Python（计算机程序设计语言）_百度百科')
        except Exception as e:
            self.baidu_page.img_screenshot(u'百度搜索')
            raise e




    def tearDown(self):
        self.driver.quit()