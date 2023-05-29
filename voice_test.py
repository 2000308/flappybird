# -*- coding: utf-8 -*-
import sys
import pygame as py
py.init()
screen = py.display.set_mode((422,512))  
voice = py.mixer.Sound('audio/start.wav')
voice1 = py.mixer.Sound('audio/flap.wav')
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == py.KEYDOWN and event.key == py.K_SPACE:
            voice.play()
            #voice1.play()