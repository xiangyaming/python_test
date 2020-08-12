# -*- coding:utf-8 -*-
# @FileName  :login_page_locator.py
# @Time      :2020/7/14 0014 01:45
# @Author    :xiaoming
# -----------------------------------------------------
from selenium.webdriver.common.by import By


class LoginPageLocator:

   #用户名输入框
    username_text=(By.XPATH,'//input[@name="user"]')
   #密码输入框
    password_text=(By.XPATH,'//input[@name="pwd"]')
   #登录按钮
    login_button=(By.XPATH,'//button[@name="submit"]')