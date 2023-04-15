# 式1.9
# 尤度 = 水疱瘡に感染した条件下で発疹が現れる確率
pSpotsGChickenpox = 0.8
# 事前確率 = 天然痘に感染している確率
pChickenpox = 0.1
# 周辺尤度 = 発疹が現れる確率
pSpots = 0.081
# 事後確率 = 発疹が現れた場合に、水疱瘡に感染している確率
pChickenpoxGSpots = pSpotsGChickenpox * pChickenpox / pSpots
print('Posterior, pChickenpoxGSpots = %.3f.' % pChickenpoxGSpots)

# 出力:   Posterior, pChickenpoxGSpots = 0.988.
