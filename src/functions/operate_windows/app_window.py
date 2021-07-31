import pygetwindow as getwindow
import pyautogui as autogui
import time


def window_catch():
    """マウスポインタの位置にwindowを移動させる"""
    x,y = autogui.position()
    target = getwindow.getWindowsWithTitle(getwindow.getActiveWindowTitle())[0]

    start = time.time()
    w = target.width
    h = target.height
    while time.time() - start < 1:
        # 1秒間は自由に動かせる
        x,y = autogui.position()
        x = int(round(x-w/2,0))
        y = int(round(y-h/2,0))
        target.moveTo(x,y)