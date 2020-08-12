# -*- coding:utf-8 -*-
# @FileName  :request_response.py
# @Time      :2020/6/2 0002 23:51
# @Author    :xiaoming
# -----------------------------------------------------

import requests

#全国天气预报
#get请求
# url = ' http://v.juhe.cn/weather/index?format=2&cityname=武汉&key=0d5f216347b581a39f526d01d2b692ad'
# res=requests.get(url)
# print('响应头是',res.headers)
# print('响应状态码为',res.status_code)
# print('响应正文为',res.json())


#post 请求
# url = ' http://v.juhe.cn/weather/index?format=2'
# date={'cityname':'武汉','key':'0d5f216347b581a39f526d01d2b692ad'}
# res=requests.get(url,date)
# # res=requests.post(url,date)
# print('响应头是',res.headers)
# print('响应状态码为',res.status_code)
# print('响应正文为',res.text)
# print('请求头为',res.request.headers)

#新闻查询
url='https://api.apiopen.top/getWangYiNews'
date={'page':'1','count':'4'}
header={'User-Agent':'Mozilla/5.0'}  #伪装浏览器为啥会失败？？？
res=requests.post(url,date,header)
print(res.json())
print(res.request.headers)

#消息实体：响应头、响应状态码、响应报文
#请求头包含：
