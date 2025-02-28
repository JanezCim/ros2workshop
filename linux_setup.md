# Linux setup (tested on Ubuntu 24.04)
Make sure internet connection is working.

### 1. Install:
 - [VSCode](https://code.visualstudio.com/download)
 - [Docker for Linux](docker_install.md)
 - It is assumed that Git and xhost are already pre-installed (usually they are on Linux)

### 2. Install VScode plugins
In VSCode install extension [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) and [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack). 

### 3. Clone this repo and build the container
 - Clone this repo into the selected directory in Terminal by executing:

    git clone https://github.com/JanezCim/ros2workshop.git

 - Then open the cloned repo with VSCode and do `F1 -> Rebuild and Reopen Container -> LINUX ROS 2 Development Container`.

After a couple of minutes VSCode should be remotely connected to the ROS2 container. It downloads ~5GB of data so if this step takes too long, check internet connection.

### 4. Start Xhost and connect to the container
 - Open a Terminal and first enter

        xhost +local:docker

 - Then connect to the container in one of two ways:

    a) In Terminal execute 
    
        docker exec -it vscoderos2workshop /bin/bash

    b) In VSCode open a terminal by pressing a + icon. It should automatically connect to the container.

 - Once inside the container execute command `rviz2`. If a window of Rviz opens, that means the setup was successful.


## Used resources when doing this tutorial (might be useful if problems occur)

Docker install https://docs.docker.com/engine/install/

ROS2 on Docker https://docs.ros.org/en/jazzy/How-To-Guides/Run-2-nodes-in-single-or-separate-docker-containers.html


# Additional debug info

## Experiencing issues opening visual programs on Docker container?
Solution: run `xhost +local:docker` on host before running container (tested on Ubuntu18.04). Full conversation about this [here](https://github.com/JanezCim/ros2workshop/issues/1).

