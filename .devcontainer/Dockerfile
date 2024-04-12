FROM osrf/ros:humble-desktop-full

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3-pip

# Install Gazebo Harmonic (by defauld by invoking install ros_humble_ros_gz, Gazebo Fortress is going to get installed - which has troubles with package naming - Ignition)
# RUN apt-get install lsb-release wget gnupg -y
# RUN wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
# RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
# RUN apt-get update -y
# RUN apt-get install gz-harmonic -y

# Installations for workspace manipulation
RUN apt-get install python3-vcstool python3-colcon-common-extensions git wget -y

# Ease of use stuff
RUN apt-get install -y nano bash-completion
RUN echo 'source /opt/ros/humble/setup.bash' >> /root/.bashrc
RUN echo 'alias s="source install/local_setup.bash"' >> /root/.bashrc
# Colcon builds with symlik (so recompile is not needed for python or config changes) and for release
RUN echo 'alias c="colcon build --symlink-install --cmake-args=-DCMAKE_BUILD_TYPE=Release"' >> /root/.bashrc

# Force color prompt for sudo user
RUN sed -i -e 's/#force_color_prompt=yes/force_color_prompt=yes/g' /root/.bashrc

ENV SHELL /bin/bash

CMD ["/bin/bash"]