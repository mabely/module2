# -*- coding: utf-8 -*-

from Shapes import *
from pylab import random as r
import time

class MovingShape:
    def __init__(self, frame, shape, diameter):
    # Variables created here stores the object/figure created. 
    # Self refers to the entire class, declared here, the entire class can use it
    # init is called whenever an obj is created, establishing the attributes/var
    # for that obj
        
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, diameter)
        self.width = frame.width
        self.height = frame.height

        # Initialising the starting position of the shape at 50,50 before movement
        # self.x = 50
        # self.y = 50
        # self.goto(self.diameter/2, self.diameter/2)
        # print('I am at starting position')

        # Calls the method below to calculate min/max positions
        self.minMax()

        # r() in the if/else statement decides whether it moves in pos or neg direction. Formula gives random value between
        # 5-15 to give dx,dy varies velocity values. movetick() updates this
        randnum = r()
        if randnum < 0.5:
            self.dx = (5 + 10 * r()) * -1
            self.dy = (5 + 10 * r()) * -1
        else:
            self.dx = 5 + 10 * r()
            self.dy = 5 + 10 * r()

    def goto(self, x, y):
        self.figure.goto(x, y)
        print(x, y)

    def minMax(self):
        # Min, max coordinates and calculations for shapes to move within a set frame
        self.minx = self.diameter/2
        self.miny = self.diameter/2
        self.maxx = self.width - (self.diameter/2)
        self.maxy = self.height - (self.diameter/2)
        self.x = self.minx + r() * (self.maxx - self.minx)
        self.y = self.miny + r() * (self.maxy - self.miny)
        self.goto(self.x, self.y)

    def moveTick(self):
        # dx,dy are the increment of each loop of movement/rate of movement
        self.x = self.x + self.dx 
        self.y = self.y + self.dy 
        # These conditionals revert numbers for when it hits the min/max x, y
        if self.x > self.maxx: 
            self.dx = self.dx * -1
        if self.x < self.minx:
            self.dx = self.dx * -1
            # time.sleep(15)
        if self.y > self.maxy:
            self.dy = self.dy * -1
        if self.y < self.miny:
            self.dy = self.dy * -1
            # time.sleep(15)
            # self.vanish(self)

        self.goto(self.x,self.y)

class Square(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'square', diameter)

class Diamond(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'diamond', diameter)

    def minMax(self):
         # Min, max coordinates and calculations for shapes to move within a set frame
         self.minx = self.diameter*0.74
         self.miny = self.diameter*0.74
         self.maxx = self.width - (self.diameter*0.74)
         self.maxy = self.height - (self.diameter*0.74)
         self.x = self.minx + r() * (self.maxx - self.minx)
         self.y = self.miny + r() * (self.maxy - self.miny)
         self.goto(self.x, self.y)
         # Min, max coordinates and calculations for shapes to move within a set frame

class Circle(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'circle', diameter)
        
        