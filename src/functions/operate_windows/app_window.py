import pygetwindow as getwindow
import pyautogui as autogui

from recognizer.key_detector import is_pressed_hot_kay
from settings import SHOURTCUTS

def window_catch():
    """マウスポインタの位置にwindowを移動させる"""
    
    x,y = autogui.position()
    autogui.click()
    target = getwindow.getWindowsWithTitle(getwindow.getActiveWindowTitle())[0]
    keys: list =  [shortcut['hot-keys'] for shortcut in SHOURTCUTS if shortcut['function'] == 'window_catch'][0]
    
    w = target.width
    h = target.height
    if not target.title:
        return
    while is_pressed_hot_kay(keys):
        x,y = autogui.position()
        x = int(round(x-w/2,0))
        y = int(round(y-h/2,0))
        target.moveTo(x,y)