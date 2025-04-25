# ros2workshop

# System setup
1. [Install Docker](https://docs.docker.com/engine/install/) 
    
    Make sure you have sudo-less Docker setup with 
    
        sudo usermod -aG docker $USER

    After which the computer should be restarted.

2. Clone this repository into prefered directory:

        git clone https://github.com/JanezCim/ros2workshop.git

3. Inside the directory execute `./run_env` which will take you to Docker environment

4. Once inside docker environment (indicated by orange username and hostname) navigate to the workspace, build and source environment:

        cd ~/ros2workshop_ws/
        colcon build --symlink-install --cmake-args=-DCMAKE_BUILD_TYPE=Release
        source install/local_setup.bash

# Things covered
**Workshop 1**
 - [Configuring the environment](https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Configuring-ROS2-Environment.html)
 - [Turtlesim](https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim.html)
 - [Understanding Nodes, Topics, Services, Parameters, RQT](https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools.html)

**Workshop 2**
 - [Configuring workspaces and packages](workspaces_packages.md)

**Workshop 3**
 - [Writing a minimal Python Publisher](minimal_python_publisher.md)


# Simulated robot

Run with 

    ros2 launch myrobot_gazebo robot.launch.py

And control with 

    ros2 run teleop_twist_keyboard teleop_twist_keyboard

