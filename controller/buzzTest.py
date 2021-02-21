
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


buzzer = 16
GPIO.setup(buzzer,GPIO.OUT)
p = GPIO.PWM(buzzer,50)
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
GPIO.cleanup()
