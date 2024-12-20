import cv2
import numpy as np
from math import sin, cos
import matplotlib.pyplot as plt
from random import randrange, uniform

class LivePlt:

    data_limit = 100

    def __init__(self, x=0, y=0):

        plt.ion()

        self.fig, self.ax = plt.subplots()

        self.x = [x]
        self.y = [y]

        self.line, = self.ax.plot(x, y)

    def updatePlt(self, x, y):

        self.x.append(x)
        self.y.append(y)

        if len(self.x) > self.data_limit : self.x.pop(0)
        if len(self.y) > self.data_limit : self.y.pop(0)

        self.line.set_xdata(self.x)
        self.line.set_ydata(self.y)

        self.ax.relim()
        self.ax.autoscale_view()
        plt.draw()
    
    def endStrean(self):

        plt.ioff()

class MirrorFrame:

    def __init__(
            
        self, frame_width=800, cap_num=0, 
        line_width=5, line_length=100, resolution=100
    ):

        self.size_x = frame_width
        self.size_y = int(self.size_x * 0.75)

        self.cap = cv2.VideoCapture(cap_num)
        self.canvas = np.zeros((self.size_y, self.size_x, 3), dtype=np.uint8)

        self.line_width = line_width
        self.line_length = line_length

        self.resolution = resolution

    def getFrame(self):

        _, frame = self.cap.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (self.size_x, self.size_y))

        self.frame = frame

        return frame
    
    def drawLine(self, coord):

        x = coord[0]+randrange(0, self.resolution)
        y = coord[1]+randrange(0, self.resolution)
        c = uniform(0, 360)

        cos_c = cos(c)
        sin_c = sin(c)

        # Get All Point
        points = [

            (int(x + cos_c * k), int(y + sin_c * k))
            for k in range(-self.line_length, self.line_length)
        ]

        # Check Point in Frame
        valid_points = [

            (x, y) for x, y in points 
            if (0 < x < self.size_x and 0 < y < self.size_y)
        ]

        if not valid_points:
            return
        
        # Get Color
        colors = np.array([

            [self.frame[j, i, 0] for i, j in valid_points],
            [self.frame[j, i, 1] for i, j in valid_points],
            [self.frame[j, i, 2] for i, j in valid_points]
        ])

        # Caculate Average Color
        draw_color = tuple(

            int(np.mean(color.astype(np.float32))) 
            for color in colors
        )

        # Draw
        cv2.line(

            self.canvas, 
            points[0], points[-1], 
            draw_color, 
            self.line_width
        )
    
    def generateCoords(self):

        coords = [
        
            (i, j) 
            for i in range(0, self.size_x, self.resolution) 
            for j in range(0, self.size_y, self.resolution)
        ]

        return coords
    
    def imshow(self, name, frame) : cv2.imshow(name, frame)

    def isEnd(self) : return cv2.waitKey(1) & 0xFF == ord('q')
    
    def endStream(self):

        print("exit...")

        self.cap.release()
        cv2.destroyAllWindows()