## Windows setup (tested on Windows 11) (Unverified and in testing)
Make sure internet connection is working.

### 1. Install: 
 - [VSCode](https://code.visualstudio.com/download)
 - [Xhost for Windows](https://sourceforge.net/projects/vcxsrv/)
 - [Docker Desktop for Windows together with WSL2](https://docs.docker.com/desktop/setup/install/windows-install/)
 - [Git for Windows](https://git-scm.com/downloads/win)

### 2. Install VScode plugins
In VSCode install extension [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) and [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack). 

### 3. Clone this repo and build the container
 - You can clone the repo through GIT UI or VSCode.
 - Then open this repo in VSCode and do `F1 -> Rebuild and Reopen Container -> WINDOWS ROS 2 Development Container`.
 - After a couple of minutes VSCode should be remotely connected to the ROS2 container. It downloads ~5GB of data so if this step takes too long, check internet connection.
 
### 4. Start Xhost and connect to the container
 - Start XLaunch from Windows launcher. In `Display settings` set `Display number` to `0`. Leave everything else to default.
 - You can connect to the container in 2 ways:
    
    a) Connect to the container by entering into Windows comandline: `docker exec -it vscoderos2workshop /bin/bash`.
    
    b) In VSCode open a terminal by pressing a + icon. It should automatically connect to the container.

 - Once inside the container execute command `rviz2`. If a window of Rviz opens, that means the setup was successful.


## Used resources when doing this tutorial (might be useful if problems occur)
 - Installing xhost https://stackoverflow.com/questions/44429394/x11-forwarding-of-a-gui-app-running-in-docker

 - Useful video for setting up Docker, ROS on Windows: https://www.youtube.com/watch?v=qWuudNxFGOQ

 - Some other common problems: https://docs.ros.org/en/jazzy/How-To-Guides/Installation-Troubleshooting.html#windows

 - Great video tutorials: https://www.youtube.com/watch?v=RbP5cARP-SM&list=PLunhqkrRNRhaqt0UfFxxC_oj7jscss2qe&index=3

 - Comment with exactly the problem I had: https://github.com/ros2/rviz/issues/929#issuecomment-1678262970