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


N = np.sum(n)              # 全患者数を取得
nx3theta2 = n[3,2]         # 3行目2列目の患者数
px3theta2 = nx3theta2/N    # 3行目2列目の患者の割合

print('Number of counts in n(3,2) is %d.' % nx3theta2)
print('Proportion of counts in p(3,2) is %.3f.' % px3theta2)

# Output: 患者数 n(3,2)は1
#         患者の割合p(3,2)は0.005
