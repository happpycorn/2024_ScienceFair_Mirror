import numpy as np
import cv2

# 顏色為 BGR (3, 3, 4)
color = (int(np.uint8(3)), int(np.uint8(3)), int(np.uint8(4)))  # 顯式轉換為 Python 的 int

# 創建一個 100x100 的黑色畫布
canvas = np.zeros((100, 100, 3), dtype=np.uint8)

# 在畫布上畫一條線
cv2.line(canvas, (10, 10), (90, 90), color, 2)

# 顯示圖片
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()