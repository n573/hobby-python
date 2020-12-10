from bluedot import BlueDot
from signal import pause
import pin_control as pin

def dpad(pos):
    if pos.top:
        print("forward")
        pin.set_color('red','on')
    elif pos.bottom:
        print("backward")
        pin.set_color('blue','on')
    elif pos.left:
        print("left")
        pin.set_color('yellow','on')
    elif pos.right:
        print("right")
        pin.set_color('green','on')
    elif pos.middle:
        print("stop")
        pin.all_off()
    else:
        pin.all_off()


bd = BlueDot()
bd.when_pressed = pin.all_on
bd.when_moved = dpad

pause()