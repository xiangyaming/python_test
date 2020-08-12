# -*- coding:utf-8 -*-
# @FileName  :unit_test.py
# @Time      :2020/6/3 0003 00:56
# @Author    :xiaoming
# -----------------------------------------------------

#写用例     TestCase
#执行用例   AestSuite 存储用例  TestLoader 加载用例
#对比结果   Assert
#测试报告   TextTestRunner  都是类

import unittest

from python_api.beiceihanshu import MathMethod
class test(unittest.TestCase):  #继承unitest的testcase,专门来写用例
    #一个用例就是一个函数，不能传参，只有self关键字
    #所有的用例都是test_开头
    def test_add_two_zhengshu (self):
        res=MathMethod(2,3).add()
        print('2+3的结果是：',res)
        try:
            self.assertEqual(5,res,'两个数相加出错了')     #断言，（来自父类），（期望值，实际值），期望值和实际值作比较
        except AssertionError as e:
            print('出错啦，断言错误{}'.format(e))
            raise e #异常处理后，要抛出异常
    def test_jianfa_zhengshu(self):
        res=MathMethod(8,5).jianfa()
        print('8-5的结果是：',res)
        try:
            self.assertEqual(4,res,'两个数相减出错了')
        except AssertionError as e:
            print('出错啦，断言错误{}'.format(e))
            raise e  # 异常处理后，要抛出异


# if __name__ == '__main__':
#     unittest.main() #所有用例全部执行

#   如果后面的用例对前面的用例有依赖，怎么去处理，三种方法
#   setUp(),每条用例执行前，先执行setUp()。 tearDown(),每条用例执行完会执行tearDown()。 是unitest框架里面的函数，继承过来自己重写

#全局变量   在函数里面声明变量为全局变量，global

#反射 getattr hasattr setattr delattr        setattr(类名，‘属性名’，‘值’)可以对类里面的属性进行修改
