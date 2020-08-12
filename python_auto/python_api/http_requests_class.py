# -*- coding:utf-8 -*-
# @FileName  :http_requests_class.py
# @Time      :2020/6/3 0003 00:30
# @Author    :xiaoming
# -----------------------------------------------------
import requests

class HttpRequest:
    '''利用HttpRequest封装get和post请求 '''
    def http_request(self,url,key,method):
        if method=='get':
            res = requests.get(url, key )
        else:
            res = requests.post(url, key)  #返回结果的消息实体
        # print('响应正文为',res.json())
        return res #返回消息实体

if __name__ == '__main__':
    url = ' http://v.juhe.cn/weather/index?format=2'
    key={'cityname':'武汉','key':'0d5f216347b581a39f526d01d2b692ad'}
    res = HttpRequest().http_request(url,key,'get') # 返回结果的消息实体  创建实例
    print('响应的结果是',res.json())

 
