import subprocess
import pygetwindow as gw
import time

class WindowsApplication():
    def __init__(self):
        pass

    def start_app(self, path: str, window_title: str):
        # 渡されたプログラムを実行スタートする
        subprocess.Popen(r'{}'.format(path))
        time.sleep(0.2)
        # 最新に開いたwindowをactivate
        print(gw.getAllTitles())
        target = gw.getWindowsWithTitle(window_title)[0]
        target.activate()

    #def close_app(self):
    #    pass