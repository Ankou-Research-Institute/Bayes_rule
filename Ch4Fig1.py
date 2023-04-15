import numpy as np
import matplotlib.pyplot as plt

plt.close("all")
plt.rcParams.update({'font.size': 18})
# NumPy配列の表示形式を設定
np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

# θの値をベクトルとして設定
THETA = np.linspace(0.0, 1.0,100)
# 式4.9に基づき尤度関数を求める
pxGTHETA = THETA**7 * (1.0-THETA)**3
# 尤度関数を描画する（図4.1）
plt.figure("Figure 4.1")
plt.plot(THETA,pxGTHETA)
plt.xlabel("Bias, $\\theta$")  
plt.ylabel("Likelihood function $p(x|\\theta)")
plt.show()