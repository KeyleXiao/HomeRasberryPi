#!/usr/bin/python2
# coding:utf8

# 自动风扇控制程序，使用wiringPi的gpio命令来操作GPIO

import commands, time, os


def get_cpu_temperature():
	return float(os.popen('vcgencmd measure_temp').readline().replace("temp=", "").replace("'C\n", ""))


# 控制风扇的GPIO
FAN_GPIO = 15

commands.getoutput('sudo gpio mode ' + str(FAN_GPIO) + ' output')

while True:
	# tmpFile = open('/sys/class/thermal/thermal_zone0/temp')
	#
	# cpu_temp_raw = tmpFile.read()
	# tmpFile.close()
	# cpu_temp = round(float(cpu_temp_raw) / 1000, 1)

	get_cpu_temperature()

	# 如果温度大于45`C，就启动风扇
	# if cpu_temp & gt;=45.0:
	# 	commands.getoutput('sudo gpio write ' + str(FAN_GPIO) + ' 0')
	#
	# # 如果温度小于42`C，就关闭风扇
	# if cpu_temp & lt;42.0:
	# 	commands.getoutput('sudo gpio write ' + str(FAN_GPIO) + ' 1')

	time.sleep(5)
