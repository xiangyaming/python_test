# -*- coding:utf-8 -*-
# @FileName  :do_Erro.py
# @Time      :2020/5/28 0028 23:25
# @Author    :xiaoming
# -----------------------------------------------------
try:
    pass
except OSError as e:   #犯的错存在一个变量里
    print('抓捕归案，等待处理')
    print('你犯的错误为{}'.format(e))
    file=open('erro.txt','a+',encoding='utf-8')  #拿个小本本记下犯了什么错
    file.write(str(e))
    file.close()
finally:    #最终都要执行的
    pass

# 标准 Python异常  BaseException 所有错误的基类， Exception 常规错误的基类