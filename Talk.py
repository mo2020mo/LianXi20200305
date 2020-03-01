#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Talk.py
@Time    :   2020/03/01 13:38:52
@Author  :   MoMse2020
@Version :   1.0
@Contact :   moge2020@outlook.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
import time, random
class Bot():
    wait = 1       #类变量,延时一分钟
    def __init__(self):
        self.q = ''

    def _think(self,s):
        return s 

    def _say(self,s):     #_say函数的功能: 说话(print)时启用一个延时
        time.sleep(Bot.wait)
        print(s)    

    def run(self):
        self._say(self.q)
        self.a = input()
        self._say(self._think(self.a))

class Hello(Bot):
    def __init__(self):
        self.q = "What\'s your name?"
    def _think(self,name):
        return f"Hello, {name}"

class Geatfeeling(Bot):
    def __init__(self):
        self.q = "How are you today?"
    def _think(self,feeling):
        if 'good' in feeling.lower():
            return "I\'m feeling great too..."
        else:
            return "Soory to hear that..."
            
class Favcolor(Bot):
    def __init__(self):
        self.q = "What\' your favouite color?"
    def _think(self, color):
        colors = ['red','orange','blue','yellow','blue','puple','indigo','black','white']
        return f"You favouite color is {color}. My favouite color is {random.choice(colors)}! "


if __name__ == '__main__':
    h = Hello()
    g = Geatfeeling()
    f = Favcolor()
    h.run()
    g.run()
    f.run()
