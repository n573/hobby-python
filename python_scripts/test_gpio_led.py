import RPi.GPIO as GPIO

pins = [{'pin_num': 9, 'color': 'red'},
        {'pin_num': 10, 'color': 'yellow'},
        {'pin_num': 11, 'color': 'blue'}]

GPIO.setmode(GPIO.BCM)  # use GPIO numbering, not generic


# setup all pins based on above configuration
for pin in pins:
    GPIO.setup(pin['pin_num'], GPIO.OUT, initial=GPIO.LOW)

def toggle_color(color, state):
    pin_nums = [pin['pin_num'] for pin in pins if pin['color'] == color]
    for pin_num in pin_nums:
        if state == 'on':
            GPIO.output(pin_num, GPIO.HIGH)
        elif state == 'off':
            GPIO.output(pin_num, GPIO.LOW)