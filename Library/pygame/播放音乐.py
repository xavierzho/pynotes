import time
import pygame



# 路径
filePath = r'E:\QQ音乐\音乐库\都智文 - 你和我都没有错.mp3'

# 初始化
pygame.mixer.init()
# 加载音乐
pygame.mixer.music.load(filePath)
# 播放
pygame.mixer.music.play()
time.sleep(193)

