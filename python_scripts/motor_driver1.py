from bluedot import BlueDot
import motor as mot
from time import sleep
from signal import pause
bd = BlueDot()

def dpad(pos):
    if pos.top:
        mot.forward()
    elif pos.right:
        mot.right(round(pos.x))
    elif pos.left:
        mot.left(-round(pos.x))
    elif pos.bottom:
        mot.backward
    elif pos.middle:
        mot.pin.coast()
    else:
        sleep(1)
bd.when_moved = dpad
pause()
#while 1:
#    mot.forward()
#    mot.speed_up(90)
#    sleep(1.5)
#    mot.slow_down(90)
#    sleep(1.5)
#    mot.pin.coast()
#    sleep(1.5)
#    mot.backward()
#    sleep(1)
#    mot.pin.coast()
#    sleep(1.5)
#    mot.left()
#    sleep(1)
#    mot.pin.coast()
#    sleep(1.5)
#    mot.right