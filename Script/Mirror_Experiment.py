import time
import numpy as np
from Modules.Modules import LivePlt, MirrorFrame

mirrorFrame = MirrorFrame(

    line_width=5, 
    line_length=100, 
    resolution=100
)

coords = mirrorFrame.generateCoords()

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