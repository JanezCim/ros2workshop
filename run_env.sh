#! /bin/bash
tag='ros2workshopimage'

xhost +local:docker

xauth=/tmp/docker.xauth
if [ ! -f "$xauth" ]; then
  touch $xauth
  echo "$xauth is created"
fi

container_name="ros2workshopcontainer"

# Check if the container exists
if docker inspect "$container_name" > /dev/null 2>&1; then
    echo "The container $container_name exists."
    
    # Check if the container is running
    if $(docker inspect -f '{{.State.Status}}' "$container_name" | grep -q "running"); then
        echo "The container $container_name is running, will exec into it."
        docker exec -it $container_name /bin/bash
    else
        echo "The container $container_name is not running, will start it."
        
        # Start the container if it is not running
        docker start "$container_name"
    fi
else
    echo "The container $container_name does not exist, will run it."
    
    # Docker build
    docker build - < .devcontainer/Dockerfile --tag $tag
    # Create and start the container if it does not exist
    docker run \
      -it --rm \
      --net=host \
      --tmpfs /tmp \
      --device /dev/dri/ \
      --name $container_name \
      -e ROS_DISTRO=jazzy \
      -e DISPLAY=$DISPLAY \
      -e QT_X11_NO_MITSHM=1 \
      -e XAUTHORITY=$xauth \
      -e "TERM=xterm-256color" \
      -e "ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST" \
      -e "ROS_DOMAIN_ID=42" \
      -v /tmp/.X11-unix/:/tmp/.X11-unix:rw \
      -v $(pwd):/root/ros2workshop_ws:rw \
      $tag /bin/bash
fi
