from approxeng.input.selectbinder import ControllerResource
from serial_communicator import SerialCommunicator, MotorCode
import requests

IP = "http://127.0.0.1:5000"

def registerControllerListener():
    while True:
        # Checks to make sure joystick is connected
        try: 
            with ControllerResource() as joystick:
                print('Found joystick!')
                while joystick.connected:
                    x = joystick.rx
                    y = joystick.ry

                    res = requests.post(IP, {
                        "controller_x": x,
                        "controller_y": y
                    })

                    
                    print(res.data())

        except IOError:
            print("Unable to find joystick!")
            sleep(1.0)
