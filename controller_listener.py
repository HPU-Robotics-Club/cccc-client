from approxeng.input.selectbinder import ControllerResource
from time import sleep
import requests

hostname = "10.240.68.93"
port = 3000

def registerControllerListener():
    while True:
        # Checks to make sure joystick is connected
        try: 
            with ControllerResource() as joystick:
                print('Found joystick!')
                while joystick.connected:
                    x = joystick.rx
                    y = joystick.ry
                    l1 = joystick["lt"]
                    r1 = joystick["rt"]
                    dup = joystick["dup"]
                    ddown = joystick["ddown"]

                    IP = f'http://{hostname}:{port}'
                    res = requests.post(IP, json={
                        "controller_x": x,
                        "controller_y": y,
                        "controller_l1": l1,
                        "controller_r1": r1,
                        "controller_dup": dup,
                        "controller_ddown": ddown
                    })

                    
                    print(res.text)

        except IOError:
            print("Unable to find joystick!")
            sleep(1.0)
