#!/usr/bin/python2.7
# coding:utf-8
__author__ = "Haddy Yang"
__date__ = "2016-06-30"
__blog__ = "http://yshblog.com"

from RPi import GPIO as gpio  # 注意RPi中的i是小写的
import time


def get_cpu_temperature():
	return float(os.popen('vcgencmd measure_temp').readline().replace("temp=", "").replace("'C\n", ""))



# 监控温度，控制风扇开关
def check_temp(port):
	# BOARD编号方式，基于插座引脚编号
	gpio.setmode(gpio.BOARD)

	# 设置哪个引脚为输出模式
	gpio.setup(port, gpio.OUT)

	# 标记风扇开关状态
	is_close = True

	try:
		while True:
			temp = get_cpu_temperature()
		if is_close:
			# 温度大于等于50时，打开引脚，输出电信号
			if temp >= 50:
				gpio.output(port, 1)
				is_close = False
		else:
			# 温度降低到45极其以下时，关闭引脚
			if temp <= 45:
				gpio.output(port, 0)
				is_close = True

		# 休眠1秒
		time.sleep(1)
		print("temp:%s, fan is close:%s" % (temp, is_close))

if __name__ == '__main__':
	port = 16
	check_temp(port)