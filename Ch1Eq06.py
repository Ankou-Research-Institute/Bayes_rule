# 式1.6
# 尤度 = 天然痘に感染した条件下で発疹が現れる確率
pSpotsGSmallpox = 0.9
# 事前確率 = 天然痘に感染している確率
pSmallpox = 0.001
# 周辺尤度 = 発疹が現れる確率
pSpots = 0.081
# 事後確率 = 発疹が現れた場合に、天然痘に感染している確率
pSmallpoxGSpots = pSpotsGSmallpox * pSmallpox / pSpots

print('Posterior, pSmallpoxGSpots = %.3f.' % pSmallpoxGSpots)
# 出力: Posterior, pSmallpoxGSpots = 0.011.