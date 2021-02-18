# LIBRO（图书管理机器人）
## 项目简介
LIBRO is short for LIBrary management RObot

## 文件说明
仓库中的多个功能包都是在 Libro 机器人运行时必不可少的，以下是各个 package 的功能介绍，

|功能包名|功能描述|
|:-----|:----:|
|libro_exec|用于执行如slam、navigation等功能的启动文件|
|libro_controller|通过键盘发送命令控制机器人运动|
|libro_web|基于web的图形化机器人控制界面|
|libro_move_base|为navigation和explore提供move_base导航功能|
|libro_map|通过 map_server 提供地图服务|
|libro_amcl|为 navigation 提供定位服务|
|libro_explore|提供基于explore_lite的自动搜索slam算法|
|libro_model|机器人模型及仿真文件|
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
|rosbridge-suite|提供基于JSON与ROS交互的协议和实现，在web控制器中使用|
|ar_track_alvar|生成、识别和跟踪AR标签，用于相机标定、机器人定位、增强现实等应用场合|

## 使用方法
- SLAM建图：roslaunch libro_exec manual_slam.launch 
- 键盘控制：roslaunch libro_controller libro_teleop.launch 
- 导航功能：roslaunch libro_exec navigation.launch 
- 自动搜索slam建图：roslaunch libro_exec auto_slam.launch 
- 设定导航目标：
   - rosrun libro_controller libro_setgoal.py x y
   - 此处的x,y值为要设置的目标点的坐标
- 保存地图：
   - 进入到libro_map文件夹下的map文件夹，输入 sh save_map.sh
- web控制器：
   - roslaunch rosbridge_server rosbridge_websocket.launch
	 - 运行 libro_web pkg src文件夹下的index.html文件
