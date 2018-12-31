# -*- coding: utf-8 -*-

from Shapes import *
from pylab import random as r

class MovingShape:
    def __init__(self, frame, shape, diameter):
#        Variables created here stores the object/figure created. 
#        Self refers to the entire class, declared here, the entire class can use it
#        init is called whenever an obj is created, establishing the attributes/var
#        for that obj
        
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, diameter)
        self.x = 0
        self.y = 0

        if r() < 0.5:
            self.dx = (5 + 10 * r()) * -1
            self.dy = (5 + 10 * r()) * -1
        else:
            self.dx = 5 + 10 * r()
            self.dy = 5 + 10 * r()
            
################ADD VARS TO STORE CURRENT LOCATION AND RATE OF MOVEMENT

    def goto(self, x, y):
        self.figure.goto(x, y)
        print(x, y)
    def moveTick(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.goto(self.x, self.y)

            
###############COMPLETE FUNCTION TO UPDATE A MOVINGSHAPE INSTANCE'S POSITION WITH EACH
###############TICK OF CLOCK

################COMPLETE THE FOLLOWING 3 DEFINTIONS OF CLASSES. 
class Square(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'square', diameter)

class Diamond(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'diamond', diameter)

class Circle(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'circle', diameter)
        
        