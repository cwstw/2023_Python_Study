'''
Created on 2023. 7. 19.

@author: user
'''
import pandas as pd
import numpy as np

#기호로 구분된 대용량 csv 읽어오기
mycolumn = ['집계일자', '집계시', '영업소코드', '입출구구분코드',
            'TCS하이패스구분코드', '1종교통량', '2종교통량',
            '3종교통량', '4종교통량', '5종교통량', '6종교통량', '총교통량', 'Noname']
filename = 'capital_area.csv'
#쉼표 구분이 아니면 보통 table 사용
#names=mycolumn :인덱스 지정
df = pd.read_table(filename,sep='|',names=mycolumn)
print('df:\n',df)
# df:
#             집계일자  집계시  영업소코드  입출구구분코드  ...  5종교통량  6종교통량  총교통량  Noname
# 0      20170201    0    101        0  ...      4      1   441     NaN
# 1      20170201    0    101        0  ...     43     55  1370     NaN
# 2      20170201    0    101        1  ...      8     24   489     NaN
# 3      20170201    0    101        1  ...     48     38  1282     NaN
# 4      20170201    0    190        0  ...      4      2   149     NaN
# ...         ...  ...    ...      ...  ...    ...    ...   ...     ...
# 15931  20170228   23    253        1  ...     51     76  1787     NaN
# 15932  20170228   23    254        0  ...      3      5   221     NaN
# 15933  20170228   23    254        0  ...     42     50   932     NaN
# 15934  20170228   23    254        1  ...      4     33   323     NaN
# 15935  20170228   23    254        1  ...     13     56   993     NaN
#
# [15936 rows x 13 columns]
print()

#영업소코드 칼럼 가져오기
print(df['영업소코드'])
print(type(df['영업소코드'])) #pandas.core.series.Series
print()

print(df[['영업소코드']])
print(type(df[['영업소코드']])) #pandas.core.frame.DataFrame
print()

print(df[['영업소코드', '총교통량', '1종교통량']])
print()

#코드가 같은 것끼리 합계구하기
mygroup = df.groupby('영업소코드')
print('mygroup:\n',mygroup)
result = mygroup.sum()
print(result)
#               집계일자    집계시  입출구구분코드  ...   6종교통량     총교통량  Noname
# 영업소코드                               ...                         
# 101    54217536576  30912     1344  ...  236974  5817454     0.0
# 190    54217536576  30912     1344  ...  150397  3701132     0.0
# 253    54217536576  30912     1344  ...  259845  5235574     0.0
# 254    54217536576  30912     1344  ...  140641  2675218     0.0
# 651    52281194688  29808     1296  ...   91917  1715680     0.0
# 685    52281194688  29808     1296  ...   67398  1580989     0.0
#
# [6 rows x 12 columns]
print(len(mygroup)) #6 그룹으로 묶인 개수
print()

#그룹에서 총교통량의 합계만 출력
print(mygroup['총교통량'].sum())
print(mygroup['총교통량'].apply(np.sum))
print(type(mygroup['총교통량'].apply(np.sum))) #pandas.core.series.Series
print()

#데이터프레임 형태로 출력
print(mygroup[['총교통량']].apply(np.sum))
print(mygroup[['총교통량','2종교통량']].apply(np.sum))
print()

#영업소코드가 190인 행 가져오기
print(df[df['영업소코드'] == 190])
print()

#전체 데이터에서 1종 교통량 최대값, 최소값
print(df[['1종교통량']].apply(np.max))
print(df[['1종교통량']].apply(np.min))

#그룹의 최대값, 최소값
# print(mygroup[['1종교통량']].apply(np.max))
# print(mygroup[['1종교통량']].apply(np.min))

#apply를 통해 출력하려고 하니 출력은 되는데 오류가 발생,
#max와 min 함수가 있으니 그걸 사용하라고 한다.
print(mygroup[['1종교통량']].max())
print()
print(mygroup[['1종교통량']].min())
print()






