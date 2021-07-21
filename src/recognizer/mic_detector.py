
import pyaudio
import pyautogui
from  typing import List

from recognizer.key_detector import is_pressed
from settings import KEYS, PYAUDIO_CHUNK,PYAUDIO_FORMAT,PYAUDIO_CHANNELS,PYAUDIO_RATE,PYAUDIO_DEVICE_INDEX

# Spaceを押している間だけ録音してその録音データを返す
def mic_recorder() -> List:
    mic = pyaudio.PyAudio()
    stream = mic.open(format = PYAUDIO_FORMAT,
                            channels = PYAUDIO_CHANNELS,
                            rate = PYAUDIO_RATE,
                            input = True,
                            input_device_index = PYAUDIO_DEVICE_INDEX,
                            frames_per_buffer= PYAUDIO_CHUNK)
    # CTRL SHIFT SPACEで発火
    frame = [] # 録音したデータ
    after_loop = True
    cnt = 0
    while is_pressed(KEYS['CTRL']) or after_loop:
        frame.append(stream.read(PYAUDIO_CHUNK))
        if not is_pressed(KEYS['CTRL']):
            cnt += 1
        if cnt > 1:
            after_loop = False
    stream.close()
    mic.terminate()
    del stream
    del mic
    return frame