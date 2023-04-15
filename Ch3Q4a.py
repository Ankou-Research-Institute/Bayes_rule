# 患者に症状x3が現れ、かつ病気θ2に感染している確率
# 表3.1のデータは転置され、pythonコードから各要素にアクセスできる
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
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
nx3theta2 = n[3,2]          # 3行目2列目の患者数
ntheta2 = np.sum(n[:,1]);   # 2列目の患者数の和
ptheta2 = ntheta2/N;        # 2列目の患者数の割合
pTHETA = 1.0*np.sum(n,axis=0)/N # 周辺分布

print 'Number of counts in col 2 is %d.' % ntheta2
print 'Proportion of counts in col 2 is %.3f.' % ptheta2
print 'Marignal distribution p(THETA)'
print pTHETA
# 2列目の患者数の和は15
# 2列目の患者の割合は0.075.
# 周辺分布 p(THETA)
# [0.055 0.075 0.095 0.12 0.185 0.135 0.13 0.085 0.075 0.045]