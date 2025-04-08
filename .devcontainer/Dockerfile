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
ARG CODIUM_RELEASE=1.87.1.24068
RUN wget https://github.com/VSCodium/vscodium/releases/download/${CODIUM_RELEASE}/codium_${CODIUM_RELEASE}_amd64.deb \
    && apt-get update \
    && apt-get -f -y install ./codium_${CODIUM_RELEASE}_amd64.deb \
    && rm --force --recursive /var/lib/apt/lists/*
RUN echo 'alias codium="codium --no-sandbox --user-data-dir /opt/vscodium/home"' >> /root/.bashrc

# Force color prompt for sudo user and set username color to orange
RUN sed -i -e 's/#force_color_prompt=yes/force_color_prompt=yes/g' /root/.bashrc
RUN echo "PS1='${debian_chroot:+($debian_chroot)}\[\033[38;5;214m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '" >> /root/.bashrc

# On every login, cd into home directory
RUN echo 'cd' >> /root/.bashrc

ENV SHELL=/bin/bash

CMD ["/bin/bash"]