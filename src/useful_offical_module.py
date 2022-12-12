"""
介绍几个常用的官方库
"""
import time
# 网络相关操作
import urllib.request

print('时间秒', time.time())
curTime = time.localtime(time.time())
print(curTime, curTime.tm_year)

print(urllib.request.urlopen('https://baidu.com').read(100))
