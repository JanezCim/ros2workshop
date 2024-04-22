Lets create a workspace

	cd ~
	mkdir ros2workshop_ws
	cd ~/ros2workshop_ws/
	mkdir src


Lets create a package (Python)

	cd ~/ros2workshop_ws/src
	ros2 pkg create --build-type ament_python first_package

Lets build the workspace

	cd ~/ros2workshop_ws/
	colcon build

Lets source the workspace and try to run the package

	cd ~/ros2workshop_ws/
	source install/local_setup.bash
	ros2 run first_package 

Why is there an error? Because no node was created inside first_package

Lets create a second package with a python node and run it

	cd ~/ros2workshop_ws/src
	ros2 pkg create --build-type ament_python --node-name second_node second_package
	cd ~/ros2workshop_ws/
	colcon build
	ros2 run second_package second_node

Lets add a third_node into second_package

	cd ~/ros2workshop_ws/src/second_package/second_package/
	cp second_node.py third_node.py
	nano ~/ros2workshop_ws/src/second_package/setup.py 

Add stuff so it looks like

```
entry_points={
'console_scripts': [
	'second_node = second_package.second_node:main',
	'third_node = second_package.third_node:main'
],
```

then compile and run.

Tip: how to make it so you don't have to recompile on every Python change

	colcon build --symlink-install

How do we create a package with c++ node?

	ros2 pkg create --build-type ament_cmake --node-name cpp_test_node cpp_test_package	
	nano ~/ros2workshop_ws/src/cpp_test_package/CMakeLists.txt

Lets add a dependency into package.xml

	nano ~/ros2workshop_ws/src/second_package/package.xml

insert

	<depend>first_package</depend>

and then

	cd ~/ros2workshop_ws/
	rosdep install -i --from-path src --rosdistro $ROS_DISTRO -y

replace `first_package` with `fake_package` and `realsense2_camera` and see what happens. Compare with `apt install`.

Lets overlay turtlesim package (example from [official docs](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html))

	cd ~/ros2workshop_ws/src/
	git clone https://github.com/ros/ros_tutorials.git -b humble
	nano ~/ros2workshop_ws/src/ros_tutorials/turtlesim/src/turtle_frame.cpp

find and replace with 

	setWindowTitle("WorkshopTurtleSim");

then

	colcon build
	source install/setup.bash
	ros2 run turtlesim turtlesim_node

To compare with underlay, open new terminal and

	ros2 run turtlesim turtlesim_node
