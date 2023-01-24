#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Date: 2023-01-23 22:08:36
@Author: 今日摸鱼 
@Email: lemonsoldout@163.com
@Github: https://www.github.com/lemonsoldout
@Package: Test\notification.py
@Version: v1.0
@Description: 桌面提醒小工具
'''

# import modules


import time

from plyer import notification

def Timer(seconds):
    if seconds < 0:
        return "Error: Seconds must be positive!"
    
    time.sleep(seconds)
    
    notification.notify(
    title = "桌面提醒",

    message = "{0} 秒倒计时已结束".format(seconds),

    timeout = 5)
    
if __name__ == "__main__":
    
    Timer(2)
   

