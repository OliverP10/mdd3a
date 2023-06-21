import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(6,GPIO.OUT) # Left Motor A
GPIO.setup(12,GPIO.OUT) # Left Motor B

left_motor_a = GPIO.PWM(6, 500)
left_motor_b = GPIO.PWM(12, 500)

left_motor_a.start(0)
left_motor_b.start(0)

left_motor_a.ChangeDutyCycle(0)
left_motor_b.ChangeDutyCycle(0)

input()

