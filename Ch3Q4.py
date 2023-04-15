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
 

N = np.sum(n)               # 全患者数を取得
ps = n/N                    # 患者数を割合に変換
ntheta2 = np.sum(n[:,1]);   # 2列目の患者数の和
ptheta2 = ntheta2/N         # 2列目の患者数の割合

px3ANDtheta2 = ps[2,1]
px3Gtheta2 = px3ANDtheta2/ptheta2

print('Prob x=3 AND theta=2 is %.3f.' % px3ANDtheta2)
print('Prob x=3 given theta=2 is %.3f.' % px3Gtheta2)

# 尤度関数を求める
nx3ANDTHETA = n[2,:]           # 3行目の患者数の和
nTHETA = np.sum(n,axis=0)     
px3GTHETA = nx3ANDTHETA/nTHETA # 周辺分布

print( 'Likelihood function p(x3|THETA) = ')
print(px3GTHETA)
# 出力: 
# x=3かつθ = 2である確率は0.005
# θ=2の場合にx=3である確率は0.067
# 尤度関数p(x3|THETA) = 
# [0.000 0.067 0.053 0.417 0.432 0.407 0.462 0.412 0.533 0.556]