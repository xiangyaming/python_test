import random
from selenium import webdriver
import os,time
# def imp(self, a):
#     a = self.driver.implicitly_wait(a)
#     return a
# s = imp(30)
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
de = webdriver.Chrome(r"E:\guge\chromedriver.exe")
de.maximize_window()
de.get(r"https://admin.zhaolaobao.com")
def imp(a):
    a = de.implicitly_wait(a)
    return a
s = imp(20)
de.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div[1]/input').send_keys('17611520838')
s
de.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/div[2]/input').send_keys('a123456')
s
de.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/button').click()
s
de.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/ul/li[1]/div').click()
s
de.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/ul/li[1]/ul/li[1]').click()
s
de.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/div[1]/div[4]/div/div/div/input').send_keys('阿萨德 8302 测试7185')
s
de.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/table/tr[2]/td[11]/a').click()
s
de.find_element_by_xpath('/html/body/div[9]/div[2]/div/div/div[3]/div/span[2]').click()

#de.find_element_by_css_selector('page-btn-blue').click()
# r.click('xpath','/html/body/div[131]/div[2]/div/div/div[3]/div/span[2]')