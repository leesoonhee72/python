# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:52:53 2021

@author: Mac_1
"""

import turtle as t
import random as r

screen=t.Screen()
image1="front.gif"
image2="back.gif"
screen.addshape(image1)
screen.addshape(image2)

for i in range(4):
    t.delay(500)
    coin=r.randin(0, 1)
    
    if coin==0:
        t.shape(image1)
        t.stamp()
        
    else:
        t.shape(image2)
        t.stamp()
    
t.exitonlick()
