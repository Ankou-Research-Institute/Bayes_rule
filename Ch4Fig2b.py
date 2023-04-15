import numpy as np
import matplotlib.pyplot as plt

plt.close("all")
plt.rcParams.update({'font.size': 18})
# Numpy配列の表示形式を設定
np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

# θの値をベクトルとして設定
THETA = np.linspace(0.0, 1.0,100)
# 式4.14に基づき事前分布を求める
pTHETA = THETA**2 * (1.0-THETA)**2
# 事前分布を描画する（図4.2b）
plt.figure("Figure 4.2b")
plt.plot(THETA,pTHETA)
plt.xlabel("Bias, $\\theta$")  
plt.ylabel("Prior probability density $p(\\theta)$")
plt.show()