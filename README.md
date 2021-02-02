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

## 使用方法
- SLAM建图：roslaunch libro_model slam.launch
- 键盘控制：rosrun libro_model libro_teleop.py
- 导航功能：roslaunch libro_model navigation.launch
