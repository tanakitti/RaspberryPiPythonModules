import RPi.GPIO as GPIO
import time

servoPIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
try:
    angle = 180
    duty = angle / 18 + 2
    p.ChangeDutyCycle(5)
    time.sleep(1)
    GPIO.output(servoPIN, False)
    p.ChangeDutyCycle(2)
    time.sleep(1)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
