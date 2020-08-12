# ###环境地址
from selenium import webdriver
import time,random
import os
import pyautogui
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def url(a):
    if a == "sit":
        url = r"https://admin.zhaolaobao.com"
    elif a == "uat":
        url = "www.abicu"
    return url

class Comm(object):
    instance = None
    init_flag  = False


    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否为空对象，若为空说明第一个对象还没被创建
        if cls.instance is None:
            # 2.对第一个对象没有被创建，我们应该调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 3.把类属性中保存的对象引用返回给python的解释器
        return cls.instance
    # 创建类属性用于__init__方法中的判断
    def __init__(self):
        if Comm.init_flag:
            return
        self.driver = webdriver.Chrome(r"E:\guge\chromedriver.exe")
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(url('sit'))
        time.sleep(3)
        Comm.init_flag = True

    #隐式等待
    def imp(self,a):
        a = self.driver.implicitly_wait(a)
        return a
    # selenium 定位方法
    def locate_element(self, loatetype, value):
        if (loatetype == 'id'):
            self.imp(30)
            el = self.driver.find_element_by_id(value)
        if (loatetype == 'name'):
            el = self.driver.find_element_by_name(value)
        if (loatetype == 'class_name'):
            el = self.driver.find_element_by_class_name(value)
        if (loatetype == 'tag_name'):
            el = self.driver.find_elements_by_tag_name(value)
        if (loatetype == 'link'):
            el = self.driver.find_element_by_link_text(value)
        if (loatetype == 'css'):
            el = self.driver.find_element_by_css_selector(value)
        if (loatetype == 'partial_link'):
            el = self.driver.find_element_by_partial_link_text(value)
        if (loatetype == 'xpath'):
            self.imp(30)
            el = self.driver.find_element_by_xpath(value)
        return el if el else None

    #selenium 输入
    def input_data(self,loatetype,value,data):
        self.locate_element(loatetype,value).send_keys(data)
        time.sleep(2)

    # selenium 点击
    def click(self,loatetype,value):
        self.locate_element(loatetype,value).click()
    # 页面截图
    def sc_shot(self,id):
        for filename in os.listdir(os.path.dirname(os.getcwd())) :
            if filename == 'picture':
                break
        else:
            os.mkdir(os.path.dirname(os.getcwd()) + '/picture/')
        photo = self.driver.get_screenshot_as_file(project_dir +  '/picture/'
                                                   + str(id) + str('_') + time.strftime("%Y-%m-%d-%H-%M-%S") + '.png')
        return photo
    def __del__(self):
        time.sleep(2)
        self.driver.close()
        os.system(r'taskkill /f /im chromedriver.exe')
#鼠标点击
def mouse_click(a):
    time.sleep(0.5)
    if a =='品牌':
        pyautogui.click(408,412)


