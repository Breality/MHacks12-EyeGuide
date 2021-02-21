from gpiozero import DistanceSensor
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

sensorLeft = DistanceSensor(echo=17, trigger=16)
#sensorCenter = DistanceSensor(echo=19, trigger=18)


def beepLeft():
    vibLeft = 16
    GPIO.setup(vibLeft,GPIO.OUT)
    p = GPIO.PWM(vibLeft,50)
    p.start(0)
    for i in range (5):
        p.ChangeDutyCycle(8)
        sleep(0.2)
        p.ChangeDutyCycle(5.7)
        sleep(0.2)
        p.ChangeDutyCycle(8)
        sleep(0.2)
        p.ChangeDutyCycle(10.3)
        sleep(0.2)
    p.ChangeDutyCycle(8)
    sleep(2)
    p.stop()
        
def beepRight():
    vibLeft = 16
    GPIO.setup(vibLeft,GPIO.OUT)
    p = GPIO.PWM(vibLeft,50)
    p.start(0)
    for i in range (5):
        p.ChangeDutyCycle(8)
        sleep(0.2)
        p.ChangeDutyCycle(10.3)
        sleep(0.2)
        p.ChangeDutyCycle(8)
        sleep(0.2)
        p.ChangeDutyCycle(5.7)
        sleep(0.2)
    p.ChangeDutyCycle(8)
    sleep(2)
    p.stop()
             

while True:
    if(sensorLeft.distance!=100):
        print("beep Left")
        #beepLeft()

    print('Distance: ', sensorLeft.distance *100)
    #print('Distance: ', sensorCenter.distance *100)
    