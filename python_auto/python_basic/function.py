# -*- coding:utf-8 -*-
# @FileName  :function.py
# @Time      :2020/5/28 0028 00:20
# @Author    :xiaoming
# -----------------------------------------------------

#函数，可以重复使用，提高代码的复用性;  函数三部曲
#  1，先用代码实现功能
#  2，变成函数 加def
#  3, 提高代码的复用性
def add_nums(m,n,k=1):  #形参，位置参数（按顺序赋值，有自己的位置），默认参数必须在位置参数后面
    sum =0
    for i in range(m,n,k):
        sum =sum + i
    print('求和的结果是',sum)

add_nums(1,6,2)     #实际参数

#动态参数  不定长参数 *args  贪婪匹配（可以接受任意多个）
#在函数内是作为元组传递的


#关键字参数 **kwargs key-value
#在函数内体现为 字典


#引入模块
#安装  在线安装   1.cmd pip install 模块名 2pip install 国内源地址+模块名  3.file--setting--project interpreter
#导入
    #1.直接导入import   2.from...import...（至少具体到模块名）
if __name__ == '__main__':  #主程序的执行入口
    pass

