import numpy as np
import matplotlib.pyplot as plt
from sys import exit

plt.close("all")
plt.rcParams.update({'font.size': 18})
#plt.ion()

# NumPy配列の表示形式を設定
np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

np.random.seed(991)

# θの値をベクトルとして設定
THETA = np.linspace(0.0, 1.0,100)
coinbias = 0.6
q = 1-THETA                             # p(裏)の値
NN = 2**10                              # コイントスの最大回数NNを設定
x0 = np.random.rand(NN,1) < coinbias     # NN回コイントスを行う
x0[0]=1; x0[1]=0; x0[2]=1; x0[3]=1;     # 説明のため、最初の3回分のコイントス結果を変更する
x0=x0.astype(int)                     # True/Falseを0, 1に変更する

for i in range(0,11):
    N = 2**i
    x = x0[0:N]
    k = np.sum(x);           # 表が観測される数
    p = THETA**k * q**(N-k); # k回表が出て、Nーk回裏が出る確率
    maxp = np.max(p);          #  確率pの最大値を求める
    p=p/maxp;                   # グラフ描画のため、最大値が１となるように調整
    plt.figure()
    plt.plot(THETA,p,'k')
    plt.xlabel("Coin Bias, $\\theta$")  
    plt.ylabel("Posterior probability density $p(\\theta|x)$")
    s = "Coin flips = %d" % N
    plt.text(0.2, 0.9,s, ha='center', va='center')
    plt.ylim([0, 1.1]); plt.pause(0.0001)
    plt.show()
    
exit(0)
