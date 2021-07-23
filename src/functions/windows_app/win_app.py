import subprocess
import pygetwindow as gw
import time

class WindowsApplication():
    def __init__(self):
        pass

    def start_app(self, path: str):
        # 渡されたプログラムを実行スタートする
        subprocess.Popen(r'{}'.format(path))

    #def close_app(self):
    #    pass