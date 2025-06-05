#! /usr/bin/env python3
import rclpy
import math
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
from std_srvs.srv import Empty

class RobotManipulator(Node):

    def __init__(self):
        super().__init__('robot_manipulator')

        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.forward_srv = self.create_service(Empty, '/send_forward', self.forward_cb)
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_cb, 10)
        self.innitial_pose = Point()
        self.travel_distance = 1
        self.travel_speed = 0.5
        self.cmd_vel_msg = Twist()
        self.cmd_timer = self.create_timer(0.5, self.cmd_timer_cb)

    def odom_cb(self, odom:Odometry):
        if not self.innitial_pose:
            self.innitial_pose = odom.pose.pose.position

        if self.innitial_pose.x == 0 and self.innitial_pose.y == 0:
            return

        if self.distance2d(self.innitial_pose, odom.pose.pose.position) < self.travel_distance:
            self.cmd_vel_msg.linear.x = self.travel_speed
        else:
            self.cmd_vel_msg.linear.x = 0.0
    
    def distance2d(self, p1:Point, p2:Point):
        return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    
    def cmd_timer_cb(self):
        self.cmd_pub.publish(self.cmd_vel_msg)

    def forward_cb(self, _, res):
        self.get_logger().info(f'Received request to send robot forward for {self.travel_distance}m.')
        self.innitial_pose = None
        return res


def main(args=None):
    rclpy.init(args=args)
    rm = RobotManipulator()
    rclpy.spin(rm)
    rm.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()