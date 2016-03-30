import socket
import RPi.GPIO as GPIO


HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
pwm1 = GPIO.PWM(18, 100)
pwm2 = GPIO.PWM(8, 100)

pwm1.start(5)
pwm2.start(5)

def update(xaxis, yaxis):
    duty1 = float(xaxis) / 10.0 + 2.5
    duty2 = float(yaxis) / 10.0 + 2.5

    pwm1.ChangeDutyCycle(duty1)
    pwm2.ChangeDutyCycle(duty2)



print('Connected by', addr)
while True:
    data = conn.recv(7)
    if data:
        data = data.decode("utf-8")
        angles = str(data).split(',')
        xaxis = angles[0]
        yaxis = angles[1]
        update(xaxis, yaxis)
conn.close()








