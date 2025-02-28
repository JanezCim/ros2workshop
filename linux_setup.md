# Linux setup (tested on Ubuntu 24.04)
Make sure internet connection is working.

### 1. Install:
 - [VSCode](https://code.visualstudio.com/download)
 - [Docker for Linux](docker_install.md)

### 2. Install VScode plugins
In VSCode install extension [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) and [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack). 

### 3. Clone this repo and build the container
 - Clone this repo into the selected directory in Terminal by executing:

    git clone https://github.com/JanezCim/ros2workshop.git

 - Then open the cloned repo with VSCode and do `F1 -> Rebuild and Reopen Container -> LINUX ROS 2 Development Container`.

After a couple of minutes VSCode should be remotely connected to the ROS2 container.

### 4. Start Xhost and connect to the container
 - Open a Terminal and first enter

        xhost +local:docker

 - Then connect to the container in one of two ways:

    a) In Terminal execute 
    
        docker exec -it vscoderos2workshop /bin/bash

    b) In VSCode open a terminal by pressing a + icon. It should automatically connect to the container.

 - Once inside the container execute command `rviz2`. If a window of Rviz openes, that means the setup was successful.