# -*- coding:utf-8 -*-
# @FileName  :python_OS.py
# @Time      :2020/5/28 0028 22:38
# @Author    :xiaoming
# -----------------------------------------------------

import os
#新建目录
# os.mkdir('mulu')
# os.mkdir('D:/mulu1')

#删除目录
# os.rmdir('mulu')

#获取当前的工作目录
# path =os.getcwd()
# 获取当前文件的绝对路径
# path2=os.path.realpath(__file__)

#如何拼接路径
new_path=os.path.join(os.getcwd(),'mulu2')
os.mkdir(new_path)
print(new_path)

#判断文件是否存在
os.path.exists(__file__)

# 获取当前路径的全部文件和文件夹
print(os.listdir(os.getcwd()))

