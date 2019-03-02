import time,sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

touch_D0= 21
touch_A0 = 27

GPIO.setup(touch_D0, GPIO.IN)
data = []

def detect():
    
    time.sleep(1)
    #GPIO.output(touch_D0,GPIO.HIGH)
    if GPIO.input(touch_D0) == GPIO.HIGH:
        data.append(1)
    if GPIO.input(touch_D0) == GPIO.LOW:
        data.append(0)
    print(data, GPIO.input(touch_D0))
