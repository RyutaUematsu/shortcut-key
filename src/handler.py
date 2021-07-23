import time

from recognizer.trigger import operation
from functions.nature_remo.aircon import aircon_on, aircon_off
from functions.nature_remo.room_right import room_light_on, room_light_off
from functions.operate_windows.key_board import input_from_mic


def indicator(count, interval):
    if count == 1:
        print('\rReady    ',end='')
    if count == interval*1:
        print('\rReady.   ',end='')
    if count == interval*2:
        print('\rReady..  ',end='')
    if count == interval*3:
        print('\rReady... ',end='')
        count = -interval

def main():
    init = True
    count = 0
    while True:
        count += 1
        indicator(count, interval=40000)
        ope = operation()
        if ope:
            if init:
                init = False
                continue
            function = ope['function']
            print(function)
            print('\rProcessing...', end="")
            globals()[function]()
            print('\rComplete!    ', end='')
            time.sleep(3)

if __name__ == '__main__':
    main()