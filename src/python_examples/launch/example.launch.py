from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),  
        Node(package='python_examples',
             executable='turtle_dance',
             name='turtle_dance'
        )
    ])