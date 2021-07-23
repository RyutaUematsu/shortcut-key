import ctypes
from typing import List

from settings import KEYS

def is_pressed(key: str):
    if ctypes.windll.user32.GetAsyncKeyState(key):
        return True

def is_pressed_hot_kay(keys: List):
    return all([is_pressed(KEYS[key]) for key in keys])