import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math


class PrintPose(Node):

    def __init__(self):
        super().__init__('print_pose')
        self.pose_sub = self.create_subscription(
            Pose, '/turtle1/pose', self.pose_cb, 10)
        self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.first_pose = None

    def pose_cb(self, msg:Pose):
        if not self.first_pose:
            self.first_pose = msg

        cmd_msg = Twist()
        if self.dis(self.first_pose, msg) < 2.0:
            cmd_msg.linear.x = 0.5
            self.cmd_pub.publish(cmd_msg)

    def dis(self, p1:Pose, p2:Pose):
        return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

def main(args=None):
    rclpy.init(args=args)
    pp = PrintPose()
    rclpy.spin(pp)
    rclpy.shutdown()

if __name__ == '__main__':
    main()


