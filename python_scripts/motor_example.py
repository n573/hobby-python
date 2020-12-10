# Write your code here :-)
#from bluedot import BlueDot
from time import sleep
import motor_pins as pin

pin.p1.start(50)
pin.p2.start(50)

#forward
print('f')
pin.set('d1','on')
pin.set('d3', 'on')
#pin.p1.speed_up
#pin.p2.speed_up
sleep(5)
#pin.p1.slow_down
#pin.p2.slow_down
sleep(5)
pin.coast
sleep(2)
#backward
print('b')
pin.set('d1','off')
pin.set('d2','on')
pin.set('d3','off')
pin.set('d4','on')
#pin.p1.speed_up
#pin.p2.speed_up
sleep(5)
pin.coast
sleep(2)
#forward_turn
print('ft')
pin.p1.ChangeDutyCycle(75)
pin.p1.ChangeDutyCycle(25)
pin.set('d2','off')
pin.set('d1','on')
pin.set('d4','off')
pin.set('d3','on')
sleep(5)
pin.coast()
sleep(2)
#backward_turn
print('bt')
pin.p1.ChangeDutyCycle(25)
pin.p1.ChangeDutyCycle(75)
pin.set('d1','off')
pin.set('d2','on')
pin.set('d3','off')
pin.set('d4','on')
sleep(5)
pin.coast()
print('done')
