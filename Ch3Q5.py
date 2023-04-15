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
ntheta2 = np.sum(n[:,1])    # 2列目の患者数の和
ptheta2 = ntheta2/N         # 2列目の患者数の割合
nx3 = np.sum(n[2,:])        # 3行目の患者数の和

print('Number of counts in row x=3 is %d.' % nx3)

ptheta2Gx3 = n[2,1]/nx3
print('Prob θ=2 given x=3 is %.3f.' % ptheta2Gx3)

# 出力: 
# 行3における患者数の和は71
# x=3である場合にθ=2である確率は0.014.

exit #