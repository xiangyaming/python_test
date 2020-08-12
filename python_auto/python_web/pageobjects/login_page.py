# -*- coding:utf-8 -*-
# @FileName  :login_page.py
# @Time      :2020/7/14 0014 01:20
# @Author    :xiaoming
# -----------------------------------------------------
from python_web.pagelocator.login_page_locator import LoginPageLocator as loc

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC


class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    def login(self,username,password):
        #等待元素出现
       WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.username_text))
        #输入用户名
       self.driver.find_element(*loc.username_text).send_keys(username)
        #输入密码
       self.driver.find_element(*loc.password_text).send_keys(password)
        #点击登录
       self.driver.find_element(*loc.login_button).click()

