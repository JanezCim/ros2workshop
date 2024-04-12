#! /bin/bash
tag='workshopcontainer'

docker build - < Dockerfile --tag $tag

xauth=/tmp/docker.xauth
if [ ! -f "$xauth" ]; then
  touch $xauth
  echo "$xauth is created"
fi

docker run \
  --net=host \
  --tmpfs /tmp \
  --device /dev/dri/ \
  --name ros2workshop \
  -e ROS_DISTRO=humble -e DISPLAY=$DISPLAY \
  -e QT_X11_NO_MITSHM=1 \
  -v /tmp/.X11-unix/:/tmp/.X11-unix:rw \
  -e XAUTHORITY=$xauth \
  -e "TERM=xterm-256color" \
  -it $tag /bin/bash \
