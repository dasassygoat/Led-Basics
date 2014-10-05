import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)

gpio.output(17, 1)
time.sleep(200)


gpio.cleanup()
