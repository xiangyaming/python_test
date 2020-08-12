# -*- coding:utf-8 -*-
# @FileName  :class_object.py
# @Time      :2020/5/31 0031 23:37
# @Author    :xiaoming
# -----------------------------------------------------

#class 类名： 首字母大写、驼峰命名
#类属性
#类方法

class GirlFriend:
    #类属性
    height=160
    weight=100

    #实例方法
    def cooking(self):
        print('女朋友要会做饭')

    def swimming(self):
        print('女朋友要会游泳')

#创建实例  类名（）：  上面的self就是实例本身（类里面定义函数会自动传一个实例）
gf=GirlFriend()  #创建实例只能在类的外面创建（与类名统计）
#调用属性   实例.属性名
#调用函数   实例.方法名

#类方法 @classmethod
#静态方法 @staticmethod     这两个方法不需要用到类里面的属性的时候就可以声明，可以直接类名.方法名，可以不创建实例


#初始化函数  def __init__(self,参数):
                #self.参数=参数   把外面传的参数赋值给实例的参数
#多个函数用到这个参数的时候，就可以用初始化函数        初始化函数没有返回值