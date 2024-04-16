# ros2workshop

# Running with VSCode
In VSCode install extension [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) and [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack). Then open this repo in VSCode and do `F1 -> Rebuild and Reopen Container`.

# Run ROS2 Manually with Docker (only tested on Ubuntu 22.04)

Make sure you have Docker installed (see resources).

    cd .devcontainer/
    ./manualrun.sh

You should automatically create and connect to a Docker container with ROS2.

If a container already exists OR another terminal needs to be opened in same container, run:

    docker exec  -it ros2workshop /bin/bash


# Things covered
**Workshop 1**
 - [Configuring the environment](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Configuring-ROS2-Environment.html)
 - [Turtlesim](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim.html)
 - [Understanding Nodes, Topics, Services, Parameters, RQT](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools.html)


# Resources
Docker install https://docs.docker.com/engine/install/

ROS2 on Docker https://docs.ros.org/en/humble/How-To-Guides/Run-2-nodes-in-single-or-separate-docker-containers.html


# Additional debug info

## Experiencing issues opening visual programs on Docker container?
Solution: run `xhost +local:docker` on host before running container (tested on Ubuntu18.04). Full conversation about this [here](https://github.com/JanezCim/ros2workshop/issues/1).