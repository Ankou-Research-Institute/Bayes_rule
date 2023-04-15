# -*- coding: utf-8 -*-
"""
ファイル名: BayesRulePythonBinomial_v1.py, Royston SellmanによるコードをJames V Stoneが修正
本コードは、"［速習］ベイズの定理 ——「推論」に効く数学の力（原題：A Tutorial Introduction Introduction）（James V Stone著）"に付属するものです。
概要：本ソースコードは、図4.7に記載されたグラフを描くためのものです。
コインの偏りb（表が出る確率）と、コイントスの回数ごとにデータセットxを生成し、xにおける表の数nhと裏の数ntをカウントします。
bが取りうる各値において、xが発生する確率を計算し、これにより尤度関数を求めます。
尤度関数の各値を、それと対応する事前分布の値と掛け合わすことで、事後分布を得ます。
事前分布は、useuniformpriorの値をbooleanもしくはbinominalとすることで、一様分布もしくは二項分布を設定できます。

このソースコードは、downloaded from http://jim-stone.staff.shef.ac.uk/BayesBook/Pythonからダウンロードできます。
また、Python 2.7と互換性があります。
Copyright: 2014, JV Stone, Psychology Department, Sheffield University, Sheffield, England.
日時: 12 January 2014.
"""
# 必要なモジュールのインポート
import numpy as np
import matplotlib.pyplot as plt


plt.close("all")
plt.rcParams.update({'font.size': 12})
# plt.ion()
# 乱数シードの設定
np.random.seed(99)

# コインの偏りが取りうる値をベクトルとして設定（偏りは、すなわち表が出る確率）
tiny = 1e-12
b = np.linspace(0, 1, 1000) # 偏りの値のベクトルを生成
a = 1-b                     # 裏が出る確率のベクトルを生成

# 一様分布と二項分布のどちらかの事前分布を選択
useuniformprior = 1
if useuniformprior: 
    prior=b**0        # 一様分布の事前分布を生成
else: 
    prior=b**2 * a**2 # 二項分布の事前分布を生成

# 各データセットxの元となるデータx0を生成
coinbias=0.6
ni = 10
NN = 2**ni # コイントスの最大回数NNを設定
# flipoutcomes = np.random.rand(NN); #（この行は不要であるためコメントアウト）
x0 = np.random.rand(NN,1) < coinbias    # NN個の乱数を生成し、coinbias未満である要素をFalse、coinbias以上である要素をTrueとした配列x0を生成（コイントスに相当）
x0[0]=1; x0[1]=0; x0[2]=1; x0[3]=1      # 配列x0の冒頭の箇所を書き換える
x0=x0.astype(int)                       # bool値を0, 1に変換

# 尤度と事後分布をコイントスの回数ごとに求める
# コイントスの回数ごとにサブプロットを作成
fig1 = plt.figure(1,(10,16)) 
for i in range(0, ni):  # コイントスの回数を2のべき乗に従って増やす
    N = 2**i            # コイントスの回数を取得
    x = x0[0:N]         # x0の最初のN回の結果xを取得 
    k = sum(x)          # xにおける面の回数を取得
    nh = k              # nh = 表の出た数
    nt = N-k            # nt = 裏の出た数
    #  尤度 = （コインの偏りがbである場合に）nh回表が出て、nt回裏が出る確率
    lik = b**nh * a**nt
    p = lik*prior       # 事後分布を求める
    maxp = max(p)       # 事後分布pの最大値を求める
    p = p/maxp          # 最大値pを1として表示するように事後分布を正規化する
    ind = p.argmax()    # 最大値pをとるインデックスを取得
    best = b[ind]       # 偏りのMAP推定値
    #  事後分布を描画
    fig2 = plt.subplot(ni/2,2,i+1) 
    plt.plot(b,p) 
    plt.xlabel("Coin Bias, $\\theta$")  
    plt.ylabel("Posterior $p(\\theta|x)$")
    plt.ylim((0,1.1)) 
    plt.text(0.05, 0.9, 'Num flipoutcomes = ' + str(N))
    plt.text(0.05, 0.8, 'Num heads = ' + str(nh))
    plt.text(0.05, 0.7, 'Bias est = '+'%(num)1.3f'% {"num" : best})
plt.show()
