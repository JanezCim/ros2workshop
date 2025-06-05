import rclpy
from rclpy.node import Node
import rclpy.signals
from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
import math
import tf_transformations


class PathFollower(Node):
    
    def __init__(self):
        super().__init__('path_follower_node')
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.marker_pub = self.create_publisher(Marker, 'line_marker', 10)
        self.pose_sub = self.create_subscription(Odometry, '/odom', self.pose_callback, 10)
        self.waypoints = [[0.0, 0.1], [2.0, 2.0], [3.0, -1.0]]
        self.current_waypoint_index = 0
        self.current_pose = Pose()
        self.timer = self.create_timer(0.1, self.spin_once) 
        
    def pose_callback(self, received_msg:Odometry):
        self.current_pose = received_msg.pose.pose
    
    def spin_once(self):
        self.draw_waypoints()
        if self.current_waypoint_index < len(self.waypoints):
            target = self.waypoints[self.current_waypoint_index]
            distance = math.sqrt((target[0] - self.current_pose.position.x)**2 + (target[1] - self.current_pose.position.y)**2)

            if distance < 0.1:  # Close enough to the waypoint
                self.current_waypoint_index += 1
                return
            
            # Calculate steering angle and velocity
            angle_to_target = math.atan2(target[1] - self.current_pose.position.y, target[0] - self.current_pose.position.x)
            r, p, y = tf_transformations.euler_from_quaternion([self.current_pose.orientation.x,
                                                                self.current_pose.orientation.y,
                                                                self.current_pose.orientation.z,
                                                                self.current_pose.orientation.w])
            self.get_logger().info("Angle to target: " + str(angle_to_target) + " angle: " + str(y))
            twist_msg = Twist()
            twist_msg.linear.x = 0.25
            twist_msg.angular.z = angle_to_target - y

            self.cmd_vel_pub.publish(twist_msg)
        else:
            self.get_logger().info("Finished path")
            self.cmd_vel_pub.publish(Twist())
    
    def draw_waypoints(self):
        marker = Marker()
        # Set up the marker properties
        marker.header.frame_id = 'odom'  # Change to your frame of reference
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = 'lines'
        marker.id = 0
        marker.type = Marker.LINE_STRIP
        marker.action = Marker.ADD
        
        # Set the scale and color of the line
        marker.scale.x = 0.02  # Line width
        marker.color.r = 1.0    # Red color
        marker.color.g = 0.0
        marker.color.b = 0.0
        marker.color.a = 1.0    # Full opacity
        
        for p in self.waypoints:
            point = Point()
            point.x = p[0]
            point.y = p[1]
            marker.points.append(point)
        
        self.marker_pub.publish(marker)


def main(args=None):
    rclpy.init(args=args)
    path_follower_node = PathFollower()
    rclpy.spin(path_follower_node)
    path_follower_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
