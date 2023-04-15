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


N = np.sum(n)           # 全患者数を取得
row3 = n[2,:]           # 3行目の患者数を取得
nx3=sum(row3)           # 3行目の患者数の和
px3 = nx3/N             # 3行目の患者数を割合に変換
X = np.sum(n,axis=1)/N  # 周辺分布

print ('Number of counts in row 3 is %d.' % nx3)
print('Proportion of counts in row 3 is %.3f.' % px3)
print('Marignal distribution p(X) ')
print(X)
# 出力: 3行目の患者数の和は71
# 3行目の患者数が占める割合は0.355
# 周辺分布p(X) [ 0.185  0.275  0.355  0.185]


