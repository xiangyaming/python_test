# -*- coding:utf-8 -*-
# @FileName  :home_work.py
# @Time      :2020/5/29 0029 00:40
# @Author    :xiaoming
# -----------------------------------------------------
#练习题： 输出一个*组成的直角三角形
#方法一
for i in range(6):
    print("*"*i)

#方法二：嵌套循环
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print('')  #print语句会换行，在控制行数的时候换行

#题目2：每个边都是5颗星的等边三角形
for i in range(1,6): #控制行数
    for j in range(1,6-i): #输出前面的空格
        print(' ',end='')
    for k in range(1,i+1): #输出后面的*空格
        print('* ',end='')
    print('')

#3，九九乘法表
for i in range(10):
    for j in range(1,i+1):
        print('{}*{}={} '.format(j,i,i*j),end='')
    print('')

#4，冒泡排序 利用for循环完成a=[1,7,4,89,34,2]到大的排序
# 冒泡：相邻两个元素进行比较，
a=[1,7,4,89,34,2]
#for i in range(1,len(a)-1):
for j in range(1,len(a)-1):
    if a[j]>a[j+1]:
        a[j],a[j+1]=a[j+1],a[j]
print(a)

# 5,自动贩卖机，只接受1,5,10元的硬币或者纸币，饮料：橙汁，椰汁，矿泉水，早餐奶，价格分别为：3.5,4,2,4.5，投钱后吐出饮料和找零
drinks={'1':3.5,'2':4,'3':2,'4':4.5}
total=0
while True:
    choose=input('请选择要买的饮料：1橙汁，2椰汁，3矿泉水，4早餐奶,q退出')
    if choose in drinks.keys():
        total=drinks[choose]
    elif choose=='q':
        print('退出选择饮料')
        break
    else:
        print('不存在该选项，请重新选择！')

#6.写一个软件测试工程师类：有类属性和类方法，完成调用