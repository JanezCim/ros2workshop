#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class ScanSubscriber(Node):

    def __init__(self):
        super().__init__('topic_republisher')
        self.subscriber_ = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)

    def scan_callback(self, received_msg:LaserScan):
        self.get_logger().info('Received: "%s"' % received_msg)

def main(args=None):
    rclpy.init(args=args)
    scan_subscriber = ScanSubscriber()
    rclpy.spin(scan_subscriber)
    scan_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()