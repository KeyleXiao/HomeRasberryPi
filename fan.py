#!/usr/bin/python2
# coding:utf8

# 自动风扇控制程序，使用wiringPi的gpio命令来操作GPIO

import os
from time import sleep
from RPi import GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
# 我用的gpio1对应的bcm是18，这里根据自己的接法修改
gpio.setup(16, gpio.OUT)
pwm = gpio.PWM(16, 100)
gpio.setwarnings(False)
pwm.ChangeDutyCycle(100)

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
