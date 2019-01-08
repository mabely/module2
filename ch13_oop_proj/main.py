# -*- coding: utf-8 -*-

from Shapes import *
import time
frame = Frame()
s1 = Shape('square', 100)

# checks that the start position is half of diameter of shape
time.sleep(2)
s1.goto(200,200)
time.sleep(3)
#s1.turtle.showturtle()

# for i in range (1000):
#     print(x ,y)
#     s1.goto(x, y)
#time.sleep(10)

# frame.clear()

frame.close()
