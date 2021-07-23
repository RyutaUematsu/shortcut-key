import pyaudio
import os
from dotenv import load_dotenv
load_dotenv()

# ショートカットキー 設定
SHOURTCUTS = [
    {
        'operation': "Aircon on",
        'hot-keys': ['CTRL', 'A', 'UP'],
        'function': 'aircon_on'
    },
    {
        'operation': "Aircon off",
        'hot-keys': ['CTRL', 'A', 'DOWN'],
        'function': 'aircon_off'
    },
    {
        'operation': "Aircon volume 1",
        'hot-keys': ['CTRL', 'A', 'NUM1'],
        'function': 'aircon_volume_1'
    },
    {
        'operation': "Aircon volume 3",
        'hot-keys': ['CTRL', 'A', 'NUM3'],
        'function': 'aircon_volume_3'
    },
    {
        'operation': "Light on",
        'hot-keys': ['CTRL', 'L', 'O'],
        'function': 'room_light_on'
    },
    {
        'operation': "Light off",
        'hot-keys': ['CTRL', 'L', 'F'],
        'function': 'room_light_off'
    },
    {
        'operation': "input from mic",
        'hot-keys': ['CTRL', 'ALT', 'SPACE'],
        'function': 'input_from_mic',
    },
    {
        'operation': "Projector power",
        'hot-keys': ['CTRL', 'ALT', 'P'],
        'function': 'projector_power',
    }
]


NATURE_REMO_TOKEN = os.environ['NATURE_REMO_TOKEN']

# ctypes key mapping https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
KEYS = {
    'A': 0x41,
    'B': 0x42,
    'C': 0x43,
    'D': 0x44,
    'E': 0x45,
    'F': 0x46,
    'G': 0x47,
    'H': 0x48,
    'I': 0x49,
    'J': 0x4A,
    'K': 0x4B,
    'L': 0x4C,
    'M': 0x4D,
    'N': 0x4E,
    'O': 0x4F,
    'P': 0x50,
    'Q': 0x51,
    'R': 0x52,
    'S': 0x53,
    'T': 0x54,
    'U': 0x55,
    'V': 0x56,
    'W': 0x57,
    'X': 0x58,
    'Y': 0x59,
    'Z': 0x5A,
    'BACK': 8,
    'TAB': 9,
    'CLEAR': 12,
    'RETURN': 13,
    'PAUSE': 19,
    'CAPSLOCK': 20,
    'ESC': 27,
    'SPACE': 32,
    'PGUP': 33,
    'PGDOWN': 34,
    'END': 35,
    'HOME': 36,
    'LEFT': 37,
    'UP': 38,
    'RIGHT': 39,
    'DOWN': 40,
    'INSERT': 45,
    'DELETE': 46,
    'LWIN': 91,
    'RWIN': 92,
    'MENU': 93,
    'NUM0': 0x30,
    'NUM1': 0x31,
    'NUM2': 0x32,
    'NUM3': 0x33,
    'NUM4': 0x34,
    'NUM5': 0x35,
    'NUM6': 0x36,
    'NUM7': 0x37,
    'NUM8': 0x38,
    'NUM9': 0x39,
    'MULTIPLY': 106,
    'ADD': 107,
    'SUBTRACT': 109,
    'DECIMAL': 110,
    'DIVIDE': 111,
    'F1': 112,
    'F2': 113,
    'F3': 114,
    'F4': 115,
    'F5': 116,
    'F6': 117,
    'F7': 118,
    'F8': 119,
    'F9': 120,
    'F10': 121,
    'F11': 122,
    'F12': 123,
    'F13': 124,
    'F14': 125,
    'F15': 126,
    'F16': 127,
    'F17': 128,
    'F18': 129,
    'F19': 130,
    'F20': 131,
    'F21': 132,
    'F22': 133,
    'F23': 134,
    'F24': 135,
    'NUMLOCK': 144,
    'SCROLLLOCK': 145,
    'SHIFT': 160,
    'RSHIFT': 161,
    'CTRL': 162,
    'RCTRL': 163,
    'ALT': 164,
    'RALT': 165,
    'COLON': 186,
    'EQUALS': 187,
    'COMMA': 188,
    'UNDERSCORE': 189,
    'PERIOD': 190,
    'FORWARDSLASH': 191,
    'AT': 192,
    'LBRACKET': 219,
    'BACKSLASH': 220,
    'RBRACKET': 221,
    'HASH': 222,
    'TILDE': 223,
    'ENTER': 0x0D
}

# pyaudio settings
PYAUDIO_RATE = 16000
PYAUDIO_CHUNK = int(PYAUDIO_RATE/10)
PYAUDIO_FORMAT = pyaudio.paInt16
PYAUDIO_CHANNELS = 1
PYAUDIO_DEVICE_INDEX = 1

# GCP Speach to text settings
from google.cloud import speech_v1p1beta1 as speech
SST_LANG = 'ja-JP'
SST_BOOT_WARD = [
    {"phrases": ["入力","検索"], "boost":12}
]
SST_METADATA = {
        "interaction_type": speech.RecognitionMetadata.InteractionType.VOICE_COMMAND,
        "recording_device_type": speech.RecognitionMetadata.RecordingDeviceType.PC,
                        }
SST_MODEL = 'command_and_search'