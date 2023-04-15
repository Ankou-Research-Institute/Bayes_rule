# 患者に症状x3が現れ、かつ病気θ2に感染している確率
# 表3.1のデータは転置され、pythonコードから各要素にアクセスできる
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from sys import exit

# NumPy配列の表示形式を設定
np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

plt.close("all")
plt.rcParams.update({'font.size': 22})

# 表3.1のデータを作成（ここでは転置している）
n = np.array([ 
[8,     9,     9,     5,     4,     1,     1,     0,     0,     0],
[3,     5,     8,     9,    14,    10,     3,     3,     0,     0],
[0,     1,     1,    10,    16,    11,    12,     7,     8,     5],
[0,     0,     1,     0,     3,     5,    10,     7,     7,     4]
])
 

N = np.sum(n)                       # 全患者数を取得
ps = n/N                            # 割合に変換
nTHETA = np.sum(n,axis=0)   

# グラフのパラメータを設定
width = 0.2                 
theta_values = range(1,11)

# 尤度関数を求める
nx3ANDTHETA = n[2,:]               # 表3.1のx=3における値を取得
px3GTHETA = nx3ANDTHETA/nTHETA     # 尤度 p(x=3|θ).
# 尤度関数を描画
plt.figure("Figure 7a")
plt.bar(theta_values, px3GTHETA, width=width,align='center')
plt.xticks(theta_values, theta_values)
#  図の左右にスペースを追加
plt.xlim([min(theta_values)-0.5, max(theta_values)+0.5]) 
plt.xlabel("Outcome value")
plt.ylabel("Likelihood, $p(x_3|\\theta)$")

# 事前分布を取得
pTHETA = nTHETA/N                  # 事前分布
# 事前分布を描画
plt.figure("Figure 7b")
plt.bar(theta_values, pTHETA, width=width,align='center')
plt.xticks(theta_values, theta_values)
plt.xlim([min(theta_values)-0.5, max(theta_values)+0.5]) 
plt.xlabel("Outcome value")
plt.ylabel("Prior, $p(\\theta)$")

# 事後分布を求める
nx3 = np.sum(n[2,:])                # x=3行の値の和
px3 = nx3/N                         # 周辺確率p(x3)
pTHETAGx3 = px3GTHETA*pTHETA/px3    # 事後分布
# 事後分布を描画
plt.figure("Figure 7c")
plt.bar(theta_values, pTHETAGx3, width=width,align='center')
plt.xticks(theta_values, theta_values)
plt.xlim([min(theta_values)-0.5, max(theta_values)+0.5]) 
plt.xlabel("Outcome value")
plt.ylabel("Posterior, $p(\\theta|x)$")
plt.show()

exit(0) #

ptheta2Gx3 = n[2,1]/nx3
print 'Prob x=3 given theta=2 is %.3f.' % ptheta2Gx3

# 出力: 
# x=3行の値の和は71
# θ=2の場合にx=3である確率は0.014


px3ANDtheta2 = ps[2,1];
px3Gtheta2 = px3ANDtheta2/ptheta2;

print 'Prob x=3 AND theta=2 is %.3f.' % px3ANDtheta2
print 'Prob x=3 given theta=2 is %.3f.' % px3Gtheta2

# 尤度関数を求める
px3GTHETA = nx3ANDTHETA/nTHETA

print 'Likelihood function p(x3|THETA) = '
print px3GTHETA
# 出力: 
# x=3かつθ=2である確率は0.005
# θ=2の場合にx=3である確率は0.067
# 尤度関数 p(x3|THETA) = 
# [0.000 0.067 0.053 0.417 0.432 0.407 0.462 0.412 0.533 0.556]


exit(0) #