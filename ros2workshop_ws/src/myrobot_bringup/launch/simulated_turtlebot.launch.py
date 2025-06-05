import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node




def generate_launch_description():
    gazebo_robot_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
        os.path.join(get_package_share_directory('myrobot_gazebo'),
            'launch',
            'robot.launch.py')
        )
    )

    cmd_timeout_node =  Node(
        package='myrobot_nav',
        executable='cmd_vel_timeout',
        name='cmd_vel_timeout',
        output='screen')

    return LaunchDescription([
        gazebo_robot_launch,
        cmd_timeout_node
    ])
