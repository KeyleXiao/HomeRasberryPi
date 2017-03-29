#!/usr/bin/python2
# coding:utf8

# 自动风扇控制程序，使用wiringPi的gpio命令来操作GPIO

import time, os


def get_cpu_temperature():
	return float(os.popen('vcgencmd measure_temp').readline().replace("temp=", "").replace("'C\n", ""))


while True:
	get_cpu_temperature()
	time.sleep(5)
