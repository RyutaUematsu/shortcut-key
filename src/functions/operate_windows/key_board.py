# Pythonからキーボード操作
import pyautogui as keyboard
import pyperclip
from typing import List
import re
import time

from recognizer.mic_detector import mic_recorder
from ext_services.gcp.speach_to_text import sst


def input_from_mic():
    input_text = ''
    frame: List = mic_recorder()
    input_text: str = sst(frame)
    if not (input_text):
        return
    # クリップボードを使って入力
    # FIXME 汎用性を持たせる
    if "検索" in input_text:
        input_text = re.findall('(.*).検索', input_text)[0]
        pyperclip.copy(input_text)
        keyboard.hotkey('ctrl','v')
        time.sleep(0.1)
        keyboard.press('enter')
        return
    pyperclip.copy(input_text)
    keyboard.hotkey('ctrl','v')
