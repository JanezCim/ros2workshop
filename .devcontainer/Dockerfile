FROM osrf/ros:jazzy-desktop-full

RUN apt-get update -y
RUN apt-get install -y python3-pip

# Installations for workspace manipulation
RUN apt-get install python3-vcstool python3-colcon-common-extensions git wget -y

# Ssh client allows git management from inside container
RUN apt-get install openssh-client -y

# Ease of use stuff
RUN apt-get install -y nano bash-completion
RUN echo 'source /opt/ros/jazzy/setup.bash' >> /root/.bashrc
RUN echo 'alias s="source install/local_setup.bash"' >> /root/.bashrc
# Colcon builds with symlik (so recompile is not needed for python or config changes) and for release
RUN echo 'alias c="colcon build --symlink-install --cmake-args=-DCMAKE_BUILD_TYPE=Release"' >> /root/.bashrc
# Suppress colcon specific warning for python package compilation as suggested in https://robotics.stackexchange.com/questions/24230/setuptoolsdeprecationwarning-in-ros2-humble
RUN echo 'PYTHONWARNINGS="ignore:easy_install command is deprecated,ignore:setup.py install is deprecated"; export PYTHONWARNINGS' >> /root/.bashrc
# Select which turtlebot to spawn, see other options in https://github.com/ROBOTIS-GIT/turtlebot3_simulations/tree/master/turtlebot3_gazebo/models
ENV TURTLEBOT3_MODEL='burger'

# Additional ROS stuff
RUN apt-get install ros-jazzy-rqt-tf-tree -y

# VSCodium 
ARG CODIUM_REL=1.99.02289
RUN wget https://github.com/VSCodium/vscodium/releases/download/${CODIUM_REL}/codium_${CODIUM_REL}_amd64.deb
RUN apt-get update
RUN apt-get -f -y install ./codium_${CODIUM_REL}_amd64.deb
RUN rm --force --recursive /var/lib/apt/lists/*
RUN echo 'alias codium="codium --no-sandbox --user-data-dir /opt/vscodium/home"' >> /root/.bashrc

# VSCode
RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
RUN sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
RUN echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" |sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null
RUN rm -f packages.microsoft.gpg
RUN sudo apt install apt-transport-https -y
RUN sudo apt update -y
RUN sudo apt install code -y
RUN code --no-sandbox --user-data-dir /opt/vscode/home --install-extension jaehyunshim.vscode-ros2
RUN code --no-sandbox --user-data-dir /opt/vscode/home --install-extension ms-python.python
RUN echo 'alias code="code --no-sandbox --user-data-dir /opt/vscode/home"' >> /root/.bashrc

# Force color prompt for sudo user and set username color to orange
RUN sed -i -e 's/#force_color_prompt=yes/force_color_prompt=yes/g' /root/.bashrc
RUN echo "PS1='${debian_chroot:+($debian_chroot)}\[\033[38;5;214m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '" >> /root/.bashrc

# On every login, cd into home directory
RUN echo 'cd' >> /root/.bashrc

ENV SHELL=/bin/bash

CMD ["/bin/bash"]