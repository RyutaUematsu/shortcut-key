import time 

from functions.nature_remo.nature_remo_api import client, getAppliances, ROOM_LIGHT_NAME, api


def room_light_power():
    api.send_signal(getAppliances(api)[ROOM_LIGHT_NAME].signals[0].id)

def room_light_on():
    room_light_power()

def room_light_off():
    room_light_power()
    time.sleep(3)
    room_light_power()