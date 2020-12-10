from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

while True:
    led.value = 0  # off
    sleep(0.3)
    led.value = 0.25
    sleep(0.3)
    led.value = 0.5  # half brightness
    sleep(0.3)
    led.value = 0.75
    sleep(0.3)
    led.value = 1  # full brightness
    sleep(0.3)
