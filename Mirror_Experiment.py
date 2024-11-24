import time
import numpy as np
import matplotlib.pyplot as plt
from Mirror_Basic import MirrorFrame

mirrorFrame = MirrorFrame(

    line_width=5, 
    line_length=100, 
    resolution=100
)

coords = mirrorFrame.generateCoords()

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

livePlt = LivePlt(x=time.time())

livePlt.ax.set_ylim(255*mirrorFrame.size_x*mirrorFrame.size_y*3, 0) # Avoid Data Move

while True:

    frame = mirrorFrame.getFrame()

    for coord in coords : mirrorFrame.drawLine(coord)

    frame_minus = np.abs(frame-mirrorFrame.canvas)

    mirrorFrame.imshow("Mirror", mirrorFrame.canvas)
    mirrorFrame.imshow("minus", frame_minus)

    livePlt.updatePlt(time.time(), np.sum(frame_minus))

    if mirrorFrame.isEnd():
        mirrorFrame.endStream()
        livePlt.endStrean()
        break