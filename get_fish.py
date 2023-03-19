# import pyWinhook
import pyautogui
import time
import random
import res_image_tools
# from win32 import win32gui
# import cv2
# import datetime
# import sys
# import event
import Listener
from ctypes import *


# windll.user32.BlockInput(1)
thread1 = Listener.myThread(1, "Listener")
thread1.start()
k=1
starttime=time.perf_counter()
# pg = pyautogui.PyMouse()
ads_pos=(1870,970)
pyautogui.moveTo(ads_pos[0],ads_pos[1])
i=0
n=0
acc=0
clock=0
while(n<=100):
    pyautogui.click(1554,220)#选中窗口，避免sleep过程中中断进程
    time.sleep(3)
    res_image_tools.rest(k)
    is_res=res_image_tools.goto('res',k)
    if(is_res==False):
        pyautogui.click(1490,260)
        print('确定在餐厅，可以开始了')
    else:
        print('回到餐厅，可以开始了')
    endtime=time.perf_counter()
    if ((endtime-starttime)//900)>clock:
        print("已经运行%d小时了，前往花园采摘"%((endtime-starttime)//3600))
        normal=res_image_tools.plant_flower(k)
        if(normal==False):
            continue
        clock+=1
    
    res_image_tools.get_card(k)
    res_image_tools.get_parrot(k)
    res_image_tools.get_mission(k)
    pyautogui.moveTo(ads_pos[0],ads_pos[1])
    print("开始第{}次循环".format(n+1))
    while(i<=199):
        pyautogui.click(ads_pos[0],ads_pos[1])#点击手机宣传
        i+=1
        time.sleep(random.uniform(0.1,0.3))
    # m.click(int(1645*k),int(675*k))#点菜4


    
    # time.sleep(random.uniform(0.1,0.3))
    # m.click(int(1735*k),int(675*k))#点菜5
    # time.sleep(random.uniform(0.1,0.3))
    # m.click(int(1845*k),int(675*k))#点菜6
    n+=1
    i=0
    print("已经进行了{}次循环，等待中".format(n))
    time.sleep(random.uniform(2,5))
    
print('运行结束')
 
