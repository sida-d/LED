# test code to integrate ledArray library with rpi_ws281x
# By Brygg Ullmer, Sida Dai, and Mitali Bhosekar, Clemson University
# Begun 2022-05-05

from ledArray    import *
from ledArrayViz import *
import time
import math
import os
from rpi_ws281x import *

# data: the data read from LiDAR. Its index number is the 
# angle, value is the distance from LiDAR
# LiDARx, LiDARy: the coordinate of LiDAR on the floor 
# coordinate system
def calCoordinate(data,LiDARx,LiDARy):
    result = []
    for i in range(len(data)):
        x = data[i]*math.sin((i/360)*math.pi)
        y = data[i]*math.cos((i/360)*math.pi)
        coor = (LiDARx-x,(33*FLOOR_Y)-(LiDARy-y))
        result.append(coor)

    return result

def calPosition(ledArr,x,y):
    arrCol = int(x // 43)
    arrRow = int(y // 33)
    
    if 0 <= arrCol < ledArr.shape[1] and 0 <= arrRow < ledArr.shape[0]:
        ledArr.fillPixel(arrRow,arrCol,'O')
    return None

def ledRun(ledstri,ledarr):
    for i in range(len(ledarr)):
        ledstri.setPixelColor(i,Color(ledarr[i][0],ledarr[i][0],ledarr[i][0]))
    ledstri.show()
    return

#floor configuration
FLOOR_X = 60
FLOOR_Y = 75

print("main called")

na = np2DCharArr((FLOOR_Y,FLOOR_X))

na.print()

global lav
lav = ledArrayViz(na)


################################################
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
    xyco = calCoordinate(i,1219,1000)
    XYdata.append(xyco)

'''
#############################################

# LED strip configuration:
LED_COUNT      = FLOOR_X * FLOOR_Y      # Number of LED pixels.
LED_PIN        = 12      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 150     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

na.print()
weaveCh = na.genColWeave()
weaveCo = na.mapColorStr2Int(weaveCh)

print("\n" + weaveCh)
print("\n" + str(weaveCo))

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ,LED_DMA,LED_INVERT,LED_BRIGHTNESS,LED_CHANNEL)
strip.begin()

j = 0

while True:
    na.refresh('.')
    
    #print("fill row")
    #na.fillRow(1, 'O')
    
    for i in XYdata[j]:
            calPosition(na,i[0],i[1])
    
    na.print()
    weaveCh = na.genColWeave()
    weaveCo = na.mapColorStr2Int(weaveCh)
    
    j += 1
    if j == 999:
        j = 0
    
    time.sleep(0.2)
    
    ledRun(strip,weaveCo)

#############################################
'''

global j
j = 0
#pgz will run this function every frame
def update():
    global j
    
    na.refresh('.')
    #print("fill row")
    na.fillRow(1, 'O')
    na.fillCol(1, 'O')
    
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
