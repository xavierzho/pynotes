import time
import pygame
import win32api
import win32gui
import win32con
import threading


def play_music():
    # 括号里填入音乐数量
    for i in range(5):
        # 路径
        file_path = r'E:\QQ音乐\音乐库\{}.mp3'  # {}表示随机读取音乐

        # 初始化
        pygame.mixer.init()
        # 加载音乐
        pygame.mixer.music.load(file_path)
        # 播放
        pygame.mixer.music.play()
        time.sleep(10)


def change_wallpaper():
    for i in range():  # 括号里填入图片数量
        path = r'填入图片文件路径\{}.jpg'.format(i)
        # 打开注册表
        reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
        win32api.RegSrtValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
        win32gui.SystemparametersInfo(win32con.SPI_SETDESKWALLPAPER, '', win32con.SPIF_SENDWININICHANGE)
        time.sleep(5)


# 开启一个线程去做播放音乐的事情
threading.Thread(target=play_music).start()
# 更改桌面背景
change_wallpaper()



