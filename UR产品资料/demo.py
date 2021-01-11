# -*- encoding:utf-8 -*-
import socket
from time import sleep
import struct
target_ip =      ("168.254.12.100" ,30001)
host_ip = "168.254.2.3"
def zts():
	print("start")
	sk = socket.socket()
	sk.connect(target_ip)
	send_data1 = 'def test():\n speedl([0,0,0.1,0,0,0],2,1)\nend'
	print(send_data1)
	sk.send(send_data1.encode('utf8'))
	print("end")

zts()
