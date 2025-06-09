#!/bin/bash

sudo apt update
sudo rosdep install --from-paths src --ignore-src -y
sudo chown -R $(whoami) /root/ros2workshop_ws