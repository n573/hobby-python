from __future__ import division  # required for python 2
from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=9, green=10, blue=11)
while True:
    led.color = (0, .5, 0)  # green
    sleep(0.2)
    led.color = (.5, 0, .5)  # magenta
    sleep(0.2)
    led.color = (.5, .5, 0)  # yellow
    sleep(0.2)
    led.color = (0, .5, .5)  # cyan
    sleep(0.2)
    led.color = (.5, .5, .5)  # white
    sleep(0.2)
led.color = (0, 0, 0)  # off
