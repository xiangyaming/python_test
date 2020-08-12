# -*- coding:utf-8 -*-
# @FileName  :basepage.py
# @Time      :2020/7/20 0020 22:43
# @Author    :xiaoming
# -----------------------------------------------------

import datetime
import time
from  selenium import  webdriver
from selenium.webdriver.common.by import By  #导入by方法
from selenium.webdriver.support.wait import WebDriverWait #隐式等待
from selenium.webdriver.support import expected_conditions as  EC
import logging #导入日志模块
from python_web.common import dir_config


# 封装基本函数--执行日志、异常处理、失败截图
# 封装页面所有的公共部分，（非业务层面）

class BasePage:
    def __init__(self,driver):
        self.driver=driver

    #等待元素可见
    def wait_eleVisible(self,locator,timeout=30,poll_frequency=0.5,doc=""):
        """

        :param locator: 元素定位，元组的形式
        :param timeout: 等待时长
        :param poll_frequency: 轮询周期
        :param doc: 截图时传入参数说明,如"登录模块_登录页面"
        :return:
        """
        logging.info("等待元素: {0} 可见".format(locator))
        try:
            start = datetime.datetime.now() #开始等待时间
            WebDriverWait(self.driver,timeout,poll_frequency)\
            .until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now() #结束等待时间
            waittime = end - start
            logging.info("等待结束，等待时长为 {} ".format(waittime))
        except:
            logging.exception("等待元素可见失败！！！")
            #截图
            self.save_screenshot(doc)
            raise


    #等待元素存在
    def wait_ele_presence(self,locator,timeout=30, poll_frequency=0.5,doc=""):
        logging.info("等待元素: {0} 存在".format(locator))
        try:
            start = datetime.datetime.now()  # 开始等待时间
            WebDriverWait(self.driver, timeout, poll_frequency) \
                .until(EC.presence_of_element_located(locator))
            end = datetime.datetime.now()  # 结束等待时间
            waittime = (end-start).seconds
            logging.info("等待结束，等待时长为 {} ".format(waittime))
        except:
            logging.exception("等待元素存在失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    #查找元素
    def get_element(self,locator,doc=""):
        logging.info("查找元素: {0}".format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    #点击操作
    def click_element(self,locator,doc=""):
        #查找元素
        ele = self.get_element(locator,doc)
        #元素操作
        logging.info("点击元素：{0}".format(locator))
        try:
            ele.click()
        except:
            logging.exception("点击元素失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise
    #输入操作
    def input_text(self,locator,text,doc=""):
        # 查找元素
        ele = self.get_element(locator, doc)
        # 元素操作
        logging.info("元素输入内容：{0}".format(locator))
        try:
            ele.send_keys(text)
        except:
            logging.exception("元素输入内容失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    #获取元素的文本类容
    def get_ele_text(self,locator,doc=""):
        # 查找元素
        ele = self.get_element(locator, doc)
        # 元素操作
        logging.info("获取元素：{0} 的文本内容".format(locator))
        try:
           return ele.text
        except:
            logging.exception("获取元素文本内容失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise
    #获取元素属性
    def get_ele_attribute(self,locator,attribute,doc=""):
        # 查找元素
        ele = self.get_element(locator, doc)
        # 元素操作
        logging.info("获取元素：{0} 的属性".format(locator))
        try:
            return ele.get_attribute(attribute)
        except:
            logging.exception("获取属性失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise
    #alter处理
    def alert_action(self):
        self.driver.switch_to.alert()
        pass
    #iframe切换
    def switch_iframe(self,locator,doc):
        #找到要切换的iframe元素
        ele = self.get_element(locator)
        logging.info("切换到iframe")
        try:
            self.driver.switch_to.iframe(ele)
        except:
            logging.exception("切换iframe失败")
            self.save_screenshot(doc)
        raise

    #窗口切换
    def switch_window(self,doc):
        #获取所有窗口的句柄
        handles = self.driver.window_handles
        logging.info("切换到最后一个窗口")
        try:
            self.driver.switch_to_window(handles[-1])
        except:
            logging.exception("切换窗口失败")
            self.save_screenshot(doc)
        raise
    #上传操作
    #滚动条处理
    #错误截图
    def save_screenshot(self,doc):
        # 图片名称：模块名_页面名称_操作名称_年-月-日_时分秒.png
        #时间等于当前时间，格式年-月-日_时分秒

        file_path = dir_config.screenshot_dir + \
                    "/{0}_{1}.png ".format(doc,time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime()))
        try:
            self.save_screenshot(file_path)
            logging.info("截取网页成功。截图的路径为：{0}".format(file_path))
        except:
            logging.exception("截图失败！！！")