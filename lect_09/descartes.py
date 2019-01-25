"""
    功能：笛卡儿积心形线
"""
import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(-2 * np.pi, 2 * np.pi, 1024)
x = 1*(2 * np.sin(a)-np.sin(2 * a))
y = 1*(2 * np.cos(a)-np.cos(2 * a))
plt.title("Heart")
plt.plot(x, y, "r")
plt.show()