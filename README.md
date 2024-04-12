# ros2workshop

# Run ROS2 Manually with Docker (only tested on Ubuntu 22.04)

Make sure you have Docker installed (see resources).

    cd .devcontainer/
    ./manualrun.sh

You should automatically create and connect to a Docker container with ROS2.

If a Docker already exists OR another terminal needs to be opened in same container, run:

    docker exec  -it ros2workshop /bin/bash


# Things covered
**Workshop 1**
 - [Configuring the environment](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Configuring-ROS2-Environment.html)
 - [Turtlesim](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim.html)
 - [Understanding Nodes, Topics, Services, Parameters, RQT](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools.html)


# Resources
Docker install https://docs.docker.com/engine/install/

ROS2 on Docker https://docs.ros.org/en/humble/How-To-Guides/Run-2-nodes-in-single-or-separate-docker-containers.html