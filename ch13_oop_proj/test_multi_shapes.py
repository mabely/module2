# -*- coding: utf-8 -*-

from MovingShapes import *
import time

frame = Frame()
numshapes = 3
shapes = []
size = 60
for i in range(numshapes):
    shapes.append(Square(frame,size))
    shapes.append(Circle(frame,size))
    shapes.append(Diamond(frame,size))

for i in range(300):
# while True:
    for shape in shapes:
        shape.moveTick()
frame.close()

