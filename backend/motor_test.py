import RPi.GPIO as GPIO    
from time import sleep
from RpiMotorLib import RpiMotorLib

GPIO.setmode(GPIO.BCM)

GPIO_pins = (14, 15, 18)
vertical_direction = 20
vertical_step = 21

horizontal_direction = 19
horizontal_step = 26

heat_pin = 13 

GPIO.setup(heat_pin, GPIO.OUT)
GPIO.output(heat_pin, GPIO.LOW)

motor_vertical = RpiMotorLib.A4988Nema(vertical_direction, vertical_step, GPIO_pins, "A4988")

motor_horizontal = RpiMotorLib.A4988Nema(horizontal_direction, horizontal_step, GPIO_pins, "A4988")

slider = 5

print("motor turn")
motor_vertical.motor_go(True, "Full" , 600,int(slider)*.0004, False, .05)

motor_horizontal.motor_go(True, "Full" , 600,int(slider)*.0004, False, .05)
print("Done")

GPIO.output(heat_pin, GPIO.HIGH)
sleep(5)

GPIO.output(heat_pin, GPIO.LOW)
print("program ends")
