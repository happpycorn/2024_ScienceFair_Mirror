import matplotlib.pyplot as plt
import numpy as np

# 開啟交互模式
plt.ion()

# 創建圖形和軸
fig, ax = plt.subplots()
x = np.linspace(0, 10, 100)
line, = ax.plot(x, np.sin(x))

# 動態更新圖形
for i in range(100):
    line.set_ydata(np.sin(x + i / 10))  # 更新y數據
    plt.draw()  # 重新繪製圖形
    plt.pause(0.1)  # 暫停，控制更新頻率

# 關閉交互模式
plt.ioff()
plt.show()
