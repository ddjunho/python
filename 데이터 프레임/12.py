import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 상자그림
# mpg = pd.read_csv('mpg.csv')
# mpg = mpg.query("category in ['compact','subcompact', 'suv']")
# sns.boxplot(data=mpg, x='category', y='cty')
# plt.show()

# 시계열 차트
# economics = pd.read_csv('economics.csv')
# economics['date2']=pd.to_datetime(economics['date'])
# economics['year']=economics['date2'].dt.year
# sns.lineplot(data=economics, x = 'year', y = 'psavert', ci=None)
# plt.show()
#
# economics['month']=economics['date2'].dt.month
# df_2014 = economics.query('year == 2014')
# sns.lineplot(data=df_2014, x='month', y= 'psavert', ci= None)
# plt.show()
# # 막대 그래프
# mpg = pd.read_csv('mpg.csv')
# mpg_new = mpg.copy()
#
#
# print(mpg_new)
# mpg_new=mpg_new.query('category=="suv"').groupby('manufacturer', as_index=False).agg(mean_cty=('cty','mean')).sort_values('mean_cty',ascending=False).head(5)
# print(mpg_new)
# sns.barplot(data=mpg_new, x='manufacturer', y='mean_cty')
# plt.show()

# df_mpg=mpg.groupby('category', as_index=False).agg(n=('category', 'count')).sort_values('n', ascending=False)
# sns.barplot(data=df_mpg, x='category', y='n')
# plt.show()

# drv별로 cty평균 알아보기
# mpg = pd.read_csv('mpg.csv')
# mpg_new = mpg.copy()
# print(mpg_new.dropna(subset = ['drv','cty']).groupby('drv').agg(mean_cty= ('cty','mean')))

# 이상치 제거 확인
# mpg_new = mpg.copy()
# mpg_new.loc[[1,2,4,5], 'drv'] = 'k'
# mpg_new.loc[[1,3,5,7], 'cty'] = [3,4,39,42]
#
# print(mpg_new['cty'].value_counts())
#
# sns.boxplot(data=mpg_new, y='cty')
# plt.show()
#
# pct25= mpg_new['cty'].quantile(.25)
# pct75= mpg_new['cty'].quantile(.75)
# iqr = pct75 - pct25
# low=pct25 - 1.5 * iqr
# up=pct75 + 1.5 * iqr
#
# mpg_new['cty']= np.where(mpg_new['cty']<low, np.nan, mpg_new['cty'])
# mpg_new['cty']= np.where(mpg_new['cty']>up, np.nan, mpg_new['cty'])
# print(mpg_new['cty'].value_counts())
# sns.boxplot(data=mpg_new, y='cty')
# plt.show()

## 이상치 확인 1
# print(mpg_new['drv'].value_counts())
# mpg_new['drv']= np.where(mpg_new['drv']=='k', np.nan, mpg_new['drv'])
# print(mpg_new['drv'].value_counts())
#1,2
# mpg_new.loc[[2,3,5,7], 'hwy'] = np.nan
# mpg_count=pd.isna(mpg_new['drv']).sum()
# print(mpg_count)
# mpg_count=pd.isna(mpg_new['hwy']).sum()
# print(mpg_count)
# mpg_new['hwy']=mpg_new['hwy'].dropna()
# print(mpg_new['hwy'])
# mpg_new = mpg_new.groupby('drv').agg(mean_hwy = ('hwy','mean'))
# print(mpg_new)