# 患者に症状x3が現れ、かつ病気x2に感染している確率
# 表3.1のデータは転置され、pythonコードから各要素にアクセスできる

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

fig = plt.figure()
ax = fig.add_subplot(111)
#plt.ion() # インタラクティブな描画を許可

for r in range(0, 4):
    for c in range(0, 10):
        ndots = n[r,c]
        for i in range(0,ndots):
            rr = 0.1+r+0.8*np.random.random()
            cc = 0.1+c+0.8*np.random.random()
            plt.scatter(cc,rr)

plt.ylim([0,4])
plt.xlim([0,10])
ax.yaxis.set_ticks([0,1,2,3,4])
plt.xlabel("$\\theta$")  
plt.ylabel("x")  
plt.grid(True)
plt.show()
# Pythonの配列におけるインデックスは0~N-1の値をとるが、本書における例は
# 1~Nまでのインデックスを想定していることに注意。一貫性を保つため、ここでは変数名
# は1~Nを想定している

