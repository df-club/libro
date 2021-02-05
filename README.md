# LIBRO（图书管理机器人）
## 项目简介
LIBRO is short for LIBrary management RObot

## 文件说明
仓库中的多个功能包都是在 Libro 机器人运行时必不可少的，以下是各个 package 的功能介绍，

|功能包名|功能描述|
|:-----|:----:|
|libro_exec|用于执行如slam、navigation等功能的启动文件|
|libro_map|通过 map_server 提供地图服务|
|lirbo_amcl|为 navigation 提供定位服务|
|libro_move_base|为 navigation 和 explore 提供 move_base 导航功能|
|libro_model|机器人模型及仿真文件|
|libro_controller|键盘控制文件|
|libro_gmapping|提供 gmapping 扫描地图功能|
|libro_sim|提供在gazebo中libro仿真的环境文件|
|CMakeLists.txt|ROS功能包编译配置文件|
|package.xml|ROS功能包编译配置文件|

## 安装依赖
手动安装依赖包：sudo apt install ros-melodic-(包名)

|包名（主要）|功能描述|
|:-----|:----:|
|gmapping|基于粒子滤波的SLAM算法|
|navigation|用于实现导航功能的一系列包的合集|
|- map_server|用于保存和发布map信息|
|- amcl|自适应蒙特卡洛定位算法，采用粒子滤波来跟踪已知地图中机器人位姿|
|- move_base|提供ROS导航的基础框架，用于连接navigation中其他功能包|
|- costmap2d|在静态地图的基础上添加用于导航规划的局部和全局代价信息|
|- XXX_planner|不同的路径规划算法，用于局部和全局的路径规划|
|- recovery_behaviors|用于机器人在导航过程中遇到问题时的行为恢复|
|explore_lite|提供基于greedy frontier-based的地图搜索算法|
|robot_pose_ekf|用于融合里程计，惯性测量单元和视觉里程计的传感器输出，从而减少测量中的总体误差|

## 使用方法
- SLAM建图：roslaunch libro_exec manual_slam.launch 
- 键盘控制：roslaunch libro_controller libro_teleop.launch 
- 导航功能：roslaunch libro_exec navigation.launch 
- 自动搜索slam建图：roslaunch libro_exec auto_slam.launch 
- 保存地图 :
  进入到libro_map文件夹下的map文件夹，输入
  sh save_map.sh
