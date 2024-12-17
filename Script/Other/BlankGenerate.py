import cv2
import numpy as np

FRAME_SIZE_X = 800
FRAME_SIZE_Y = int(FRAME_SIZE_X * 0.75)

RESOLUTION = 200

blank = np.zeros((FRAME_SIZE_Y, FRAME_SIZE_X, 3), dtype=np.uint8)

COLORS = [
    (0, 0, 255),
    (0, 255, 0),
    (255, 0, 0),
    (0, 255, 255),
    (255, 0, 255),
    (255, 255, 0),
    (255, 255, 255),
]

for row in range(0, FRAME_SIZE_X, RESOLUTION):
    for col in range(0, FRAME_SIZE_X, RESOLUTION):

        y_start, y_end = row, row + RESOLUTION
        x_start, x_end = col, col + RESOLUTION

        blank[y_start:y_end, x_start:x_end] = COLORS[(row+col)//RESOLUTION % 6]

        # if (row+col)//RESOLUTION % 2 != 0:
        #     blank[y_start:y_end, x_start:x_end] = (255, 0, 0)
        # else:
        #     blank[y_start:y_end, x_start:x_end] = (0, 0, 0)


cv2.imwrite(r"Blank/blank.png", blank)