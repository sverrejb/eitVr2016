import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
pwm1 = GPIO.PWM(18, 100)
pwm2 = GPIO.PWM(8, 100)

pwm1.start(5)
pwm2.start(5)


def update(angle):
    duty = float(angle) / 10.0 + 2.5
    pwm1.ChangeDutyCycle(duty)
    pwm2.ChangeDutyCycle(duty)

while True:
    angle = int(input('Vinkel: '))+25
    update(angle)
    