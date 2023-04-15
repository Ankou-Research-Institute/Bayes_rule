# ライブラリのインポート
from numpy import arange, linspace, ones, linalg, zeros, amin, amax, exp
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

plt.close("all")
plt.rcParams.update({'font.size': 12})
#plt.ion()

# 事前分布 p(THETA)を生成
# xに関して尤度関数を求める
# さらに、同時分布p(X, THETA)および事後分布p(THETA|X)を求める
imax = 1001; imid = 500.0; 
X = linspace(0,1,imax) 
sdlik = 0.1                   # 尤度の標準偏差
sdprior = 0.1                 # 事前分布の標準偏差
x1_index = round(imax*0.25)       # x=0.75を表す配列のインデックス 
thetatrue_index = round(imax*0.6) # theta=0.6を表す配列のインデックス

# 正規分布の事前分布を生成
prior =  np.exp(-((X-0.5)**2/(2*sdprior**2)))
# 事前分布の描画
ax6 = plt.subplot(426); plt.ylim([0, 1.1])
plt.plot(X,prior);      plt.title("Prior distribution")
plt.ylabel("$p(x)$");   plt.xlabel("$\\theta$")
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax6.get_yticklabels(), visible=False)

likelihoods = zeros((imax,imax)) # 尤度を描画するための2次元配列を用意
prior2d = zeros((imax,imax)) # コピーした事前分布を描画するための２次元配列を用意
# 上記の配列を埋める
for r in arange(0,imax):  
    rfrac = 1.0*(imax-r)/imax
    likelihoods[r,:] = np.exp(-((X-rfrac)**2/(2*sdprior**2)))
    prior2d[r,:] = prior

likelihoods = likelihoods/np.max(likelihoods) 
prior2d = prior2d/np.max(prior2d) # 配列の最大値が1となるように正規化

lik1d = likelihoods[x1_index,:] # X=x1における尤度関数を取得
ax4 = plt.subplot(424);            plt.ylim([0,1.1])
plt.plot(X,lik1d);                 plt.title("Likelihood")
plt.ylabel("$p(x_1|\\theta)$");    plt.xlabel("$\\theta$")
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_yticklabels(), visible=False)

# 同時分布を求める（式3.41 p(X,THETA)=p(X|THETA)*p(THETA)を参照）
joint1 = likelihoods * prior2d;    joint1=joint1/np.max(joint1)

# X=x1における同時分布の断面を取得
joint1d = joint1[x1_index,:];    joint1d = joint1d/np.max(joint1d)
ax2 = plt.subplot(422);          plt.plot(X,joint1d)
plt.title("Joint distribution at $X=x_1$"); plt.ylim([0,1.1])
plt.ylabel("$p(x_1,\\theta)$");  plt.xlabel("$\\theta$")
plt.setp(ax2.get_xticklabels(),visible=False)
plt.setp(ax2.get_yticklabels(),visible=False)

# 周辺尤度p(X)を求める
pX = np.sum(joint1,axis=1)
pX = pX/np.max(pX)

# xの各値において、事後分布を求める
pX_duplicated = zeros((imax,imax))
for r in arange(0,imax):  
    pX_duplicated[:,r]=pX
posteriors = likelihoods * prior2d / pX_duplicated
posteriors = posteriors/np.max(posteriors)

# X=x1における事後分布を取得
posterior = posteriors[x1_index,:]
ax8 = plt.subplot(428);         plt.ylim([0,1.1])           
plt.plot(X,posterior)
plt.title("Posterior distribution")
plt.ylabel("$p(\\theta|x_1)$");    plt.xlabel("$\\theta$")
plt.setp(ax8.get_xticklabels(), visible=False)
plt.setp(ax8.get_yticklabels(), visible=False)

# 2次元分布を画像として表示
lw = 5  # 2次元グラフにおける白線の太さを指定
# 同時分布を表示
# thetatrue_indexにおける全行と、x1_indexにおける全列に白線を引く
Mark all rows at thetatrue_index and columns at x1_index.
joint1[:,thetatrue_index-lw:thetatrue_index+lw]=1
joint1[x1_index-lw:x1_index+lw,:]=1
ax1 = plt.subplot(421);         plt.axis('off')
plt.imshow(joint1,cmap="gray"); plt.title("Joint distribution")

# 尤度関数を表示
plt.subplot(423)
# thetatrue_indexにおける全行と、x1_indexにおける全列に白線を引く
likelihoods[:,thetatrue_index-lw:thetatrue_index+lw]=1
likelihoods[x1_index-lw:x1_index+lw,:]=1
plt.imshow(likelihoods, cmap="gray")
plt.title("Likelihoods");    plt.axis('off')

# 事前分布のコピーを表示
plt.subplot(425);   plt.axis('off')
plt.imshow(prior2d,cmap="gray")
plt.title("Prior distributions")

# 事後分布を表示
plt.subplot(427)
posteriors[:,thetatrue_index-lw:thetatrue_index+lw]=1
posteriors[x1_index-lw:x1_index+lw,:]=1
plt.imshow(posteriors, cmap="gray")
plt.title("Posterior distributions"); plt.axis('off'); 
figManager = plt.get_current_fig_manager()
#figManager.window.showMaximized()
