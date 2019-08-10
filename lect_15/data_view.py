# 用来可视化身高和体重的数据

#用来可视化身高和体重的数据
import numpy as np
# 用来可视化身高和体重的数据
import matplotlib.pyplot as plt

data = np.array([[152, 51], [156, 53], [160, 54], [164, 55], [168, 57],
                 [172, 60], [176, 62], [180, 65], [184, 69], [188, 72]])

#打印出数据的大小
print(data.shape)

#从data中提取出身高和体重，分别存放在x，y变量中
x, y = data[:, 0].reshape(-1, 1), data[:, 1]

# 在二维空间里面画出身高和体重的分布图
plt.scatter(x, y, color="black")
plt.xlabel('height(cm)')
plt.ylabel('weight(kg)')
plt.show()