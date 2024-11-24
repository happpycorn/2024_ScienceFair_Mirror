import cv2
import numpy as np
from math import sin, cos
from random import randrange, uniform

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
    
    def endStream(self):

        if not cv2.waitKey(1) & 0xFF == ord('q') : return False

        print("exit...")

        mirrorFrame.cap.release()
        cv2.destroyAllWindows()

        return True


mirrorFrame = MirrorFrame()

coords = mirrorFrame.generateCoords()

while True:

    frame = mirrorFrame.getFrame()

    for coord in coords : mirrorFrame.drawLine(coord)

    mirrorFrame.imshow("Mirror", mirrorFrame.canvas)
    mirrorFrame.imshow("cap", frame)

    if mirrorFrame.endStream():
        break