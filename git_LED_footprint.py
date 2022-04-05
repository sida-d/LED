from rpi_ws281x import *
import time

# LED strip configuration:
LED_COUNT      = 500      # Number of LED pixels.
LED_PIN        = 10      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 150     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ,LED_DMA,LED_INVERT,LED_BRIGHTNESS,LED_CHANNEL)
strip.begin()

'''
for x in range(0,LED_COUNT//10):
        strip.setPixelColor(x*10,Color(255,0,0))
        strip.show()
        #time.sleep(0.01)
        strip.setPixelColor(x*10,Color(0,0,0))
        strip.show()
        #time.sleep(0.01)
'''

def position(x,y,LED):
    if x % 2 == 0:
        ind = sum(LED[:(x)]) + LED[x]-y
        return ind
    else:
        ind = sum(LED[:(x)]) + y - 1
        return ind

def light(LEDlist):
    for x in LEDlist:
        strip.setPixelColor(x,Color(255,0,0))
        strip.show()
        #time.sleep(0.01)
        #strip.setPixelColor(x*10,Color(0,0,0))
        #strip.show()
        #time.sleep(0.01)

def footprint(x,y,LED):
    foot = [[x,y]]
    foot.append([x,y-1])
    foot.append([x,y+1])
    foot.append([x-1,y])
    foot.append([x+1,y])
    return foot

LED_n = [37,37,36,38,39,40,40,41,42,42,42,43]

for i in range(1,5):
    pos_l = footprint(i*3,i*8,LED_n)

    test = []

    for i in pos_l:
        pos = position(i[0],i[1],LED_n)
        test.append(pos)
    light(test)
    time.sleep(1)









'''
ind = 0

for i in LED_num:
    ind += i
    strip.setPixelColor(ind,Color(255,0,0))
    strip.show()
    time.sleep(0.01)
    strip.setPixelColor(ind,Color(0,0,0))
    strip.show()
    time.sleep(0.01)
'''




#for x in range(0,LED_COUNT):
    




#https://gist.github.com/chris-gong/fbebf494725cc762d731d567700fdafa