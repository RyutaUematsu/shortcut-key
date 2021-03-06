import time

from recognizer.trigger import operation
from functions.nature_remo.aircon import aircon_on, aircon_off, aircon_volume_1, aircon_volume_3
from functions.nature_remo.room_right import room_light_on, room_light_off
from functions.nature_remo.projector import projector_power
from functions.operate_windows.key_board import input_from_mic
from functions.operate_windows.app_window import window_catch
from functions.windows_app.edge.operation_edge import start_edge


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
            try:
                globals()[function]()
            except Exception as e:
                print(e)
            print('\rComplete!    ', end='')
            if not ope.get('interval_skip'):
                time.sleep(3)

if __name__ == '__main__':
    main()      