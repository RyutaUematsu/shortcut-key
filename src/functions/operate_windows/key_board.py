# Pythonからキーボード操作
import pyautogui as keyboard
import pyperclip
from typing import List

from recognizer.mic_detector import mic_recorder


def input_from_mic():
    frame: List = mic_recorder()
    input_text: str = speach_to_text_gcp(frame)
    # クリップボードを使って入力
    pyperclip.copy(input_text)
    keyboard.hotkey('ctrl','v')
