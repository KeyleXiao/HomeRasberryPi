import RPi.GPIO as GPIO
import time

GPIO_PIN = 24
count = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)

print("waiting 5 times...")

while count > 0:
    if(GPIO.input(GPIO_PIN) == 1):
        count = count - 1
        print("input high")
    time.sleep(0.1)

print("exit...")
GPIO.cleanup()