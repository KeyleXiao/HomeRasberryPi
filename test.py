#!/usr/bin/python2
# coding:utf8

import os
from time import sleep


def get_cpu_temperature():
	return float(os.popen('vcgencmd measure_temp').readline().replace("temp=", "").replace("'C\n", ""))


def get_cpu_temperature2():
	file = open("/sys/class/thermal/thermal_zone0/temp")
	temp = float(file.read()) / 1000
	file.close()
	return temp


while True:
	tp = get_cpu_temperature()
	print("%d < current cpu temperature" % tp)

	sleep(3)
