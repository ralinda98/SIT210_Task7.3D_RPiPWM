import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

BUZZFREQ = 10

BUZZ = 21
TRIG = 3
ECHO = 2

# Setting up PWM for buzzer
GPIO.setup(BUZZ, GPIO.OUT)
buzz = GPIO.PWM(BUZZ, BUZZFREQ)
buzz.start(0)

# Setting pins for ultrasonic sensor
GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, 0)
GPIO.setup(ECHO, GPIO.IN)

time.sleep(0.1)
loop = 1

while(loop == 1):
    print ("Duty Cycle:")

    GPIO.output(TRIG, 1)
    time.sleep(0.001)     # Only trigger for 10 micro seconds
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        pass                         # Pass tells program to do nothing but loop
    start = time.time()              # When input is 1, the start time will be recorded

    while GPIO.input(ECHO) == 1:
        pass
    stop = time.time()               # When input is 0, the stop time will be recorded

    # Speed of light is 340m/s. Because the sound
    # travels both ways we will be halving the distance.
    # 170m x 100 will be 17000cm
    dc = 100 - ((stop - start) * 17000)
    if dc <= 0:
        dc = 0
    buzz.ChangeDutyCycle(dc)
    print(dc)