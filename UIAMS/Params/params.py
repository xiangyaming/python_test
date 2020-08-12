import os
import yaml
import random
import time
import string
from pywinauto import Desktop   #导入Desktop库，实现对windows系统桌面进行操作
from pywinauto.keyboard import send_keys   #导入send_keys库，实现模拟键盘操作
from Params.index import Comm
###定义随机数，预防重复
global r
r = Comm()
def num():
    a = random.randint(0,10000)+random.randint(0,10000)
    s = a
    return s
###随机生成N位数字，做手机号拼接使用
def rdm(a):
    seeds = string.digits
    random_str = random.sample(seeds, k=a)
    s = ("".join(random_str))
    return s
###等待时间
def T(a):
    time.sleep(a)

###yaml文件
path_dir = str(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
def get_value(key_name):
    """
    获取yaml文件
    :param value:
    :return:
    """
    yamlPath = path_dir + '\\Params\\file.yaml'
    f = open(yamlPath, 'r', encoding='utf-8')
    y = yaml.load_all(f)
    try:
        for data in y:
            if data['name'] == key_name:
                return data
    except Exception:
        raise
#从windows中上传图片
def win_click(a,b):
    app = Desktop()  #创建操作桌面的对象
    time.sleep(0.5)
    dlg = app["打开"]   #获取弹窗的窗口标题
    #dlg.print_ctrl_ids()   打印窗口的所有控件信息
    time.sleep(0.5)
    dlg["地址: xiaominToolbar"].click()   #获取文件路径填写输入框并点击
    time.sleep(0.5)
    send_keys(a)     #在文件路径填写输入框输入文件存在的路径
    send_keys("{VK_RETURN}")  #输入文件路径后按回车键
    time.sleep(0.5)
    dlg["文件名(&N):Edit"].type_keys(b)  #获取文件名输入框并填写文件名
    time.sleep(0.5)
    #send_keys("{VK_RETURN}")
    dlg["打开(&O)"].click()  #获取“打开”控件并点击
    time.sleep(5)
#foucs聚焦到页面某一点位
def focus(a):
    target = r.driver.find_element_by_xpath(a)
    r.driver.execute_script("arguments[0].scrollIntoView();", target)

#根据下拉列表来选择对应的控件
def list(a,b,c):
    r.click('xpath',a)
    time.sleep(0.3)
    department = r.driver.find_elements_by_xpath(b)
    for li in department:
        if c in li.text:
            li.click()
            break