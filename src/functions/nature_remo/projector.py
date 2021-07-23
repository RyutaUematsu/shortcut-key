from functions.nature_remo.nature_remo_api import getAppliances, PROJECTOR_NAME, api


def projector_power():
    api.send_signal(getAppliances(api)[PROJECTOR_NAME].signals[0].id)
