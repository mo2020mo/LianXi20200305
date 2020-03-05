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
from simpleeval import simple_eval  #计算函数
from termcolor import colored       #引用termcolor.colored函数改变文字在控制台的颜色
import colorama                     #引用colorama函数
colorama.init()                     #要使termcolor中使用的ANSI颜色与windows终端一起使用,不处理控制台输出可能会乱码
class Bot():
    wait = 1                        #类变量,延时一分钟
    def __init__(self,runtype = "once"):
        self.q = ''
        self.runtype = runtype

    def _think(self,s):
        return s

    def _say(self,s):              #_say函数的功能: 说话(print)时启用一个延时
        time.sleep(Bot.wait)
        print(colored(s,'blue'))   #colored改变文字颜色 

    def _run_once(self):           #开关1
        self._say(self.q)
        self.a = input()
        self._say(self._think(self.a))

    def _run_looped(self):         #开关2                 
        self._say(self.q)
        while True:
            self.a = input()
            if self.a.lower() in ["exit","queit","x","q"]:
                break
            self._say(self._think(self.a))

    def run(self):                 #相当于一个控制开关!
        if self.runtype == "once":
            self._run_once()
        elif self.runtype == "looped":
            self._run_looped()
    
class Hello(Bot):
    def __init__(self,runtype = "once"):
        super().__init__(runtype)
        self.q = "What\'s your name?"
    def _think(self,name):
        return f"Hello, {name}"

class Geatfeeling(Bot):
    def __init__(self,runtype = "once"):
        super().__init__(runtype)
        self.q = "How are you today?"
    def _think(self,feeling):
        if 'good' in feeling.lower():
            return "I\'m feeling great too..."
        else:
            return "Soory to hear that..."
            
class Favcolor(Bot):
    def __init__(self,runtype = "once"):
        super().__init__(runtype)
        self.q = "What\' your favouite color?"
    def _think(self, color):
        colors = ['red','orange','blue','yellow','blue','puple','indigo','black','white']
        return f"You favouite color is {color}. My favouite color is {random.choice(colors)}! "

class clacl(Bot):
    def __init__(self,runtype = "once"):
        super().__init__(runtype)
        if self.runtype == "looped":    #判断开关输出不同的提示问题
            self.q = colored('The system has upgraded the computing function. Let\'s try some questions! Input ["exit","queit","x","q"] exit!','red')
        elif self.runtype == "once":
            self.q = colored('The system has upgraded the computing function. Let\'s try some questions!','green')
    def _think(self, s):
        try:
            result = simple_eval(s)
            return f"Done. Rseult = {result}"
        except:
            return "Input Error! restart..."

if __name__ == '__main__':
    h = Hello()
    g = Geatfeeling()
    f = Favcolor()
    c = clacl("looped")
    h.run()
    g.run()
    f.run()
    c.run()