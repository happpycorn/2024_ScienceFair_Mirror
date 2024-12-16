import os
import cv2
import sys
from tqdm import tqdm
import numpy as np
from Modules.Modules import MirrorFrame

TEST_TIME = 10
TEST_COUNT = 100

FOLDER = r'C:\Users\happp\Documents\2024_ScienceFair_Mirror'

BLANKS = {
    'R' : os.path.join(FOLDER, r'Blank\blank_red.png'),
    'Y' : os.path.join(FOLDER, r'Blank\blank_yellow.png'),
    'B' : os.path.join(FOLDER, r'Blank\blank_blue.png')
}

line_width = int(sys.argv[1])
line_length = int(sys.argv[2])
resolution = int(sys.argv[3])

SAVE_PATH = os.path.join(FOLDER, f'data_{resolution}.npy')

mirrorFrame = MirrorFrame(

    line_width=line_width*2+1, 
    line_length=line_length*10+1, 
    resolution=resolution*25+10
)

coords = mirrorFrame.generateCoords()
max_value = 255*mirrorFrame.size_x*mirrorFrame.size_y*3

def dataInit():

    dtype = [
        ("ID", int),
        ("RY", float, (10, 100)), 
        ("YR", float, (10, 100)), 
        ("YB", float, (10, 100)),
        ("BY", float, (10, 100)), 
        ("BR", float, (10, 100)), 
        ("RB", float, (10, 100))
    ]

    data = np.zeros(1, dtype=dtype)

    data["ID"] = line_width * 10000 + line_length * 100 + resolution

    return data

data = dataInit()

TEST_ORDER = [('RY', 'YR'), ('YB', 'BY'), ('BR', 'RB')]

for blank1, blank2 in TEST_ORDER:

    # init

    blank_name = BLANKS[blank2[0]]
    mirrorFrame.frame = frame = cv2.imread(blank_name)

    for _ in tqdm(range(TEST_COUNT)):

        for coord in coords : mirrorFrame.drawLine(coord)

    for i in tqdm(range(TEST_TIME)):

        # blank 1

        blank_name = BLANKS[blank1[0]]
        mirrorFrame.frame = frame = cv2.imread(blank_name)

        for j in range(TEST_COUNT):

            for coord in coords : mirrorFrame.drawLine(coord)

            frame_minus = np.abs(frame.astype(np.int32)-mirrorFrame.canvas.astype(np.int32))

            data[blank1][0][i][j] = np.sum(frame_minus)/max_value
        
        # blank 2

        blank_name = BLANKS[blank2[0]]
        mirrorFrame.frame = frame = cv2.imread(blank_name)

        for j in range(TEST_COUNT):

            for coord in coords : mirrorFrame.drawLine(coord)

            frame_minus = np.abs(frame.astype(np.int32)-mirrorFrame.canvas.astype(np.int32))

            data[blank2][0][i][j] = np.sum(frame_minus)/max_value

if os.path.exists(SAVE_PATH):
    # 如果文件存在，讀取現有數據並合併
    existing_data = np.load(SAVE_PATH, allow_pickle=True)
    combined_data = np.concatenate([existing_data, data])
else:
    # 如果文件不存在，直接保存新數據
    combined_data = data

# 保存合併後的數據
np.save(SAVE_PATH, combined_data)

print(data["ID"])