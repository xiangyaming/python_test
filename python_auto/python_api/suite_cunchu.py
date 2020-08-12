# -*- coding:utf-8 -*-
# @FileName  :suite_cunchu.py
# @Time      :2020/6/5 0005 01:56
# @Author    :xiaoming
# -----------------------------------------------------

import unittest
from python_api.unit_test import test
import HTMLTestRunner

#suite存储用例，如果在测试用例模块外想要用到测试用例，就要创建实例

suite =unittest.TestSuite()  #存储器，用来存储用例

# #只执行一条用例
# suite.addTest(test('test_add_two_zhengshu'))
#
# runner=unittest.TextTestRunner()
# runner.run(suite)


#方法二，testloader
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(test)) #从测试名里面去找以test_开头的测试用例

#执行
# with open('text.txt','w+',encoding='utf-8')as file : #上下文管理器，冒号后会关闭打开的文件
#     runner=unittest.TextTestRunner(stream=file, descriptions=True, verbosity=2)
#     runner.run(suite)

#生成HTML测试报告、
with open('test_report.html','wb') as file :
    runner=HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2,title='单元测试报告',description='测试报告',tester='xiaoming')
    runner.run(suite)

# #想执行哪条执行哪条
# suite=unittest.TestSuite()  #存储用例
# suite.addTest( )#括号里面是测试类（要不要传参，看父类有没有初始化函数）
# runner=unittest.TextTestResult()
# runner.run(suite)
#
#
# loader=unittest.TestLoader()    #加载用例
# loader.addTest(loader.loadTestsFromName())#()内是测试用例名
# runner=unittest.TextTestResult()
# runner.run(loader)
