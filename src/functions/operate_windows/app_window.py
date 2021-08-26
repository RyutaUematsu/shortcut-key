import pygetwindow as getwindow
import pyautogui as autogui
import time

from recognizer.key_detector import is_pressed_hot_kay
from settings import SHOURTCUTS


DEFAULT_WIDTH = 1500
DEFAULT_HEIGHT = 927 

DEFAULT_LEFT = 3543
DEFAULT_RIGHT = 5610
DEFAULT_TOP = 100
DEFAULT_TOP_INTERVAL =  400

MAX_ORDER = 5

def move_window(target) -> int:
    keys: list =  [shortcut['hot-keys'] for shortcut in SHOURTCUTS if shortcut['function'] == 'window_catch'][0]
    w = target.width
    h = target.height
    while is_pressed_hot_kay(keys):
        x,y = autogui.position()
        x = int(round(x-w/2,0))
        y = int(round(y-h/2,0))
        target.moveTo(x,y)
        x,y = autogui.position()
    return x,y


global window_state
window_state = []    #モニター3に投げ込まれた順番にappendする

def organize_windows(target):
    window_state.append(target)
    target.resizeTo(DEFAULT_WIDTH,  DEFAULT_HEIGHT)
    order = len(window_state) -1 # 何番目に投げ込まれたのか
    if order > 14:
        return
    
    if not order%2:
        target.moveTo(DEFAULT_LEFT, DEFAULT_TOP + (DEFAULT_TOP_INTERVAL*(int(order/2))))
    else:
        target.moveTo(DEFAULT_RIGHT, DEFAULT_TOP + (DEFAULT_TOP_INTERVAL*(int(((order+1)/2)-1))))


def window_aggregate():
    for order, window in enumerate(window_state):
        window.resizeTo(DEFAULT_WIDTH,  DEFAULT_HEIGHT)
        window.activate()
        if not order%2:
            window.moveTo(DEFAULT_LEFT, DEFAULT_TOP + (DEFAULT_TOP_INTERVAL*(int(order/2))))
        else:
            window.moveTo(DEFAULT_RIGHT, DEFAULT_TOP + (DEFAULT_TOP_INTERVAL*(int(((order+1)/2)-1))))

def onResetOrder():
    # モニター3にあるwindowをすべてリセットして並べ直す
    window_state.clear()
    all_window = getwindow.getAllWindows()
    for win in all_window:
        if 3440 < win.left and win.title:
            window_state.append(win)
    window_aggregate()
    return


def window_catch():
    """マウスポインタの位置にwindowを移動させる"""
    # すべてのウインドをチェックする
    all_window = getwindow.getAllWindows()
    for win in window_state:
        if not win in all_window:
            window_state.remove(win)
            window_aggregate()
        
    
    x, y = autogui.position()
    autogui.click()
    target = getwindow.getWindowsWithTitle(getwindow.getActiveWindowTitle())[0]
    if not target.title:
        return

    target.restore()

    # 移動開始
    end_x, end_y = move_window(target)

    # ウインド廃棄
    if end_x == 7279 and end_y == 2159:
        target.close()
        if target in window_state:
            window_state.remove(target)
            window_aggregate()
        return

    # 左1
    if end_x == -1920:
        autogui.hotkey('win','left', interval=0.1)
        time.sleep(0.1) 
        autogui.press('esc')
        return 
    # 右1
    if -100 < end_x < 0:
        autogui.hotkey('win','right', interval=0.1)        
        time.sleep(0.1)
        autogui.press('esc')
        return
    # 左2
    if 0 < end_x < 500:
        autogui.hotkey('win','left', interval=0.1) 
        time.sleep(0.1)
        autogui.press('esc')
        return 
    # 右2
    if 3244 - 500 < end_x < 3440:
        autogui.hotkey('win','right', interval=0.1)
        time.sleep(0.1)
        autogui.press('esc')
        return

        
    if 3440 < end_x and end_y == 0:
        onResetOrder()
        return

    # 持ち出されたwindowがモニター3からなのかを判別してaggregate
    if target in window_state:
        window_state.remove(target)
        window_aggregate()

    # モニター3
    if 3440 < end_x:
        organize_windows(target) 


    # 最大化
    if end_y == 0:
        target.maximize()
    
    target.activate()
    
    
