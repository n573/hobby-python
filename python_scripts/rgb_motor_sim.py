from gpiozero import RGBLED
from bluedot import BlueDot
from signal import pause
from gpiozero import Robot

#led = RGBLED(red=9, green=10, blue=11)
bd = BlueDot()
robot = Robot(left = (9,10), right = (,11))
def dpad(pos):
    #ex=pos.x
    #wy=pos.y
    #turn=(pos.x+1)/2
    #speed = (pos.y+1)/2
    #led.color = (turn,speed,0)
	#led.color = (abs(ex/2, abs(wy)/2, abs((pos.x+pos.y)/2))
    #if(pos.x>0) & (pos.x<1) & (pos.y>0) & (pos.y<1):
    #    led.color(1,pos.x,pos.y)
    #else:
    #    led.color(1,1,1)
    robot.right
    sleep(5)
    robot.left

#bd.when_pressed = dpad
bd.when_moved = dpad

pause()