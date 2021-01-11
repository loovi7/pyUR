import socket
import struct
import math
import re, time
import numpy as np

HOST = "192.168.30.16"  # The remote host
PORT = 30003  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
z = 1


def main():

    dic = {'MessageSize': 'i', 'Time': 'd', 'q target': '6d', 'qd target': '6d', 'qdd target': '6d', 'I target': '6d',
           'M target': '6d', 'q actual': '6d', 'qd actual': '6d', 'I actual': '6d', 'I control': '6d',
           'Tool vector actual': '6d', 'TCP speed actual': '6d', 'TCP force': '6d', 'Tool vector target': '6d',
           'TCP speed target': '6d', 'Digital input bits': 'd', 'Motor temperatures': '6d', 'Controller Timer': 'd',
           'Test value': 'd', 'Robot Mode': 'd', 'Joint Modes': '6d', 'Safety Mode': 'd', 'empty1': '6d',
           'Tool Accelerometer values': '3d',
           'empty2': '6d', 'Speed scaling': 'd', 'Linear momentum norm': 'd', 'SoftwareOnly': 'd', 'softwareOnly2': 'd',
           'V main': 'd',
           'V robot': 'd', 'I robot': 'd', 'V actual': '6d', 'Digital outputs': 'd', 'Program state': 'd',
           'Elbow position': '3d', 'Elbow velocity': '3d', 'Safety Status': 'd'}

    data = s.recv(1116)

    names = []
    ii = range(len(dic))
    for key, i in zip(dic, ii):
        fmtsize = struct.calcsize(dic[key])
        data1, data = data[0:fmtsize], data[fmtsize:]
        fmt = "!" + dic[key]
        names.append(struct.unpack(fmt, data1))
        dic[key] = dic[key], struct.unpack(fmt, data1)
    # a = dic['q actual']
    # print(a[1])

    print("第{0:}次解析".format(z))
    for key, value in dic.items():
        print(key, end=": ")
        print(value[1])
    print()


if __name__ == '__main__':

    step = 1

    while z <= step:
        main()
        z = z + 1
        time.sleep(1)


