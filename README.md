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

And controll with 

    ros2 run teleop_twist_keyboard teleop_twist_keyboard

# Resources
Docker install https://docs.docker.com/engine/install/

ROS2 on Docker https://docs.ros.org/en/jazzy/How-To-Guides/Run-2-nodes-in-single-or-separate-docker-containers.html


# Additional debug info

## Experiencing issues opening visual programs on Docker container?
Solution: run `xhost +local:docker` on host before running container (tested on Ubuntu18.04). Full conversation about this [here](https://github.com/JanezCim/ros2workshop/issues/1).



Enabling on windows

Install VScode, docker desktop

install xhost https://stackoverflow.com/questions/44429394/x11-forwarding-of-a-gui-app-running-in-docker

https://www.youtube.com/watch?v=qWuudNxFGOQ

Some other common problems: https://docs.ros.org/en/jazzy/How-To-Guides/Installation-Troubleshooting.html#windows

Great video tutorials: https://www.youtube.com/watch?v=RbP5cARP-SM&list=PLunhqkrRNRhaqt0UfFxxC_oj7jscss2qe&index=3

Comment with exactly the same problem https://github.com/ros2/rviz/issues/929#issuecomment-1678262970