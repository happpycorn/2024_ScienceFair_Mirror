import time
import numpy as np
import matplotlib.pyplot as plt
from Mirror_Basic import MirrorFrame

plt.ion()

mirrorFrame = MirrorFrame(

    line_width=5, 
    line_length=100, 
    resolution=100
)

coords = mirrorFrame.generateCoords()

fig, ax = plt.subplots()

x = [time.time()]
y = [0]

data_limit = 100

line, = ax.plot(x, y)

ax.set_ylim(255*mirrorFrame.size_x*mirrorFrame.size_y*3, 0)

while True:

    frame = mirrorFrame.getFrame()

    for coord in coords : mirrorFrame.drawLine(coord)

    frame_minus = np.abs(frame-mirrorFrame.canvas)

    mirrorFrame.imshow("Mirror", mirrorFrame.canvas)
    mirrorFrame.imshow("minus", frame_minus)

    x.append(time.time())
    y.append(np.sum(frame_minus))

    if len(x) > data_limit : x.pop(0)
    if len(y) > data_limit : y.pop(0)

    line.set_xdata(x)
    line.set_ydata(y)

    ax.relim()
    ax.autoscale_view()
    plt.draw()

    if mirrorFrame.endStream():
        plt.ioff()
        break