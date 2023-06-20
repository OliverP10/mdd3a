import rospy
from mdd3a.msg import Motor

def pwm_publisher():
    rospy.init_node("motor_debug_publisher", anonymous=True)
    pub = rospy.Publisher("motor_control_topic", Motor, queue_size=10)

    while not rospy.is_shutdown():
        try:
            motor_speed = input("Enter motor speed: ").split()
            data = Motor()
            data.left = round(float(motor_speed[0]),2)
            data.right = round(float(motor_speed[1]),2)
            pub.publish(data)
            # rospy.loginfo("Published motor msg: Left: %s Right: %s", data.left, data.right)
        except Exception as e:
            rospy.loginfo(e)
            rospy.loginfo("Invalid input")

if __name__ == '__main__':
    try:
        pwm_publisher()
    except rospy.ROSInterruptException:
        pass