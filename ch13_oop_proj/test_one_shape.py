# -*- coding: utf-8 -*-

from MovingShapes import *
import time
frame = Frame()
shape1 = Diamond(frame,100)

# This shows min and max positions
t.hideturtle()
shape1.goto(shape1.minx, shape1.miny)
time.sleep(2)
shape1.goto(shape1.maxx, shape1.maxy)
time.sleep(2)

for i in range(100):
   shape1.moveTick()
