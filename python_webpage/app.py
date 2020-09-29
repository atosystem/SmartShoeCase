import RPi.GPIO as GPIO    
from time import sleep
from RpiMotorLib import RpiMotorLib

# Hardware settings
GPIO.setmode(GPIO.BCM)

GPIO_pins = (14, 15, 18)
PIN_vertical_direction = 20
PIN_vertical_step = 21

PIN_horizontal_direction = 19
PIN_horizontal_step = 26

PIN_heat = 13 

GPIO.setup(PIN_heat, GPIO.OUT)
GPIO.output(PIN_heat, GPIO.LOW)

motor_vertical = RpiMotorLib.A4988Nema(PIN_vertical_direction, PIN_vertical_step, GPIO_pins, "A4988")

motor_horizontal = RpiMotorLib.A4988Nema(PIN_horizontal_direction, PIN_horizontal_step, GPIO_pins, "A4988")

slider = 5

from flask import Flask , send_file
app = Flask(__name__)


@app.route('/')
def get_index():
    return send_file("src/index.html")


@app.route('/jquery-3.5.1.min.js')

def get_jquery():
    return send_file("src/jquery-3.5.1.min.js")


@app.route('/index.js')
def get_indexjs():
    return send_file("src/index.js")


@app.route('/getStatus')
def get_getStatus():
    return {"pos" : 2}

@app.route('/turn1')
def get_turn1():
    motor_vertical.motor_go(True, "Full" , 600,int(slider)*.0004, False, .05)
    return "ok"

@app.route('/turn2')
def get_turn2():
    motor_horizontal.motor_go(True, "Full" , 600,int(slider)*.0004, False, .05)
    return "ok"

@app.route('/heaton')
def get_heaton():
    GPIO.output(PIN_heat, GPIO.HIGH)
    return "ok"

@app.route('/heatoff')
def get_heatoff():
    GPIO.output(PIN_heat, GPIO.LOW)
    return "ok"

    # return "Hello World!"




if __name__ == '__main__':
    app.run(host= '0.0.0.0')