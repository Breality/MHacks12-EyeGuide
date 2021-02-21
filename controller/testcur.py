import RPi.GPIO as GPIO # ImportRaspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True: # Run forever
    
    if GPIO.input(8) == GPIO.HIGH:
        print("Pushed")

