from selenium.webdriver.common.by import By

from common.Base_Page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from common.locator import get_locater

class BaiduPage(BasePage):
	 # 定位器
    yaml_name = 'baidu_loginPage'
    locator = get_locater(yaml_name).open1
    #   打开页面
    def open(self):
        self._open(self.url, self.title)

    #   输入关键词
    def input_keywords(self, keywords):
        self.find_element(*self.locator("keywords_loc")).send_keys(keywords)

            # self.find_element()

    #   点击搜索按钮
    def click_submit(self):
        self.find_element(*self.locator("submit_loc")).click()

    #   点击pthon百科链接
    def click_python_known(self):
        self.find_element(By.XPATH,'//*[@id="2"]/h3/a/em').click()

    def title_python_known(self):
	     return  self.driver.title

    #点击登录
    def click_login(self):
        elets = self.find_element(*self.locator('login_loc'))
        action = ActionChains(self.driver)
        action.click(elets).perform()
    #点击账号登录
    def click_log_name(self):
        self.find_element(*self.locator("login_mo")).click()