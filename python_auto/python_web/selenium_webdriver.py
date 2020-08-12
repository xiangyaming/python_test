# -*- coding:utf-8 -*-
# @FileName  :selenium_webdriver.py
# @Time      :2020/6/24 0024 01:17
# @Author    :xiaoming
# -----------------------------------------------------

from  selenium import webdriver
from python_web.pageobjects.login_page import LoginPage
from python_web.pageobjects.cb_sys_page import HtDengji

driver = webdriver.Chrome()
driver.get('http://pomtest.cnfantasia.com/')

#调用类里面的函数，先实例化在调用，实例化要不要传参数，看有没有init函数
LoginPage(driver).login('mysoft','myy@2020')

HtDengji(driver).ht_page()
HtDengji(driver).new_ht("自动化测试合同")