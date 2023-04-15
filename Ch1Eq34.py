# 式1.34
pData = 0.61 #p(データ)
pDataGFourCandles = 0.6 #p(データ|フォー・キャンドル)
pFourCandles = 0.9 #p(フォー・キャンドル)
pFourCandlesGData = pDataGFourCandles * pFourCandles / pData
print 'pFourCandlesGData = %.3f' % pFourCandlesGData # p(フォー・キャンドル|データ)
     
pDataGForkHandles = 0.7 #p(データ|フォークハンドル)
pForkHandles = 0.1 #p(フォークハンドル)
pForkHandlesGData = pDataGForkHandles * pForkHandles / pData #p(フォークハンドル|データ)
print 'pForkHandlesGData = %.3f\n' % pForkHandlesGData # p(fork handles|data)

# 出力:   pFourCandlesGData = 0.885
#           pForkHandlesGData = 0.115