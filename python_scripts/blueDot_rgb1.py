#from __future__ import division  # required for python 2
from gpiozero import RGBLED
from bluedot import BlueDot
from signal import pause

led = RGBLED(red=9, green=10, blue=11)
bd = BlueDot()
def dpad(pos):
	led.color = (abs(pos.x)/2, abs(pos.y)/2, abs((pos.x+pos.y)/2))
	#print((1+pos.x)/2)
	#print((1+pos.y)/2)
	#print(abs(((pos.x+pos.y)))/2)

#bd.when_pressed = dpad
bd.when_moved = dpad

pause()
