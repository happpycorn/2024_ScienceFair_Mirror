import os
import time
from tqdm import tqdm
import numpy as np
from Modules.Modules import MirrorFrame

TEST_RANGE = 20
TEST_TIME = 100

FOLDER = r'C:\Users\happp\Documents\2024_ScienceFair_Mirror\Blank\2_192'

SAVE_PATH = os.path.join(FOLDER, f'data.npy')

mirrorFrame = MirrorFrame(

    line_width=5, 
    line_length=100, 
    resolution=100
)

max_value = 255*mirrorFrame.size_x*mirrorFrame.size_y*3
mirrorFrame.frame = frame = np.zeros((600, 800, 3), dtype=np.uint8)

coords = mirrorFrame.generateCoords()

# Exp1, 3

exp_1 = np.zeros((TEST_RANGE, TEST_TIME), dtype=float)

exp_3 = np.zeros((TEST_RANGE, TEST_TIME), dtype=float)

for i in tqdm(range(TEST_RANGE)):

    mirrorFrame.line_width = i*2+1

    for j in range(TEST_TIME):

        start_time = time.time()

        mirrorFrame.drawLine((350, 250))

        end_time = time.time()

        exp_1[i][j] = end_time - start_time
    
    for j in range(TEST_TIME):

        start_time = time.time()

        for coord in coords : mirrorFrame.drawLine(coord)

        end_time = time.time()

        exp_3[i][j] = end_time - start_time

mirrorFrame.line_width = 5

# Exp2, 4

exp_2 = np.zeros((TEST_RANGE, TEST_TIME), dtype=float)

exp_4 = np.zeros((TEST_RANGE, TEST_TIME), dtype=float)

for i in tqdm(range(TEST_RANGE)):

    mirrorFrame.line_length = i*10+1

    for j in range(TEST_TIME):

        start_time = time.time()

        mirrorFrame.drawLine((350, 250))

        end_time = time.time()

        exp_2[i][j] = end_time - start_time
    
    for j in range(TEST_TIME):

        start_time = time.time()

        for coord in coords : mirrorFrame.drawLine(coord)

        end_time = time.time()

        exp_4[i][j] = end_time - start_time

mirrorFrame.line_length = 100

# Exp5

exp_5 = np.zeros((TEST_RANGE, TEST_TIME), dtype=float)

for i in tqdm(range(TEST_RANGE)):

    mirrorFrame.resolution = i*10+1

    coords = mirrorFrame.generateCoords()

    for j in range(range(TEST_TIME)):

        start_time = time.time()

        for coord in coords : mirrorFrame.drawLine(coord)

        end_time = time.time()

        exp_2[i][j] = end_time - start_time

# 保存合併後的數據
np.save(SAVE_PATH, [exp_1, exp_2, exp_3, exp_4, exp_5])