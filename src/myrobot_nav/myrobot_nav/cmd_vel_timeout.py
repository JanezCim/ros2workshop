import rclpy
from rclpy.node import Node
from rclpy.time import Duration
from geometry_msgs.msg import Twist

class CmdVelTimeout(Node):

    def __init__(self):
        super().__init__('cmd_vel_timeout_node')
        self.timeout_s = Duration(seconds=1.0)
        self.clock = self.get_clock()
        self.last_msg_time = None
        self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.cmd_sub = self.create_subscription(Twist, '/cmd_vel', self.cmd_cb, 10)
        self.cmd_timeout_check_timer = self.create_timer(0.5, self.cmd_timeout_check_cb)

    def cmd_cb(self, cmd:Twist):
        self.cmd_pub.publish(cmd)
        self.last_msg_time = self.clock.now()

    def cmd_timeout_check_cb(self):
        if self.last_msg_time:
            time = self.clock.now() - self.last_msg_time
            self.get_logger().info(f'{time}')
            if self.clock.now() - self.last_msg_time > self.timeout_s:
                self.cmd_pub.publish(Twist())
                self.last_msg_time = None


def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(CmdVelTimeout())
    rclpy.shutdown()

if __name__ == '__main__':
    main()


