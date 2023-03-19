import numpy as np
from PIL import Image,ImageGrab
import cv2
import sys
# np.set_printoptions(threshold=sys.maxsize)#防止输出结果出现省略号

image=np.asarray(ImageGrab.grab(bbox=(1042,152,1366,727)))#(左，上，右，下)截图并转为opencv可处理的对象
# image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)#将PIL的RGB格式转换为BGR格式
image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)#将PIL的RGB格式转换为GRAY格式
# image=cv2.imread("./image/mission.png",0)
sign=cv2.imread("./image/mission_sign.png",0)
print(sign.shape[::-1])
w,h=sign.shape[::-1]
print(w,h)
res=cv2.matchTemplate(image,sign,cv2.TM_SQDIFF)
min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
print(min_val,max_loc)
top_left=min_loc
bottom_right=(top_left[0]+w,top_left[1]+h)
cv2.rectangle(image,top_left,bottom_right,255,2)
# cv2.imshow('sign',sign)
cv2.imshow('test',image)
cv2.waitKey()
cv2.destroyAllWindows()







# print(image[1,1])
# rgb=np.array([40,106,217])
# hsv=(621,8157,8510)
# print(np.column_stack(np.where(image==hsv)))
# print(image[95,181])
# grb=[24,139,204]
# print(np.column_stack(np.where(image==hsv)))
# image[25,1]=[1,1,1]
# color=np.column_stack(np.where(image==grb))
# new_color=np.delete(color,[2],axis=1)
# print(color)
# for item in color:
#     image[item]==[0,0,0]
#     print(image[item])
# print(image[24,1])
# print(color[1][0])
