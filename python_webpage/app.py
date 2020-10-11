import RPi.GPIO as GPIO    
from time import sleep
from RpiMotorLib import RpiMotorLib

import Adafruit_DHT
sensor=Adafruit_DHT.DHT11
PIN_temp = 4

import threading

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
    while(not GPIO.input(PIN_shoe_touch)):
        print("Please take out your shoes!",end='\r')
        sleep(1)

    print("Initialization done")
    
def getTempHumid():

    global machine_status
    
    humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN_temp)
    if humidity is not None and temperature is not None:
            print('Temperature = {0:0.1f}*C  Humidity = {1:0.1f}%'.format(temperature, humidity))
    else:
            print('Failed to get reading. Try again!')


    
    machine_status["temperature"] = temperature
    machine_status["humidity"] = humidity
    return (temperature,humidity)


def operate_machine():
    print("Machine operation Starts")
    global machine_status
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
            while(GPIO.input(PIN_shoe_touch)):
                print("Waiting for shoes",end='\r')
                machine_status["shoes"] = False
                sleep(1)
            print("Shoes detected")
            machine_status["status"] = "shoes_detected"
            machine_status["shoes"] = True

            sleep(2)
            if not GPIO.input(PIN_shoe_touch):
                con = False
            else:
                con = True
                machine_status["status"] = "idle"

        # move plate to state 1
        # TODO
        print("Moving plate to state 1")
        motor_horizontal.motor_go(True,"Full",1000,0.006,False,0.95)
        print("[Done] Moving plate to state 1")


        # record atmosphere humidity
        print("Getting atm humidity")
        getTempHumid()
        atm_humidity = machine_status["humidity"]
        print("Atm Humidity {}".format(atm_humidity))

        # shift down the shell
        # TODO
        machine_status["status"] = "shelldown"
        print("Shell going down")
        motor_vertical.motor_go(False,"Full",15000,0.0012,False,0.95)
        print("[Done] Shell going down")
       
       
       
       
       
       
        # detect if need dry
        #machine_status["status"] = "pre_check"
        #machine_status["plate_state"] = 1
        #print("Prechecking shoes")
        #print("[Done] Prechecking shoes")
        
        

        need_dry = True

        GPIO.output(PIN_heat, GPIO.HIGH)
        print("On heat")
        machine_status["status"] = "heating"
        while(need_dry):
            
            sleep(5)
            getTempHumid()
            if machine_status["temperature"] > 60:
                # overheat
                GPIO.output(PIN_heat,GPIO.LOW)
            else:
                GPIO.output(PIN_heat,GPIO.HIGH)
            
            if machine_status["humidity"] <= atm_humidity + 2:
                # done drying process
                need_dry = False

        print("off heat")
        GPIO.output(PIN_heat, GPIO.LOW)

        # shift up the shell
        # TODO
        machine_status["status"] = "shell_up"
        print("shell going up")
        motor_vertical.motor_go(True,"Full",15000,0.004,False,0.95)
        print("[Done] shell going up")


        # move plate to state 2
        print("moving to state 2")
        machine_status["status"] = "done"
        machine_status["state"] = 2
        motor_horizontal.motor_go(True,"Full",1000,0.004,False,0.95)
        print("[Done] moving to state 2")

        while(not GPIO.input(PIN_shoe_touch)):
            print("Waiting for shoes to release",end='\r')
            machine_status["shoes"] = True
            sleep(1)
        print("Shoes release")
        machine_status["shoes"] = False
        sleep(1)

        # move the plate back to state 0
        print("Moving plate back to state 0")
        motor_horizontal.motor_go(False,"Full",2000,0.004,False,0.95)
        print("[Done] Moving plate back to state 0")
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

@app.route('/index.css')
def get_indexcss():
    return send_file("src/index.css")

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
    t = threading.Thread(target = operate_machine)
    t.start()
    print("server start") 
    app.run(host= '0.0.0.0')
    print("server end")
    t.join()
    print("process ends")
    
