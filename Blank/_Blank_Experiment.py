import cv2
import numpy as np
import pandas as pd
from tqdm import tqdm
from Module import MirrorFrame, LivePlt

mirrorFrame = MirrorFrame(

    line_width=5, 
    line_length=100, 
    resolution=100
)

livePlt = LivePlt()

livePlt.ax.set_ylim(0, 1) # Avoid Data Move

coords = mirrorFrame.generateCoords()

data = { "Value" : [] }

max_value = 255*mirrorFrame.size_x*mirrorFrame.size_y*3

num = 0

for i in tqdm(range(10)):

    mirrorFrame.frame = frame = cv2.imread('Blank\\blank_red.png')

    for _ in range(100):

        for coord in coords : mirrorFrame.drawLine(coord)

        frame_minus = np.abs(frame.astype(np.int32)-mirrorFrame.canvas.astype(np.int32))

        data["Value"].append(np.sum(frame_minus)/max_value)

        livePlt.updatePlt(num, np.sum(frame_minus)/max_value)
        num += 1

        mirrorFrame.imshow("Mirror", mirrorFrame.canvas)

        if mirrorFrame.isEnd():
            mirrorFrame.endStream()
            break
    
    mirrorFrame.frame = frame = cv2.imread('Blank\\blank_blue.png')

    for _ in range(100):

        for coord in coords : mirrorFrame.drawLine(coord)

        frame_minus = np.abs(frame.astype(np.int32)-mirrorFrame.canvas.astype(np.int32))

        data["Value"].append(np.sum(frame_minus)/max_value)
        
        livePlt.updatePlt(num, np.sum(frame_minus)/max_value)
        num += 1

        mirrorFrame.imshow("Mirror", mirrorFrame.canvas)

        if mirrorFrame.isEnd():
            mirrorFrame.endStream()
            break

df = pd.DataFrame(data)
df.to_csv("experiment_data.csv")