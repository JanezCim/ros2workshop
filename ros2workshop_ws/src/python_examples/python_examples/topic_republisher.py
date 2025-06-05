import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MinimalRepublisher(Node):

    def __init__(self):
        super().__init__('topic_republisher')
        self.publisher_ = self.create_publisher(String, 'republished_topic', 10)
        self.subscriber_ = self.create_subscription(String, 'topic', self.sub_callback, 10)

    def sub_callback(self, received_msg:String):
        self.publisher_.publish(received_msg)
        self.get_logger().info('Publishing: "%s"' % received_msg.data)


def main(args=None):
    rclpy.init(args=args)
    minimal_republisher = MinimalRepublisher()
    rclpy.spin(minimal_republisher)
    minimal_republisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
