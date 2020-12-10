from bluedot import BlueDot
from time import sleep
import motor_pins as pin

#pin.p1.start(50)
#pin.p2.start(50)
pin.p1.start(0)
pin.p2.start(0)

def forward():
    print('f')
    pin.set('d1','on')
    pin.set('d2','off')
    pin.set('d3', 'on')
    pin.set('d4','off')

def backward():
    print('b')
    pin.set('d1','off')
    pin.set('d2','on')
    pin.set('d3', 'off')
    pin.set('d4','on')

#def left():
#    pin.set('d1','on')
#    pin.set('d2','off')
#    pin.set('d3', 'off')
#    pin.set('d4','off')

#def right():
#    pin.set('d1','on')
#    pin.set('d2','off')
#    pin.set('d3', 'on')
#    pin.set('d4','off')

def speed_up(i):
    print("speed_up")
    for x in range (i):                          #execute loop for 50 times, x being incremented from 0 to 49.
        pin.p1.ChangeDutyCycle(x)
        pin.p2.ChangeDutyCycle(x)
        sleep(0.1)                           #sleep for 100m second

def slow_down(i):
    print("slow_down")
    for x in range (i):                         #execute loop for 50 times, x being incremented from 0 to 49.
        pin.p1.ChangeDutyCycle(i-x)
        pin.p2.ChangeDutyCycle(i-x)
        sleep(0.1)                          #sleep for 100m second

def right(i):
    print("right")
    for x in range (i):
        pin.p1.ChangeDutyCycle(i-x)
        pin.p2.ChangeDutyCycle(x)
        sleep(0.1)

def left(i):
    print("left")
    for x in range (i):
        pin.p1.ChangeDutyCycle(x)
        pin.p2.ChangeDutyCycle(i-x)
        sleep(0.1)

#while 1:
#    forward()
#    speed_up(80)
#    sleep(1.5)
#    slow_down(80)
#    sleep(1.5)
#    pin.coast()
#    sleep(2.5)
#    backward()
#    speed_up(90)
#    sleep(1)
#    slow_down(90)
#    sleep(1)
#    pin.coast
#    sleep(1.5)
#    right(75)
#    sleep(2)
#    pin.coast()
#    sleep(1.5)
#    left(75)
#    sleep(2)
#    pin.coast()
#    sleep(1.5)


#forward
#pin.set('d1','on')
#pin.set('d3', 'on')
#sleep(5)
#pin.all_off
#sleep(2)
#backward
#pin.set('d1','off')
#pin.set('d2','on')
#pin.set('d3','off')
#pin.set('d4','on')
#sleep(5)
#pin.all_off
#sleep(2)
#forward_turn
#pin.p1.ChangeDutyCycle(75)
#pin.p1.ChangeDutyCycle(25)
#pin.set('d2','off')
#pin.set('d1','on')
#pin.set('d4','off')
#pin.set('d3','on')
#sleep(5)
#pin.all_off()
#sleep(2)
#backward_turn
#pin.p1.ChangeDutyCycle(25)
#pin.p1.ChangeDutyCycle(75)
#pin.set('d1','off')
#pin.set('d2','on')
#pin.set('d3','off')
#pin.set('d4','on')
#sleep(5)
#pin.all_off()