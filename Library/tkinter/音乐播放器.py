import tkinter
import pygame
from tkinter import *
from tkinter import filedialog


# 暂停
def pause():
    pygame.mixer.music.pause()


# 停止
def stop():
    pygame.mixer.music.stop()


# 播放
def start():
    pygame.mixer.music.start()


# 选择音乐
def choose():
    file = filedialog.askopenfilename()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


# 窗口
win = tkinter.Tk()
# 标题
win.title('Tins')
# 大小和位置
win.geometry("400x300+400+200")
# 一级菜单
one = Menu()
win.config(menu=one)
Menu(one)

pygame.init()

l = Label(win, text="欢迎来到Tins播放器")
l.pack()
Button(win, text="选择音乐", command=choose).pack()  # 菜单按钮
Button(win, text="暂停", command=pause).pack()
Button(win, text="继续", command=start).pack()
Button(win, text="停止", command=stop).pack()
win.mainloop()
