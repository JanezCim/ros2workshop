import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    sim_launch_descr = PythonLaunchDescriptionSource(
        os.path.join(
            get_package_share_directory('myrobot_gazebo'),
            'launch',
            'robot.launch.py'
        )
    )
    return LaunchDescription([
        Node(
            package='python_examples',
            executable='robot_manipulator',
            name='robot_manipulator',
            output='screen'),
        IncludeLaunchDescription(sim_launch_descr)
    ])
