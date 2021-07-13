from remo import NatureRemoAPI

from settings import NATURE_REMO_TOKEN

AIRCON_NAME = 'air_con'
ROOM_LIGHT_NAME = 'room_right'


def client():
    api = NatureRemoAPI(NATURE_REMO_TOKEN)
    return api


def getAppliances(client):
    appliances = client.get_appliances()
    appliances = {
        AIRCON_NAME : appliances[-3],
        ROOM_LIGHT_NAME : appliances[-1]
    }
    return appliances

api = client()