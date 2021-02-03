# LIBRO（图书管理机器人）
## 项目简介
LIBRO is short for LIBrary management RObot

## 文件说明
仓库中的libro_model文件夹包括主要项目工程文件，CHANGELOG文件记录开发中信息，其他文件一般为项目所引用的功能包。

libro_model文件夹结构说明：

|文件（夹）名|功能描述|
|:-----|:----:|
|launch|用于执行如slam、navigation等功能的启动文件|
|config|各功能模块的参数配置文件|
|maps|通过slam所得到的环境地图文件|
|rviz|rviz环境配置文件|
|scripts|ros python程序文件|
|urdf|机器人模型及仿真文件|
|worlds|环境模型文件|
|CMakeLists.txt| ROS功能包编译配置文件 |
|package.xml|ROS功能包编译配置文件|

## 安装依赖
手动安装依赖包：sudo apt install ros-melodic-(包名)

|包名（主要）|功能描述|
|:-----|:----:|
|gmapping|基于粒子滤波的SLAM算法|
|amcl|自适应蒙特卡洛定位算法，采用粒子滤波来跟踪已知地图中机器人位姿|
|move_base|提供ROS导航的整体框架，包括路径规划、代价地图、行为恢复等模块|
|explore_lite|提供基于greedy frontier-based的地图搜索算法|

## 使用方法
- SLAM建图：roslaunch libro_exec manual_slam.launch 
- 键盘控制：roslaunch libro_controller libro_teleop.launch 
- 导航功能：roslaunch libro_exec navigation.launch 
- 自动搜索slam建图：roslaunch libro_exec auto_slam.launch 
- 保存地图 :
  进入到libro_map文件夹下的map文件夹，输入
  sh save_map.sh
