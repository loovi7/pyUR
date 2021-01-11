# -*- coding: utf-8 -*-
# @Time    : 2021/1/9 16:22
# @Author  : luowei
# @FileName: UR_Commands.py
# @Csdn_blogs ：https://blog.csdn.net/luodaxia_ttt

import socket
from time import sleep

target_ip = ("192.168.30.16", 30003)  # 机械臂IP & 端口号
sk = socket.socket()  # 创建套接字
sk.connect(target_ip)  # 连接


def movej_list(q, a, v):
    """
    移动机械臂至指定关节角
    :param v: 速度
    :param a: 加速度
    :param q: 目标角度list
    """
    data = "def test():\n movej(["
    for i in range(len(q) - 1):
        data += str(q[i])
        data += ","
    data += str(q[5])
    data += "],a="
    data += str(a)
    data += ",v="
    data += str(v)
    data += ")\nend\n"
    sk.send(data.encode('utf-8'))


def movej_enum(q1, q2, q3, q4, q5, q6, a, v):
    """
    移动机械臂至指定关节角
    :param q1 q2 q3 q4 q5 q6: 角度列举
    :param a: 加速度
    :param v: 速度
    """
    data = "def test():\n movej(["
    data += str(q1)
    data += ","
    data += str(q2)
    data += ","
    data += str(q3)
    data += ","
    data += str(q4)
    data += ","
    data += str(q5)
    data += ","
    data += str(q6)
    data += "],a="
    data += str(a)
    data += ",v="
    data += str(v)
    data += ")\nend\n"
    print(data)
    sk.send(data.encode('utf-8'))


def speedj_list(qd, a, t):
    """
    控制六关节的速度
    :param qd: 目标速度列表
    :param a: 加速度
    :param t: 持续时间
    """
    data = "def test():\n speedj(["
    for i in range(len(qd) - 1):
        data += str(qd[i])
        data += ","
    data += str(qd[5])
    data += "],a="
    data += str(a)
    data += ",t="
    data += str(t)
    data += ")\nend\n"
    sk.send(data.encode('utf-8'))


def speedj_enum(qd1, qd2, qd3, qd4, qd5, qd6, a, t):
    """
    控制六关节的速度
    :param qd1 ~ qd6: 每个关节角的目标速度
    :param a:
    :param t:
    """
    data = "def test():\n speedj(["
    data += str(qd1)
    data += ","
    data += str(qd2)
    data += ","
    data += str(qd3)
    data += ","
    data += str(qd4)
    data += ","
    data += str(qd5)
    data += ","
    data += str(qd6)
    data += "],a="
    data += str(a)
    data += ",t="
    data += str(t)
    data += ")\nend\n"
    print(data)
    sk.send(data.encode('utf-8'))


def send_script(urscript):
    """
    直接发送ur脚本给机械臂
    @param urscript:写好的urscript文件路径
    """
    text = open(urscript)
    text = text.read()
    sk.send(text.encode('utf-8'))


def exit_control():
    sk.close()
