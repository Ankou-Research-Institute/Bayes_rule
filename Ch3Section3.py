# ベイズの定理を用いて事後分布を推定
# 表3.1のデータは転置され、pythonコードから各要素にアクセスできる
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from sys import exit

# NumPy配列の表示形式を設定
np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

# 表3.1のデータを作成（ここでは転置している）
n = np.array([ 
[8,     9,     9,     5,     4,     1,     1,     0,     0,     0],
[3,     5,     8,     9,    14,    10,     3,     3,     0,     0],
[0,     1,     1,    10,    16,    11,    12,     7,     8,     5],
[0,     0,     1,     0,     3,     5,    10,     7,     7,     4]
])
 

N = np.sum(n)                       # 全患者数を取得
ps = n/N                            # 患者数を割合に変換
nTHETA = np.sum(n,axis=0)           # 各列の和を取る

# 尤度関数を求める
nx3ANDTHETA = n[2,:]               # x=3における患者数を取得
px3GTHETA = nx3ANDTHETA/nTHETA     # 尤度p(x=3|theta).
print("Likelihood function:")
print(px3GTHETA)

# 事前分布を取得
pTHETA = nTHETA/N                  # 事前分布
print("Prior distribution:")
print(pTHETA)

# 事後分布を求める
nx3 = np.sum(n[2,:])                # Number of counts in row x=3.
px3 = nx3/N                         # Marginal probability p(x3)
pTHETAGx3 = px3GTHETA*pTHETA/px3    # Bayes Rule=>Posterior distn.
print("Posterior distribution:")
print(pTHETAGx3)

# 出力:
# 尤度関数:
# [0.000 0.067 0.053 0.417 0.432 0.407 0.462 0.412 0.533 0.556]
# 事前分布:
# [0.055 0.075 0.095 0.120 0.185 0.135 0.130 0.085 0.075 0.045]
# 事後分布:
# [0.000 0.014 0.014 0.141 0.225 0.155 0.169 0.099 0.113 0.070]