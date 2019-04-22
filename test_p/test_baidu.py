import time

from selenium import webdriver
from selenium.webdriver import ActionChains

dr = webdriver.Firefox();
dr.get("https://www.baidu.com/")

elets = dr.find_element_by_link_text('登录')
action = ActionChains(dr)
action.click(elets).perform()
# action.click(elets).perform()
time.sleep(10)
dr.find_element_by_xpath("""//*[@id="TANGRAM__PSP_10__footerULoginBtn"]""").click()
