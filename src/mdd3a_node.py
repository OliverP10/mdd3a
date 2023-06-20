import rospy
from mdd3a.msg import Motor
import RPi.GPIO as GPIO

left_motor_a: GPIO.PWM = None
left_motor_b: GPIO.PWM = None
right_motor_a: GPIO.PWM = None
right_motor_b: GPIO.PWM = None

motor_status = Motor()

# Setup the mdd3a
def setup_mdd3a():
    global left_motor_a 
    global left_motor_b 
    global right_motor_a
    global right_motor_b

    # Set up the GPIO
    GPIO.setmode(GPIO.BCM)

    # Set up the GPIO channels
    GPIO.setup(12,GPIO.OUT) # Left Motor A
    GPIO.setup(13,GPIO.OUT) # Left Motor B
    GPIO.setup(18,GPIO.OUT) # Right Motor A
    GPIO.setup(19,GPIO.OUT) # Right Motor B

    # Set up the PWM channels
    left_motor_a = GPIO.PWM(12, 500)
    left_motor_b = GPIO.PWM(13, 500)
    right_motor_a = GPIO.PWM(18, 500)
    right_motor_b = GPIO.PWM(19, 500)

    # Start the PWM channels
    left_motor_a.start(0)
    left_motor_b.start(0)
    right_motor_a.start(0)
    right_motor_b.start(0)

    rospy.loginfo("MDD3A Setup Complete")

def set_motor_speeds(data):
    global motor_status
    motor_status = data

    data.left = data.left * 100
    data.right = data.right * 100

    if(data.left >= 0):
        left_motor_a.ChangeDutyCycle(data.left)
        left_motor_b.ChangeDutyCycle(0)
        rospy.loginfo("Forward a: %s b: %s", data.left, 0)
    else:
        left_motor_a.ChangeDutyCycle(0)
        left_motor_b.ChangeDutyCycle(-data.left)
        rospy.loginfo("Backwards a: %s b: %s", 0, -data.left)

    if(data.right >= 0):
        right_motor_a.ChangeDutyCycle(data.right)
        right_motor_b.ChangeDutyCycle(0)
        # rospy.loginfo("Forward a: %s b: %s", data.right, 0)
    else:
        right_motor_a.ChangeDutyCycle(0)
        right_motor_b.ChangeDutyCycle(-data.right)
        # rospy.loginfo("Backwards a: %s b: %s", 0, -data.right)

    # rospy.loginfo("Left: %s Right: %s", data.left, data.right)
        
def motor_subscriber():
    rospy.loginfo("Starting motor subscriber")
    rospy.init_node("motor_control_node", anonymous=True)
    rospy.Subscriber("motor_control_topic", Motor, set_motor_speeds)
    rospy.spin()

if __name__ == '__main__':
    try:
        setup_mdd3a()
        motor_subscriber()
    except rospy.ROSInterruptException:
        pass