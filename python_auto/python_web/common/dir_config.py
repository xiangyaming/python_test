# -*- coding:utf-8 -*-
# @FileName  :dir_config.py
# @Time      :2020/7/23 0023 01:40
# @Author    :xiaoming
# -----------------------------------------------------

import  os

'''
1、os.path.abspath(__file__)  返回当前脚本的绝对路径

2、os.path.split(path)  将path分割成目录和文件名二元组返回

3、os.path.dirname(path)  返回path的目录，等同于os.path.split(path)[0]

4、os.path.basename(path) 返回path的文件名，等同于os.path.split(path)[1]

'''

#框架项目顶层项目
base_dir = os.path.split(os.path.abspath(__file__))[0][0]

testdatas_dir = os.path.join(base_dir,"testdatas")

testcases_dir = os.path.join(base_dir,"testcases")

htmlreport_dir = os.path.join(base_dir,"report")

log_dir = os.path.join(base_dir,"logs")

# config_dir = os.path.join(base_dir,"config")

screenshot_dir = os.path.join(base_dir,"screenshot")