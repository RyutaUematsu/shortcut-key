
import pyaudio
from  typing import List

from recognizer.key_detector import is_pressed
from settings import KEYS, PYAUDIO_CHUNK,PYAUDIO_FORMAT,PYAUDIO_CHANNELS,PYAUDIO_RATE,PYAUDIO_DEVICE_INDEX

# Spaceを押している間だけ録音してその録音データを返す

stream = pyaudio.PyAudio().open(format = PYAUDIO_FORMAT,
                            channels = PYAUDIO_CHANNELS,
                            rate = PYAUDIO_RATE,
                            input = True,
                            input_device_index = PYAUDIO_DEVICE_INDEX,
                            frames_per_buffer= PYAUDIO_CHUNK)

def mic_recorder() -> List:
    # CTRL SHIFT SPACEで発火
    frame = [] # 録音したデータ
    while is_pressed(KEYS['SPACE']):
        frame.append(stream.read(PYAUDIO_CHUNK))
    return frame