#from __future__ import division  # required for python 2
from gpiozero import RGBLED
from bluedot import BlueDot
from signal import pause

led = RGBLED(red=9, green=10, blue=11)
bd = BlueDot()

def dpad(pos):
    if pos.top:
        led.color = (0, .5, 0)  # green
	bd.color = "green"
    elif pos.bottom:
        led.color = (.5, 0, .5)  # magenta
	bd.color = "magenta"
    elif pos.left:
        led.color = (.5, .5, 0)  # yellow
	bd.color = "yellow"
    elif pos.right:
        led.color = (0, .5, .5)  # cyan
	bd.color = "cyan"
    elif pos.middle:
        led.color = (.5, .5, .5)  # white
	bd.color = "white"
    else:
	led.color = (0, 0, 0)  # off


#bd.when_pressed = dpad
bd.when_moved = dpad

pause()
