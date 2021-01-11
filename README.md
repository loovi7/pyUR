# pyUR
python API for Universal Robot Control

# WHAT
基于python编写windows平台上控制UR机械臂（CB系列：UR3 UR5 UR10，e系列：UR16e等）的常用方法，包括movej，speedj等。
windows上控制机械臂运动的基本方法是**发送URScript**。
# WHY
+ ROS有点难。（但是学会了真的很有用）
+ UR主打协作，即应用层面上的研发，有完整、友好的用户接口，为啥不用呢？
# HOW
能跑python脚本的软件就行。
+ UR_Commands.py: 将控制指令重写为函数，方便直接调用
+ send_demo.py: 调用UR_Commands.py中的函数
+ recv_port_30003: 接收30003端口收到的数据包，并解析。UR机械臂收发的数据包协议由搭载的系统版本决定，当前UR16e版本为5.5，数据包长度1116。
+ test.urscript: 用urscript语法编写的脚本，用于UR_Commands.py中的函数send_script()。

***持续更新***
