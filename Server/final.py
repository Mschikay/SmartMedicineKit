from twilio.rest import Client
import led
import threading
import alarm
import RPi.GPIO as GPIO
import sockettest
import time

GPIO.setmode(GPIO.BCM)

touch_D0= 21
button_pin = 20

GPIO.setup(touch_D0, GPIO.IN)
GPIO.setup(button_pin, GPIO.IN)
data = []

def sendmsg(text):
    account_id = "AC4bef835d93cacb8df0a54bf789fa7231"
    auto_token = "c475c3eb65375309f307b5f7b540e825"

    client = Client(account_id, auto_token)
    message = client.messages.create(
        to = "+14125006861",
        from_ = "+16108803667",
        body = text)


def countTime():
    while True:
        newCurrTime = ""
        currTime = time.strftime("%H%M")
        for c in range(len(currTime)):
            if currTime[c] == " ":
                newCurrTime += "0"
            else:
                newCurrTime += currTime[c]
        if newCurrTime == sockettest.INTENDTIME:
            print("alarm")
            remove_alarm()
            break

def remove_alarm():
    led.led_reset()
    led.led_green()

def read_illegal():
    while True:
        if(GPIO.input(button_pin) == GPIO.LOW):
            sendmsg("the medicine kit is opened before time!")
            alarm.run_illegal()
            
            
def read_lost():
    while True:
        if(sockettest.status_lost_socket == 1):
            sendmsg("the medicine kit is missing!")
            alarm.run_lost()
            sockettest.status_lost_socket = 0
            
if __name__ == "__main__":
    led.led_reset()
    led.led_blue()
    sthreadrun1 = threading.Thread(target=countTime)
    sthreadrun1.start()
    
    sthreadrun2 = threading.Thread(target=sockettest.OpenSocket)
    sthreadrun2.start()
    
    sthreadrun3 = threading.Thread(target=read_illegal)
    sthreadrun3.start()
    
    sthreadrun4 = threading.Thread(target=read_lost)
    sthreadrun4.start()