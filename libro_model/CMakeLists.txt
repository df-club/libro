cmake_minimum_required(VERSION 2.8.3)
project(libro_model)
find_package(catkin REQUIRED COMPONENTS
	roscpp
	rospy
	std_msgs
	message_generation
	controller_manager
	gazebo_ros
	move_base
	map_server
	amcl
	gmapping
	dwa_local_planner
)

catkin_package(
   CATKIN_DEPENDS urdf xacro
)