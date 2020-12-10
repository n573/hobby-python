#from __future__ import division  # required for python 2
from gpiozero import RGBLED
from bluedot import BlueDot
from signal import pause

led = RGBLED(red=9, green=10, blue=11)
bd = BlueDot()

def dpad(pos):
    if pos.top:
        led.color = (0, pos.y, 0)  # green
	#led.color = (0, .5, 0)  # green
	bd.color = "green"
    elif pos.bottom:
	led.color = (pos.x, pos.y, 0)
        #led.color = (.5, 0, .5)  # magenta
	bd.color = "magenta"
    elif pos.left:
	led.color = (pos.y, pos.x, 0)  # green
        #led.color = (.5, .5, 0)  # yellow
	bd.color = "yellow"
    elif pos.right:
        led.color = (0, pos.x, pos.y)  # cyan
	bd.color = "cyan"
    elif pos.middle:
        led.color = (pos.x, pos.y, (pos.x+pos.y)/2)  # white
	bd.color = "white"


#bd.when_pressed = dpad
bd.when_moved = dpad

pause()
