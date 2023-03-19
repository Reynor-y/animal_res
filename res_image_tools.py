import numpy as np
from PIL import Image,ImageGrab
import cv2
import sys
import time
import random
import pyautogui

np.set_printoptions(threshold=sys.maxsize)#防止输出结果出现省略号
screen_w=1920
screen_h=1080
game_ratio=1.787
w=445
h=w*game_ratio
box_left=screen_w-w
box_top=screen_h-h-40
box_right=screen_w
box_down=screen_h-40
normal=True
where_to_go={
    "res":(1695,630),
    "garden":(1605,695)
}
def get_mission(k):
    box=(1579,510,1825,749)
    Tem_file=".\image\sign2.png"
    min_val,min_loc=get_image(box,Tem_file)
    if min_val<=0.050 :
        # print('感叹号识别度{}'.format(min_val))
        pyautogui.click(int(1579*k+min_loc[0]+6),int(510+min_loc[1])+60)
        print('识别到点餐任务，点击了坐标(%d,%d)'%(int(1579*k+min_loc[0]+6),int(510+min_loc[1])+60))
        time.sleep(random.uniform(0.5,1.2))
        pyautogui.click(int(1525*k),int(940*k))
        print('跳过对话')
        time.sleep(random.uniform(5,6))
        pyautogui.click(int(1790*k),int(760*k))
        print('接受订单')
        time.sleep(random.uniform(0.5,1.2))
        pyautogui.click(int(1525*k),int(940*k))
        print('跳过对话')
        time.sleep(random.uniform(0.5,1.2))
    pass

def get_parrot(k):
    box=(1799,416,1813,447)
    Tem_file=".\image\sign2.png"
    min_val,min_loc=get_image(box,Tem_file)
    if (min_val<=0.050):
        print('识别到鹦鹉来了，点击了坐标(%d,%d)'%(int(1815*k),int(490*k)))
        print('感叹号坐标位于(%d,%d)'%(min_loc[0]+1474,min_loc[1]+251))
        i=0
        while(i<20):
            pyautogui.click(int(1815*k),int(460*k))
            time.sleep(random.uniform(0.1,0.3))
            i+=1
        print('鹦鹉开始唱歌了')
        time.sleep(2)
    pass
def get_card(k):
    image=np.asarray(ImageGrab.grab(bbox=(int(1620*k),int(517*k),int(1670*k),int(557*k))))#(左，上，右，下)截图并转为opencv可处理的对象
    image=cv2.cvtColor(image,cv2.COLOR_RGB2HSV)#将PIL的RGB格式转换为HSV格式
    hat=cv2.cvtColor(cv2.imread(".\image\magic_hat.png"),cv2.COLOR_BGR2HSV)
    # cv2.imshow('hat',hat)
    res=cv2.matchTemplate(image,hat,cv2.TM_SQDIFF_NORMED)
    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
    print('魔术师的匹配度为{}'.format(min_val))
    if(min_val<0.1):
        print('老鼠魔术师来了')
        pyautogui.click(int(1645*k),int(560*k))#点击老鼠魔术师
        time.sleep(random.uniform(0.5,1))
        pyautogui.click(int(1645*k),int(560*k))#点击跳过对话
        time.sleep(random.uniform(0.5,1))
        pyautogui.click(int(1790*k),int(925*k))#点击"玩吧"
        time.sleep(random.uniform(0.5,1))
        pyautogui.click(int(1575*k),int(535*k))#点击最左侧卡牌
        time.sleep(5)

        image=np.asarray(ImageGrab.grab(bbox=(int(1721*k),int(908*k),int(1862*k),int(943*k))))#(左，上，右，下)截图并转为opencv可处理的对象
        image=cv2.cvtColor(image,cv2.COLOR_RGB2HSV)#将PIL的RGB格式转换为HSV格式
        ok=cv2.cvtColor(cv2.imread(".\image\ok.png"),cv2.COLOR_BGR2HSV)
        # cv2.imshow('hat',hat)
        res=cv2.matchTemplate(image,ok,cv2.TM_SQDIFF_NORMED)
        min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
        print('输赢匹配度为{}'.format(min_val))
        # cv2.imshow('hat',ok)
        # cv2.waitKey()
        # cv2.destroyAllWindows()
        if(min_val<0.7):
            print('输了')
            pyautogui.click(int(1790*k),int(925*k))#通过模板匹配判断是否赢，如果没赢点击“好吧”
            time.sleep(random.uniform(0.5,1))
            pyautogui.click(int(1623*k),int(732*k))#点击“不使用”
            print('等待广告播放')
            time.sleep(40)#等待广告播放
            pyautogui.click(1554,220)#选中窗口，避免sleep过程中中断进程
            pyautogui.click(int(1880*k),int(282*k))#关闭广告
            time.sleep(3)
            pyautogui.click(int(1614*k),int(720*k))#关闭广告
            print('关闭广告')
            pyautogui.click(int(1613*k),int(716*k))#再次点击跳过对话
            time.sleep(1)#等待卡片出现
            pyautogui.click(int(1575*k),int(535*k))#点击最左侧卡牌
            time.sleep(random.uniform(3,4))
            pyautogui.click(int(1575*k),int(535*k))#再次点击跳过对话
        else:
            print('赢了')
            pyautogui.click(int(1575*k),int(535*k))#再次点击跳过对话
        time.sleep(5)
def plant_flower(k):
    lower_color01=np.array([20,15,245])
    higher_color01=np.array([25,20,251])
    lower_color02=np.array([18,204,235])
    higher_color02=np.array([22,208,239])
    lower_color03=np.array([5,175,190])
    higher_color03=np.array([15,185,200])
    lower_color04=np.array([130,105,200])
    higher_color04=np.array([140,115,210])
    #白色[22,18,249] 黄色[20,206,237] 红色[11,179,198] 紫色[134,112,205]
    normal=goto('garden',k)
    if(normal==False):
        return False
    time.sleep(5)
    image=np.asarray(ImageGrab.grab(bbox=(int(1570*k),int(600*k),int(1620*k),int(630*k))))#(左，上，右，下)截图并转为opencv可处理的对象
    image=cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    mask=cv2.inRange(image,lower_color01,higher_color01)
    if([255] in mask):
        pyautogui.click(int(1645*k),int(609*k))
        print('检测到花圃1已经成熟，点击收获')
        time.sleep(random.uniform(1,2))
        pyautogui.click(int(1645*k),int(609*k))#点击花圃
        time.sleep(random.uniform(2,2.5))
        pyautogui.click(int(1700*k),int(745*k))#点击按钮
        print('花圃1已经重新播种')
    else:
        print('花圃1还没有成熟')
    time.sleep(2)
    #采摘花圃1
    image=np.asarray(ImageGrab.grab(bbox=(int(1750*k),int(600*k),int(1795*k),int(630*k))))#(左，上，右，下)截图并转为opencv可处理的对象
    image=cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    mask=cv2.inRange(image,lower_color02,higher_color02)
    if([255] in mask):
        time.sleep(random.uniform(0.5,1))
        pyautogui.click(int(1775*k),int(610*k))
        print('检测到花圃2已经成熟，点击收获')
        time.sleep(random.uniform(1,2))
        pyautogui.click(int(1775*k),int(610*k))#点击花圃
        time.sleep(random.uniform(2,2.5))
        pyautogui.click(int(1700*k),int(745*k))#点击按钮
        print('花圃2已经重新播种')
        
    else:
        print('花圃2还没有成熟')
    time.sleep(2)
    #采摘花圃2
    image=np.asarray(ImageGrab.grab(bbox=(int(1570*k),int(715*k),int(1620*k),int(740*k))))#(左，上，右，下)截图并转为opencv可处理的对象
    image=cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    mask=cv2.inRange(image,lower_color03,higher_color03)
    if([255] in mask):
        time.sleep(random.uniform(0.5,1))
        pyautogui.click(int(1600*k),int(725*k))
        print('检测到花圃3已经成熟，点击收获')
        time.sleep(random.uniform(1,2))
        pyautogui.click(int(1600*k),int(725*k))#点击花圃
        time.sleep(random.uniform(2,2.5))
        pyautogui.click(int(1700*k),int(745*k))#点击按钮
        print('花圃3已经重新播种')
    else:
        print('花圃3还没有成熟')
    time.sleep(2)
    #采摘花圃3
    image=np.asarray(ImageGrab.grab(bbox=(int(1750*k),int(715*k),int(1795*k),int(740*k))))#(左，上，右，下)截图并转为opencv可处理的对象
    image=cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    mask=cv2.inRange(image,lower_color04,higher_color04)
    if([255] in mask):
        time.sleep(random.uniform(0.5,1))
        pyautogui.click(int(1775*k),int(725*k))
        print('检测到花圃4已经成熟，点击收获')
        time.sleep(random.uniform(1,2))
        pyautogui.click(int(1775*k),int(725*k))#点击花圃
        time.sleep(random.uniform(2,2.5))
        pyautogui.click(int(1700*k),int(745*k))#点击按钮
        print('花圃4已经重新播种')
    else:
        print('花圃4还没有成熟')
    time.sleep(2)
    #采摘花圃4
    normal=goto('res',k)
    if(normal==False):
        return False
    else:
        return True
    
def rest(k):
    box=(1656,739,1738,765)
    Tem_file=".\image\\rest_ok.png"
    min_val,min_loc=get_image(box,Tem_file)

    if(min_val<0.056):
        # pyautogui.click()
        pyautogui.click(int(1695*k),int(750*k))
        print("检测到休息提示，帮你取消了窗口")
    else:
        print("还不该休息")
    pass


def get_image(box,Tem_file):
    
    image=np.asarray(ImageGrab.grab(bbox=box))
    #(左，上，右，下)截图并转为opencv可处理的对象
    # image=np.asarray(ImageGrab.grab(bbox=(box_left,box_top,box_right,box_down)))
    image=cv2.cvtColor(image,cv2.COLOR_RGB2HSV)#将PIL的RGB格式转换为GRAY格式
    # sign=cv2.cvtColor(cv2.imread(".\image\sign2.png"),cv2.COLOR_BGR2HSV)
    sign=cv2.cvtColor(cv2.imread(Tem_file),cv2.COLOR_BGR2HSV)
    # cv2.imshow('image',image)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    res=cv2.matchTemplate(image,sign,cv2.TM_SQDIFF_NORMED)
    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
    print('识别度{}'.format(min_val))
    print('坐标位于(%d,%d)'%(min_loc[0]+1579,min_loc[1]+510))
    # top_left=min_loc
    # w=80
    # h=24
    # bottom_right=(top_left[0]+w,top_left[1]+h)
    # cv2.rectangle(image,top_left,bottom_right,255,2)
    # # cv2.imshow('sign',sign)
    # cv2.imshow('test',image)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    return min_val,min_loc
def goto(where,k):
    box=(1773,741,1837,773)
    Tem_file='.\image\map.png'
    pyautogui.click(int(1825*k),int(360*k))#点击地图
    time.sleep(3)
    pyautogui.click(int(where_to_go[where][0]*k),int(where_to_go[where][1]*k))#点击目的地
    print('前往{}'.format(where))
    time.sleep(2)
    min_val,min_loc=get_image(box,Tem_file)
    if (min_val<=0.045):
        print('传送失败，检测到程序错误，回到餐厅')
        pyautogui.click(1695,630)
        if(where=='res'):
            print('已经在餐厅了，可以开始了')
            pyautogui.click(1490,260)
            return True
        return False
    time.sleep(2)
    return True
# cv2.bitwise_and(image,)
# image=np.asarray(ImageGrab.grab(bbox=(1100,360,1290,460)))#(左，上，右，下)截图并转为opencv可处理的对象
# image=cv2.cvtColor(image,cv2.COLOR_RGB2HSV)#将PIL的RGB格式转换为GRAY格式
# sign=cv2.cvtColor(cv2.imread("./image/mission_sign.png"),cv2.COLOR_BGR2HSV)


# (1695,750)连续在线按钮坐标
    # top_left=min_loc
    # bottom_right=(top_left[0]+w,top_left[1]+h)
    # cv2.rectangle(image,top_left,bottom_right,255,2)
    # # cv2.imshow('sign',sign)
    # cv2.imshow('test',image)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
# pyautogui.click(885,565)#点击取消分享

