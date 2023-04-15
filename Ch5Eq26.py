# -*- coding: utf-8 -*-

##################################################################################
# ファイル名: Regression.py
# 本コードは、"［速習］ベイズの定理 ——「推論」に効く数学の力（原題：A Tutorial Introduction Introduction）（James V Stone著）"に付属するものです。
# JV Stone, 2014.
# Copyright: 2014, JV Stone,  Sheffield University, Sheffield, England.
# 以下のPythonコードはversion 0.1であり、http://jim-stone.staff.shef.ac.uk/BookBayes2012/BayesRuleBookMain.htmlからダウンロードできます。
# このコードはPython 2.76上で動作させる必要があり, Enthough Canopy Version: 1.3.0 (64 bit) 上でテストされました。
# （訳注：Python 3.8での動作を確認しています）
# このコードは、MATLABコードをPythonに移植したものであり、Royston Sellmanによるコメントを残しています。
##################################################################################

# ライブラリのインポート
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from numpy import arange, linspace, random, ones, linalg, zeros, amin, amax, exp
import numpy as np
import matplotlib.pyplot as plt
#import statsmodels.regression.linear_model as sm # 訳注：statsmodels.apiに変更
import statsmodels.api as sm
from sys import exit

plt.close("all")
plt.rcParams.update({'font.size': 18})
#plt.ion()

# 乱数シードを設定
np.random.seed(6)

# 図5.3.
# 傾きmと切片cのモデルに基づきノイズを含んだデータを生成
# 水平軸にプロットする11個の収入を定義
s = arange(1,12)                        
# 傾きmと切片cの値を設定
m = 0.5; c = 3
# 測定した身長それぞれで標準偏差を設定
sds = 2*arange(1,12)/10.0; sds = sds * arange(1,12)/10.0       
# 本書で使用したノイズの大きさ（なお、この値は上記の標準偏差に基づき推定したもの）
eta=[-0.0023,-0.0728,0.1104,0.6076,-0.3034,-0.2237,0.7407,
-1.0,-3.0,-2.4653,-3.0]
# ノイズを含むxの観測値
x = m*s + c + eta

# 重み付き最小二乗回帰
# 各データ点に対して重み（ディスカウント）を求める
vars0 = sds ** 2; w = 1/vars0       
# 重みづけをしない場合は次の行のコメントを外す
#w=ones(size(w)) 
ss = sm.add_constant(s) # Add column of 1s for regression.   
model = sm.WLS(x,ss, weights=w)       
results = model.fit()
cest2, mest2 = results.params
print('Estimated slope = %.3f,' % mest2)
print(' estimated intercept = %.3f.' % cest2)

# 回帰の結果求められた傾きと切片の値に基づいて回帰直線xestを生成
s2 = arange(0,13)
xest2 = mest2 * s2 + cest2               

# 回帰直線xest、データ点、エラーバーを描画
fig1 = plt.figure() 
plt.errorbar(s, x, yerr=sds, fmt='o',color='k')
plt.plot(s,x, 'k*', s2, xest2, 'k--')
plt.xlabel('Salary, $s$ (groats)')
plt.ylabel('Height, $x$ (feet)')
plt.xlim((0,12)); plt.ylim((0,9))
# 出力: 
#    Estimated slope = 0.479. 
#    Estimated intercept = 3.019.

# 図5.4aの二次元グラフを描画
# （ここまでに記載したコードの変数値を利用）
m = mest2; mmin = mest2-1; mmax = mest2+1
c = cest2; cmin = cest2-1; cmax = cest2+1
minc = (mmax-mmin)/100
cinc = (cmax-cmin)/100

Fs = []
ms = linspace(mmin, mmax, 100);    nm = len(ms)
cs = linspace(cmin, cmax, 100);    nc = len(cs)
Farray = zeros((nm,nc))
for m1 in arange(0,nm):                 
    for c1 in arange(0, nc):            
        mval=ms[m1]
        cval=cs[c1]
        y1 = mval*s + cval
        F1 = ((x-y1)/sds) ** 2
        Farray[m1,c1] = sum(F1)
        Fs = (Fs, F1)

fig2 = plt.figure()
Z1 = Farray.T
zmin = amin(Z1); zmax = amax(Z1)                         
zrange = zmax - zmin 
v = arange(zmin, zmax, zrange / 10)     
# 等高線の間隔を調整
v = arange(0, 9 ,0.5)
v = exp(v)
v = v * zrange/max(v);
X, Y = np.meshgrid(ms,cs)               
plt.xlabel('Slope, $m$') 
plt.ylabel('Intercept, $c$')
plt.contour(X, Y, Z1, v)
plt.show()

# 図5.4bの二次元グラフを描画
fig3 = plt.figure()
ax = fig3.add_subplot(111, projection='3d')
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(2,4)
ax.set_zlim(min(v), max(v))
ax.autoscale(enable=True, axis='z')
ax.set_xlabel('$m$'); ax.set_ylabel('$c$'); ax.set_zlabel('$F$')
surf = ax.plot_surface(X,Y,Z1,rstride=1,cstride=1,
cmap = cm.coolwarm,linewidth=0,antialiased=True)
plt.show()
# 出力: 
#    Estimated slope = 0.479. 
#    Estimated intercept = 3.019.