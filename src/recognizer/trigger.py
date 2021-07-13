from settings import SHOURTCUTS
from recognizer.key_detector import is_pressed_hot_kay


def operation():
# 押されているショートカットキーに応じてその操作のデータを返す
    for shortcut in SHOURTCUTS:
        keys = shortcut['hot-keys']
        if is_pressed_hot_kay(keys):
            return shortcut
    return False
