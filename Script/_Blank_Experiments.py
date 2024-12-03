import cv2
import numpy as np
import pandas as pd
from tqdm import tqdm
from Modules.Modules import MirrorFrame

test_time = 10
test_count = 100

blank1 = r'Blank\blank_yellow.png' 
blank2 = r'Blank\blank_blue.png' 

save_path = r'exp_data.csv'

mirrorFrame = MirrorFrame(

    line_width=5, 
    line_length=100, 
    resolution=100
)

coords = mirrorFrame.generateCoords()

data = {} 

max_value = 255*mirrorFrame.size_x*mirrorFrame.size_y*3

num = 0

for i in tqdm(range(test_time)):

    blank_name = blank1 if i % 2 == 0 else blank2
    mirrorFrame.frame = frame = cv2.imread(blank_name)
    data[i] = [0] * test_count

    for j in range(test_count):

        for coord in coords : mirrorFrame.drawLine(coord)

        frame_minus = np.abs(frame.astype(np.int32)-mirrorFrame.canvas.astype(np.int32))

        data[i][j] = np.sum(frame_minus)/max_value

df = pd.DataFrame(data)
df.to_csv(save_path)