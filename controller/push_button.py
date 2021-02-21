import RPi.GPIO as GPIO # ImportRaspberry Pi GPIO library
import time
import requests


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
connections = {"Green" : 10, "Yellow" : 12, "Red" : 16, "Blue" : 18}
endPoints = {"Green" : "callFriend", "Yellow" : "checkVision", "Red" :  "emergency", "Blue" : "readText"}
for con in connections:
    GPIO.setup(connections[con], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
while True: # Run forever
    for con in connections: 
        if GPIO.input(connections[con]) == GPIO.HIGH:
            print(con, "was pushed!")
            if con in endPoints:
                requests.get("http://mhacks12noor.ddns.net:5000/" + endPoints[con])
            time.sleep(0.25)
    
