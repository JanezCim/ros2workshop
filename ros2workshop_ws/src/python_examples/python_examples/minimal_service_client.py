import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn

class MinimalServiceClient(Node):

    def __init__(self):
        super().__init__('minimal_service_client')
        self.spawn_srv = self.create_client(Spawn, '/spawn')        
        
        while not self.spawn_srv.wait_for_service(timeout_sec=2.0):
            if not rclpy.ok():
                self.get_logger().error('Interruped while waiting for the server.')
                return
            else:
                self.get_logger().info('Server not available, waiting again...')
        
        self.request = Spawn.Request()
        self.request.name = "turtle2"
        self.future = self.spawn_srv.call_async(self.request)
        self.future.add_done_callback(self.srv_response_cb)
    

    def srv_response_cb(self, future):
        response = self.future.result()
        self.get_logger().info(f'Received response: {response}')

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(MinimalServiceClient())
    rclpy.shutdown()

if __name__ == '__main__':
    main()