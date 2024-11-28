import cv2
import numpy as np
import pandas as pd
from tqdm import tqdm
from Modules.Modules import MirrorFrame

mirrorFrame = MirrorFrame(

    line_width=5, 
    line_length=100, 
    resolution=100
)

coords = mirrorFrame.generateCoords()

data = {

    "Value" : [],
    "Time"  : []
}

max_value = 255*mirrorFrame.size_x*mirrorFrame.size_y*3

num = 0

for i in tqdm(range(10)):

    mirrorFrame.frame = frame = cv2.imread('Blank\\blank_red.png')

    for num in range(num, num+100):

        for coord in coords : mirrorFrame.drawLine(coord)

        frame_minus = np.abs(frame.astype(np.int32)-mirrorFrame.canvas.astype(np.int32))

        data["Value"].append(np.sum(frame_minus)/max_value)
        data["Time"].append(num)
    
    mirrorFrame.frame = frame = cv2.imread('Blank\\blank_blue.png')

    for num in range(num, num+100):

        for coord in coords : mirrorFrame.drawLine(coord)

        frame_minus = np.abs(frame.astype(np.int32)-mirrorFrame.canvas.astype(np.int32))
        
        data["Value"].append(np.sum(frame_minus)/max_value)
        data["Time"].append(num)

df = pd.DataFrame(data)
df.to_csv("experiment_data.csv")