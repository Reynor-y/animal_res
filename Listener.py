import threading
import time
import win32gui
import sys
import pyWinhook
import os

class myThread(threading.Thread):
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
    
    def run(self):  
        time.sleep(5)
        while(True):                 #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
            # print ("Start")
            
            time.sleep(0.3)
            getWindow()
            # loop()

# def onMouseEvent(event):
#     return False
def getWindow():
    hwnd = win32gui.GetForegroundWindow()
    # print(hwnd)
    hwnd_name=win32gui.GetWindowText(hwnd)
    # print(hwnd_name)
    if(hwnd_name!='动物餐厅'):
    #     # print(1)
        os._exit(1)
    #     # pass
# def MouseSwitch():
#     pass

thread1 =myThread(1, "Listener")
thread1.start()
# getWindow()