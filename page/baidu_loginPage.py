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

    #   鼠标悬停在"更多产品"上
    def ActionChains_more(self):
        mouse = self.find_element(*self.more_loc)
        ActionChains(self.driver).move_to_element(mouse).perform()

    #   点击“全部产品”
    def click_zhidao(self):
        self.find_element(*self.zhidao_loc).click()