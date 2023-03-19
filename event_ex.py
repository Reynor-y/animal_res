from queue import Queue,Empty
from threading import Thread,Timer
import sys
import win32gui

class EventManager:
    def __init__(self):
        self.eventQuene=Queue()
        self.active=False
        self.thread=Thread(target=self.Run)
        self.count=0
        self.handlers={}
    def Run(self):
        # 引擎运行
        print('{}run'.format(self.count))
        while self.active:
            try:
                print('\n   <RUN:>开始get:',self.eventQuene)
                event=self.eventQuene.get(block=True,timeout=1)
                print('<RUN:>取到事件了:',event)
                self.EventProcess(event)
            except Empty:
                print('<RUN:>队列是空的')
                pass
            self.count+=1
            print('<RUN:>Run中的count：',self.count)
    def EventProcess(self,event):
        #处理事件
        print('{}EventProcess'.format(self.count))
        if event.type in self.handlers:
            for handler in self.handlers[event.type]:
                handler(event)
        self.count+=1
    def Start(self):
        print('{}start'.format(self.count))
        self.active=True
        self.thread.start()
        self.count+=1
        print('start中的count:',self.count)
    def Stop(self):
        print('{}Stop'.format(self.count))
        self.active=False
        self.thread.join()
        self.count+=1
    def AddEventListener(self,type,handler):
        print('{}AddEventListener'.format(self.count))
        try:
            handlerList=self.handlers[type]
        except KeyError:
            handlerList=[]
            self.handlers[type]=handlerList
        if handler not in handlerList:
            handlerList.append(handler)
        print(self.handlers)
        self.count+=1
    def RemoveEventListener(self,type,handler):
        print('{}RemoveEventListner'.format(self.count))
        try:
            handlerList=self.handlers[type]
            if handler in handlerList:
                handlerList.remove(handler)
            if not handlerList:
                del self.handlers[type]
        except KeyError:
            pass
        self.count+=1
    def SendEvent(self,event):
        '发送事件，向事件队列中存入事件'
        print('{}SendEvent'.format(self.count))
        self.count+=1
class Event:
    # '事件对象'
    def __init__(self,type=None):
        print('实例化事件对象：事件类型：{},事件：self.dict'.format(type))
        #事件类型
        self.type=type
        self.dict={}
EVENT_ARTICLE="Event_Article"

class PublicAccounts:
    # 事件源
    def __init__(self,eventManager):
        print('实例化')
        self.eventManager=eventManager
    def WriteAndSendNewArtical(self):
        # 事件发生
        event=Event(type=EVENT_ARTICLE)
        event.dict['article']='文章名。。。'
        #发送事件
        print(u'事件发生')
        self.eventManager.SendEvent(event)
class Listener:
    #监听器
    def __init__(self,username):
        self.username=username

    #监听器的处理函数
    def ReadArtical(self,event):
        print(u'%s收到新文章'%self.username)
        print(u'正在阅读内容%s'%event.dict['artcle'])
def test():
    # 测试函数
    # 1.实例化监听器
    listener1=Listener('小明')#订阅者1
    listener2=Listener('小红')#订阅者2
    # 2.实例化事件管理器
    eventManager=EventManager()
    # 3.绑定事件和监听器响应函数
    eventManager.AddEventListener(EVENT_ARTICLE,listener1.ReadArtical)
    eventManager.AddEventListener(EVENT_ARTICLE,listener2.ReadArtical)
    # 4.启动事件管理器
        # 注意：4.1这里会启动一个新的事件处理线程，一直监听下去，可以看run（）中的while
        #      4.2 同时主线程会继续执行下去
    eventManager.Start()
    # 5.实例化事件源
    publicAcc=PublicAccounts(eventManager)
    # 6.定时启动事件源中的生成事件对象以及发送事件
    timer=Timer(5,publicAcc.WriteAndSendNewArtical)
    timer.start()

if __name__=='__main__':
    test()
# def onMouseEvent(event):
#     if(event.MessageName=="mouse right down"):
        
#         sys.exit()

#     return True
# hwnd = win32gui.GetForegroundWindow()

# def onKeyboardEvent(event):
#     print(event.Key)
#     # if(event.Key=='F5'):
#     #     sys.exit()
#     return True
# def main():
#     hm=pyWinhook.HookManager()
#     hm.KeyDown = onKeyboardEvent
#     hm.HookKeyboard()
#     # hm.MouseAll = onMouseEvent   
#     # hm.HookMouse()
#     # pythoncom.PumpMessages()
# main()