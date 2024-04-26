Development with VSCode and ROS on Docker

Make sure you have [installed Docker](docker_install.md), then

	git clone https://github.com/JanezCim/ros2workshop.git

In VSCode install extension [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) and [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack). Then open this repo in VSCode and do 

	F1 -> Rebuild and Reopen Container

---

**Lets create a minimal python publisher**

**Task:** Create a python package without a node. 

Download a minimal example node and add it to package.

	wget https://raw.githubusercontent.com/ros2/examples/humble/rclpy/topics/minimal_publisher/examples_rclpy_minimal_publisher/publisher_member_function.py

Then compile the workspace and run the node

---

Task: how do we write a node that re-publishes the message it receives from a topic?

Hint to publish string from terminal:

	ros2 topic pub /topic std_msgs/msg/String "{data: 'bla'}"


---

Task: How to change the code to re-publish a message of type `Int8`? What about [some other interface](https://github.com/ros2/common_interfaces)?

---
