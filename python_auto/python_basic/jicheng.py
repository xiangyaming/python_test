# -*- coding:utf-8 -*-
# @FileName  :jicheng.py
# @Time      :2020/6/1 0001 00:52
# @Author    :xiaoming
# -----------------------------------------------------

class RobotOne:
    def __init__(self,year,name):
        self.year=year
        self.name=name
    def walking(self):
        print(self.name+'可以在地面行走')
r1=RobotOne(1990,'小米')
r1.walking()

class RobotTwo(RobotOne):
    def walking(self):  #继承时，函数名相同时叫重写
        print(self.name+'可以在地面上平稳的行走')
    def walking_avoid(self):    #父类没有的叫重写
        print(self.name+'可以避开障碍物')
r2=RobotTwo(1998,'小花')      #传不传参数要看父类里面初始化函数要不要传参
r2.walking()

# class RobotThree(RobotOne,RobotTwo):    #多继承  两个父类之间不要有继承，会报错
#     pass


#超继承   扩展+重写
# class RobotFour(RobotOne):
#     def walkin(self):
#         super()#(子类名，self).add（） 顺着子类名找父类的方法，父类的方法要有，自己还要有新的方法