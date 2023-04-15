import numpy as np
import matplotlib.pyplot as plt
from sys import exit

plt.close("all")
plt.rcParams.update({'font.size': 18})
# NumPy配列の表示形式を設定
np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
# θの値をベクトルとして設定
THETA = np.linspace(0.0, 1.0,100)

# 式4.17に記載の事後分布を求める
pTHETAGx = THETA**9 * (1.0-THETA)**5
# グラフ描画のため、１を最大値に設定する
pTHETAGx = pTHETAGx/max(pTHETAGx)
# 事後分布を描画する（図4.3c）
plt.figure("Figure 4.3c")
plt.plot(THETA,pTHETAGx)
plt.xlabel("Coin bias, $\\theta$")  
plt.ylabel("Posterior probability density $p(\\theta|x)$")

# 式4.9に基づき尤度関数を求める
pxGTHETA = THETA**7 * (1.0-THETA)**3
# グラフ描画のため、１を最大値に設定する
pxGTHETA = pxGTHETA/max(pxGTHETA)
# 比較のため、尤度関数を描画する
plt.plot(THETA,pxGTHETA,'r--')
plt.ylim([0, 1.1]) 
plt.show()
exit
