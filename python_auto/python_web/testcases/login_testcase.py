# -*- coding:utf-8 -*-
# @FileName  :login_testcase.py
# @Time      :2020/7/15 0015 01:48
# @Author    :xiaoming
# -----------------------------------------------------

import unittest
from selenium import webdriver
from python_web.pageobjects.login_page import LoginPage

class LoginTest():
    #前置：每条用例执行前，驱动一个浏览器，并打开网址
    def setup(self):
        self.drver = webdriver.Chrome()
        self.drver.get('http://pomtest.cnfantasia.com/')
    #后置：每条用例执行完成后 ，退出进程
    def teardown(self):
        self.drver.quit()


    #成功用例
    def login_sucess(self,):
        pass

