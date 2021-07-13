from functions.nature_remo.nature_remo_api import getAppliances, AIRCON_NAME, api


def aircon_on():
    api.update_aircon_settings(getAppliances(api)[AIRCON_NAME].id,button='power-on')

def aircon_off():
    api.update_aircon_settings(getAppliances(api)[AIRCON_NAME].id,button='power-off')