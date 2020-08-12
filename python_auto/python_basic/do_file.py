# -*- coding:utf-8 -*-
# @FileName  :do_file.py
# @Time      :2020/5/28 0028 21:54
# @Author    :xiaoming
# -----------------------------------------------------

# mode r  w  a(追加)
#      r+ w+ a+

file = open('test.txt','r+')
res=file.read()
# file.write('666')
print(res)
# 可读可写，先写的话从头开始覆盖写，跟着鼠标移动 ，先读在文末写。 中文注意编码。  w,w+如果文件存在，清空重写，不存在，新建后写
#怎么移动光标？
#读取指定行？，
# a 文件存在就在文末追加，不存在就新建追加，换行加‘\n'
#file.readline() 按行读取    file.readlines() 读取多行  返回的是列表
