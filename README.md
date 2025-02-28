# ros2workshop

# System setup
 - [Linux setup](linux_setup.md)
 - [Windows setup](windows_setup.md)

# Things covered
**Workshop 1**
 - [Configuring the environment](https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Configuring-ROS2-Environment.html)
 - [Turtlesim](https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim.html)
 - [Understanding Nodes, Topics, Services, Parameters, RQT](https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools.html)

**Workshop 2**
 - [Configuring workspaces and packages](workspaces_packages.md)

**Workshop 3**
 - [Installig Docker](docker_install.md)
 - [Writing a Python Publisher with VSCode and Docker](publisher_docker_vscode.md)


# Simulated robot

Run with 

    ros2 launch myrobot_gazebo robot.launch.py

And control with 

    ros2 run teleop_twist_keyboard teleop_twist_keyboard

