import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose
from turtlesim.srv import Spawn
from geometry_msgs.msg import Twist

class TurtleDance(Node):

    def __init__(self):
        super().__init__('turtle_dance')
        self.declare_parameter('x', 0.)
        self.declare_parameter('y', 0.)

        self.turd_client = self.create_client(Spawn, '/spawn')
        self.turd_client.wait_for_service()
        spawn_msg = Spawn.Request()
        spawn_msg.name = self.get_name()

        spawn_msg.x = self.get_parameter('x').get_parameter_value().double_value
        spawn_msg.y = self.get_parameter('y').get_parameter_value().double_value
        self.future = self.turd_client.call_async(spawn_msg)
        self.future.add_done_callback(self.spawn_res_cb)
        
        self.publisher_ = self.create_publisher(Twist, '~/cmd_vel', 10)
        self.subscriber = self.create_subscription(Pose, '/turtle1/pose', self.sub_cb, 10)

    def sub_cb(self, msg:Pose):
        cmd = Twist()
        cmd.linear.x = msg.linear_velocity
        cmd.angular.z = msg.angular_velocity
        self.publisher_.publish(cmd)

    def spawn_res_cb(self, future):
        response = self.future.result()
        self.get_logger().info(f'Received response: {response}')

def main(args=None):
    rclpy.init(args=args)

    turtle_dance = TurtleDance()

    rclpy.spin(turtle_dance)
    turtle_dance.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
