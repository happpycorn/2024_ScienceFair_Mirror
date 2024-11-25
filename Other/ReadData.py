import pandas as pd
import matplotlib.pyplot as plt

# 讀取數據文件
data = pd.read_csv("GoodData\Yellow_Blue.csv")

# 獲取數據列
values = data["Value"].values

plt.ylim(0, 1)
plt.plot(range(len(values)), values)
plt.show()