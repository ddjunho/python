# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# titanic = sns.load_dataset('titanic')
# sns.countplot(data=titanic, x = 'sex')
# plt.show()
import pandas as pd
# df = pd.DataFrame({'name' : ['김지훈', '이유진', '박동현', '김민지'],
# 'eng' : [90, 80, 60, 70],
# 'math' : [50,60,100,20]})
# print(df,"\n")
# print(df['eng'],"\n")
# print(df['math'],"\n")
# print(sum(df['eng'])/4)
# print(sum(df['math'])/len(df['math']))
df_exam1 = pd.read_excel('excel_exam1.xlsx', sheet_name=0)
df_exam2 = pd.read_excel('excel_exam1.xlsx', sheet_name=1)
df_exam3 = pd.read_excel('D:/202003302/데이터 프레임/excel_exam1.xlsx', sheet_name=2)
print(df_exam1,'\n')
print(sum(df_exam1['math'])/len(df_exam1['math']),'\n')
print(df_exam2,'\n')
print(df_exam3,'\n')