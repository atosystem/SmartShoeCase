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
PIN_shoe_touch = 17


GPIO.setup(PIN_heat, GPIO.OUT)
GPIO.setup(PIN_shoe_touch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(PIN_heat, GPIO.LOW)


motor_vertical = RpiMotorLib.A4988Nema(PIN_vertical_direction, PIN_vertical_step, GPIO_pins, "A4988")

motor_horizontal = RpiMotorLib.A4988Nema(PIN_horizontal_direction, PIN_horizontal_step, GPIO_pins, "A4988")

slider = 5

machine_status={
    "status" : "idle",
    "plate_state" : 0,
    "plate_pos" : 0,
    "temperature" : -1,
    "humidity" : -1,
    "shoes" : False
}

def initialize_machine():
    print("Begin initialization")

    # reset heat plate position
    #TODO
    # print("Reseting heat plate position")

    # reset shoes plate position
    #TODO
    # print("Reseting shoes plate position")

    # make sure shoes plate is not occupied
    while(GPIO.input(PIN_shoe_touch)):
        print("Please take out your shoes!",end='\r')
        sleep(1)

    print("Initialization done")
    
def getTempHumid():
    # TODO
    machine_status["temperature"] = 24
    machine_status["humidity"] = 30
    return (24,30)

def operate_machine():
    while(True):
        machine_status={
            "status" : "idle",
            "plate_state" : 0,
            "plate_pos" : 0,
            "temperature" : -1,
            "humidity" : -1,
            "shoes" : False
        }
        
        con = True

        while(con):
            # wait for shoes
            while(not GPIO.input(PIN_shoe_touch)):
                print("Waiting for shoes",end='\r')
                sleep(1)
            print("Shoes detected")
            machine_status[status] = "shoes_detected"

            sleep(2)
            if GPIO.input(PIN_shoe_touch):
                con = False
            else:
                con = True
                machine_status[status] = "idle"

        # move plate to state 1
        # TODO
        print("Moving plate to state 1")
        print("[Done] Moving plate to state 1")

        # detect if need dry
        machine_status[status] = "pre_check"
        machine_status[plate_state] = 1
        print("Prechecking shoes")
        print("[Done] Prechecking shoes")

        getTempHumid()

        need_dry = True

        # shift down the shell
        # TODO
        machine_status[status] = "shelldown"
        print("Shell down")
        GPIO.output(PIN_heat, GPIO.HIGH)
        print("On heat")
        machine_status[status] = "heating"
        while(need_dry):
            
            sleep(7)
            getTempHumid()
            
            need_dry = False

        print("off heat")
        GPIO.output(PIN_heat, GPIO.LOW)

        # shift up the shell
        # TODO
        machine_status[status] = "shell_up"
        print("shell up")


        # move plate to state 2
        print("moving to state 2")
        machine_status[status] = "done"
        machine_status[state] = 2
        print("done")

        while(not GPIO.input(PIN_shoe_touch)):
            print("Waiting for shoes to release",end='\r')
            sleep(1)
        print("Shoes release")
        sleep(1)

        # move the plate back to state 0
        print("Moving plate back to state 0")
        sleep(1)










        




    





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

@app.route('/shoes.png')
def get_shoes_png():
    return send_file("src/shoes.png")


@app.route('/getStatus')
def get_getStatus():
    return machine_status


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
    initialize_machine()
    app.run(host= '0.0.0.0')
    print("server start")
    print("start machine")
    operate_machine()