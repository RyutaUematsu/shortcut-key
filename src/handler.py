import time

from recognizer.trigger import operation
from functions.nature_remo.aircon import aircon_on, aircon_off
from functions.nature_remo.room_right import room_light_power


def main():
    init = True
    while True:
        ope = operation()
        if ope:
            if init:
                init = False
                continue
            function = ope['function']
            print(function)
            globals()[function]()
            time.sleep(3)
main()