from functions.nature_remo.nature_remo_api import client, getAppliances, ROOM_LIGHT_NAME, api


def room_light_power():
    api.send_signal(getAppliances(api)[ROOM_LIGHT_NAME].signals[0].id)