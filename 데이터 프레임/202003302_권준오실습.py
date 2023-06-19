import pandas as pd
import numpy as np


midwest = pd.read_csv('midwest.csv')
# 4번

midwest = midwest.assign(ratio_asian = midwest['popasian']/midwest['poptotal']*100)
highest_5 = midwest.sort_values('ratio_asian', ascending=False).head(5)[['state', 'county', 'ratio_asian']]
print(highest_5)

# 3번
# midwest = midwest.assign(ratio = (1-midwest['popadults']/midwest['poptotal'])*100)
# midwest = midwest.assign(grade = np.where(midwest['ratio']>=40, 'large', 'small'))
# grade_counts = midwest['grade'].value_counts()
# print(grade_counts)

# 2번
# midwest = midwest.assign(ratio = (1-midwest['popadults']/midwest['poptotal'])*100).sort_values('ratio',ascending=False).head(7)
# print(midwest)

# 1번
# midwest = midwest.assign(ratio = (1-midwest['popadults']/midwest['poptotal'])*100)
# print(midwest)

#########      mpg.csv예제       ##########
# mpg_new= pd.read_csv('mpg.csv')

# 9번
# fuel = pd.DataFrame({ 'fl' : ['c','d','e','p','r'],
# 'price_fl' : [2.35, 2.38, 2.11, 2.76, 2.22] } )
# mpg = pd.merge(mpg_new,fuel,how='left' ,on='fl')
# print(mpg)

# 8번
# compact_counts = mpg_new[mpg_new['category'] == 'compact']['manufacturer'].value_counts().sort_values(ascending=False)
# print(compact_counts)

# 7번
# mpg_new=mpg_new.groupby('manufacturer').agg(mean_hwy=('hwy','mean')).sort_values('mean_hwy',ascending=False).head(3)
# print(mpg_new)

# 6번
# mpg_new=mpg_new.groupby('category').agg(mean_cty=('cty','mean')).sort_values('mean_cty',ascending=False)
# print(mpg_new)

# 5번
# mpg_new=mpg_new.groupby('category').agg(mean_cty=('cty','mean'))
# print(mpg_new)

# 4번
# mpg_new=mpg_new.assign(total = mpg_new['hwy']+mpg_new['cty'])
# mpg_new=mpg_new.assign(mean = mpg_new['total']/2)
# print(mpg_new)
# print(mpg_new.sort_values('mean',ascending=False).head(3))

# 3번
# mpg=mpg_new.query('manufacturer =="audi"').sort_values('hwy',ascending=False).head(3)
# print(mpg)

# 2번
# mpg=mpg_new.query('category=="suv"')['cty']
# mpg=sum(mpg)/len(mpg)
# print(mpg)
# mpg=mpg_new.query('category=="compact"')['cty'].mean()
# print(mpg)


