import rospy
from mdd3a.msg import Motor
import random

def pwm_publisher():
    rospy.init_node("motor_test_publisher", anonymous=True)
    pub = rospy.Publisher("motor_control_topic", Motor, queue_size=10)
    rate = rospy.Rate(1)  # Publish at 1Hz (1 message per second)

    while not rospy.is_shutdown():
        data = Motor()
        data.left = random.uniform(-1, 1)
        data.right = random.uniform(-1, 1)

        pub.publish(data)
        rospy.loginfo("Published motor msg: Left: %s Right: %s", data.left, data.right)

        rate.sleep()

if __name__ == '__main__':
    try:
        pwm_publisher()
    except rospy.ROSInterruptException:
        pass