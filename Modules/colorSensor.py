import RPi.GPIO as GPIO
import time

# port of sensor
s2 = 23
s3 = 24
signal = 25

# set up port 
GPIO.setmode(GPIO.BCM)
GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(s2,GPIO.OUT)
GPIO.setup(s3,GPIO.OUT)

# set the cycle of color detection
NUM_CYCLES = 10

# read value of Red
GPIO.output(s2,GPIO.LOW)
GPIO.output(s3,GPIO.LOW)
time.sleep(0.3)
start = time.time()
for impulse_count in range(NUM_CYCLES):
    GPIO.wait_for_edge(signal, GPIO.FALLING)
duration = time.time() - start      #seconds to run for loop
red  = NUM_CYCLES / duration   #in Hz
print("red value - ",red)

# read value of Blue
GPIO.output(s2,GPIO.LOW)
GPIO.output(s3,GPIO.HIGH)
time.sleep(0.3)
start = time.time()
for impulse_count in range(NUM_CYCLES):
    GPIO.wait_for_edge(signal, GPIO.FALLING)
duration = time.time() - start
blue = NUM_CYCLES / duration
print("blue value - ",blue)

# read value of Green
GPIO.output(s2,GPIO.HIGH)
GPIO.output(s3,GPIO.HIGH)
time.sleep(0.3)
start = time.time()
for impulse_count in range(NUM_CYCLES):
    GPIO.wait_for_edge(signal, GPIO.FALLING)
duration = time.time() - start
green = NUM_CYCLES / duration
print("green value - ",green)