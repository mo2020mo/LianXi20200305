from Talk import *

class TalkBot():
    def __init__(self):
        self.bots = []
    def _add(self,bot):
        self.bots.append(bot)
    def run(self):
        print("Welcome to Talk-diglog system. Let\'s Talk...\n")
        for bot in self.bots:
            bot.run()

if __name__ == '__main__':
    #创建对象
    talkbot = TalkBot()
    #添加实例 
    talkbot._add(Hello())
    talkbot._add(Geatfeeling())
    talkbot._add(Favcolor())
    talkbot._add(clacl("looped"))
    #运行
    talkbot.run()