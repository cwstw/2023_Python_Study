'''
Created on 2023. 7. 19.

@author: user
'''
import pandas as pd
import numpy as np

col = ['국어','영어','수학']
idx = ['박보검','홍길동','아이유']
data = [-40,50,50,70,-50,20,20,20,20]

df = pd.DataFrame(np.reshape(data,[3,3]),idx,col)
print('df:\n',df)
# df:
#       국어  영어  수학
# 박보검 -40  50  50
# 홍길동  70 -50  20
# 아이유  20  20  20
print()

#데이터를 절대값으로
df = np.abs(df)
print('df:\n',df)
print()

#데이터프레임의 합계, 칼럼별로 합계 출력
print('np.sum(df):\n',np.sum(df))
print()
print(df.apply(np.sum))
print()
#축을 1로 설정하면 인덱스 기준으로 합계
#대신에 'index', 'columns'입력 가능
print(df.apply(np.sum,axis=1))
print()
print(df.apply(np.sum,axis='columns'))
print()

#칼럼에서 제일 큰 값 출력
print(df.apply(np.max,axis=0))
#인덱스에서 제일 큰 값 출력
print(df.apply(np.max,axis=1))

#람다 함수를 정의하여 출력, 최대값-최소값
print(df.apply(lambda x : x.max() - x.min(), axis=0))
print()

print('df:\n',df)
print()

#없는 칼럼 추가
df.loc['김연아'] =[11,22,33]
print('df:\n',df)
print()

#인덱스 정렬
print(df.sort_index())
print()

#칼럼 정렬
print(df.sort_index(axis=1,ascending=False))
print()

#데이터 정렬, 기준으로 할 컬럼을 필수로 하나 이상 넣어준다.
#기준 컬럼을 하나 이상 작성 시 []로 묶어준다.
#정렬도 각각 적용 시 []로 묶어 작성
print(df.sort_values(by=['영어','수학'],ascending=[False,True]))
print()

filename = 'df_ex.csv'
df.to_csv(filename,encoding='euc-kr',mode='w')
print(filename+'에 저장됨.')

dfex = pd.read_csv(filename,encoding='euc_kr',index_col=0)
print()
print('dfex:\n',dfex)







