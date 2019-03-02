import time,sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

LED_PIN_red = 15
LED_PIN_green = 18
LED_PIN_blue = 23
GPIO.setup(LED_PIN_red, GPIO.OUT)
GPIO.setup(LED_PIN_green, GPIO.OUT)
GPIO.setup(LED_PIN_blue, GPIO.OUT)
def led_reset():
    GPIO.output(LED_PIN_red, GPIO.LOW)
    GPIO.output(LED_PIN_green, GPIO.LOW)
    GPIO.output(LED_PIN_blue, GPIO.LOW)
def led_red():
    GPIO.output(LED_PIN_red, GPIO.HIGH)
    
def led_green():
    GPIO.output(LED_PIN_green, GPIO.HIGH)
    
    
def led_blue():
    GPIO.output(LED_PIN_blue, GPIO.HIGH)

def led_blue_illegal():
    for i in range(0,50):
        GPIO.output(LED_PIN_blue, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN_blue, GPIO.LOW)
        time.sleep(0.5)
