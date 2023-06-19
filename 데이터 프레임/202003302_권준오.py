import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

s_trans = pd.read_csv('seoul_public_transport.csv',encoding='cp949')
#
s_trans_mean = s_trans['총_승객수_일반'].mean()

s_trans_not_good=s_trans.assign(혼잡도 = np.where(s_trans['총_승객수_일반']>s_trans_mean,'혼잡','여유'))
print(s_trans_not_good)
count_not_good=s_trans_not_good['혼잡도'].value_counts().plot.bar(rot=0)
plt.show()