# Library support for 2D LED strip arrays
# By Brygg Ullmer, Sida Dai, and Mitali Bhosekar, Clemson University
# Begun 2022-04-13

from ledArray    import *
from ledArrayViz import *
import time
import math


############## calCoordinate ##############

# data: the data read from LiDAR. Its index number is the 
# angle, value is the distance from LiDAR
# LiDARx, LiDARy: the coordinate of LiDAR on the floor 
# coordinate system
def calCoordinate(data,LiDARx,LiDARy):
    result = []
    for i in range(len(data)):
        x = data[i]*math.sin((i/360)*math.pi)
        y = data[i]*math.cos((i/360)*math.pi)
        coor = (LiDARx-x,LiDARy-y)
        result.append(coor)

    return result

def calPosition(ledArr,x,y):
    arrCol = int(x // 200)
    arrRow = int(y // 200)
    
    if 0 <= arrCol < ledArr.shape[1] and 0 <= arrRow < ledArr.shape[0]:
        ledArr.fillPixel(arrRow,arrCol,'O')
    return None

print("main called")

na = np2DCharArr((20,40))

na.print()

global lav
lav = ledArrayViz(na)

#open the log file and change it into a float list
f = open("data-2022-04-10-1730.txt")

ldata = []
for i in range(1000):
    line = f.readline()
    nline = line[1:(len(line)-2)]
    lsplit = nline.split(", ")
    data = list(map(float,lsplit))
    ldata.append(data)
    
f.close()

#change the LiDAR data into XY coordinate data
XYdata = []
for i in ldata:
    xyco = calCoordinate(i,4000,4000)
    XYdata.append(xyco)


global j
j = 0
#pgz will run this function every frame
def update():
    global j
    
    na.refresh('.')
    for i in XYdata[j]:
            calPosition(na,i[0],i[1])
    
    j += 1
    if j == 999:
        j = 0
    
    time.sleep(0.2)

#print(XYdata)


def draw(): 
   global screen, lav
   try: lav.draw(screen)
   except: pass