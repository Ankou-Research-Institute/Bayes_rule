# 式1.26
pSpotsGSmallpox = 0.9 #p(x|θs)
pSmallpox = 0.001 #p(θs)
pSpotsGChickenpox = 0.8 #p(x|θc)
pChickenpox = 0.1 #p(θc)
Rpost = pSpotsGChickenpox*pChickenpox / (pSpotsGSmallpox*pSmallpox)
print('Rpost = %.3f.' % Rpost)

# 出力:   Rpost = 88.9