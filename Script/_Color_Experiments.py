import os
import cv2
from tqdm import tqdm
import numpy as np
from Modules.Modules import MirrorFrame

TEST_TIME = 10
TEST_COUNT = 100

FOLDER = r'C:\Users\happp\Documents\2024_ScienceFair_Mirror\Blank\3'

BLANKS = [f for f in os.listdir(FOLDER)]

SAVE_PATH = os.path.join(FOLDER, f'data.npy')

mirrorFrame = MirrorFrame(

    line_width=5, 
    line_length=100, 
    resolution=100
)

coords = mirrorFrame.generateCoords()
max_value = 255*mirrorFrame.size_x*mirrorFrame.size_y*3

data = {}

for index, blank in enumerate(BLANKS):

    mirrorFrame.frame = frame = cv2.imread(os.path.join(FOLDER, blank))

    data[blank[0]] = np.zeros((10, 100), dtype=float)

    for i in tqdm(range(TEST_TIME)):

        # Init Canva
        mirrorFrame.canvas = np.zeros((mirrorFrame.size_y, mirrorFrame.size_x, 3), dtype=np.uint8)

        for j in range(TEST_COUNT):

            for coord in coords : mirrorFrame.drawLine(coord)

            frame_minus = np.abs(frame.astype(np.int32)-mirrorFrame.canvas.astype(np.int32))

            data[blank[0]][i, j] = np.sum(frame_minus)/max_value

# 保存合併後的數據
np.save(SAVE_PATH, data)