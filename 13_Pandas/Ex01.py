'''
Created on 2023. 7. 19.

@author: user
'''
import pandas as pd
import numpy as np

arr = np.array([10,40,30,20])
print('arr:',arr)
print(type(arr)) #numpy.ndarray
print()

#pandas Series
#1차원 배열과 같은 자료구조, 인덱스와 값으로 구성
s1 = pd.Series([10,40,30,20])
print('s1:\n',s1)
print(type(s1)) #pandas.core.series.Series
print(s1.ndim,s1.shape) #1 (4,)
print(s1.index) #RangeIndex(start=0, stop=4, step=1)
print(s1.values) #[10 40 30 20]
print(s1[1]) #40
print()

#인덱스를 사용자 지정 가능, index = 은 생략 가능
s2 = pd.Series([10,40,30,20],index=['윤아','슬기','조이','웬디'])
print('s2:\n',s2)
print(s2.index) #Index(['윤아', '술기', '조이', '웬디'], dtype='object')
print(s2.values) #[10 40 30 20]

#시리즈를 인덱스로 출력
print(s2['슬기'])
print(s2[['슬기']])

#시리즈를 번호로 출력
print(s2[1])
print(s2[[1]])

#없는 인덱스에 값을 저장하면 인덱스와 값이 추가된다.
s2['서현'] = 70
s2['슬기'] = 50
print('s2:\n',s2)

#시리즈를 인덱스로 다중 조회, 괄호를 두번 감싸준다.
#print(s2['슬기','웬디'])
print(s2[['슬기','웬디']])
print()

#시리즈를 번호로 다중 조회, 마찬가지로 괄호 두번 사용
#print(s2[1])
print(s2[[1,2]])

#조건을 설정하여 True False 출력
print(s2.values < 50)
#조건을 설정하여 True에 해당하는 값 출력
print(s2[s2.values < 50])
print()

#인덱스가 조건에 맞는 것만 출력
print(s2[s2.index == '웬디'])
print()

#모든 값에 *2 연산
print(s2*2)
print()

#인덱스가 해당 시리즈에 있으면 True, 없으면 False
print('서현' in s2)
print('현아' in s2)

print('======================')

#사전과 시리즈
d = {"서울":2000, "부산":3000, "울산":4000, "광주":5000}
print(type(d))
print()

#사전을 시리즈로 저장
s3 = pd.Series(d)
print('s3:\n',s3)
print()

#사전을 시리즈로 넣고 인덱스를 따로 지정
#인덱스에 맞는 값들은 해당 인덱스에 배치
#인덱스에 해당하는 값이 없으면 NaN 출력
#값 중에 하나라도 NaN이 있으면 나머지 값도 실수로 바뀐다.
city = ['부산','울산','목포','서울']
s4 = pd.Series(d,city)
print('s4:\n',s4)
print()

#값이 NaN이면 True로 출력
print(pd.isna(s4))
print()
print(pd.isnull(s4))
print()

#값이 NaN인 것만 출력
print(s4[pd.isna(s4)])
print()
print(s4[pd.isnull(s4)])
print()

#값이 NaN이 아닌 것만 출력
print(s4[pd.notna(s4)])
print()
print(s4[pd.notnull(s4)])
print()
print(s4[pd.isna(s4) == False])
print()
print(s4[pd.isnull(s4) == False])
print()

print('s4:\n',s4)
print()

#Nan을 임의로 넣고 싶으면 넘파이 모듈 이용
s5 = pd.Series([5,6,np.NaN])
print('s5:\n',s5)
print()

#시리즈끼리의 연산 시 한쪽이라도 NaN이면 NaN으로 출력
city = ['부산','대구','울산','목포','서울']
s6 = pd.Series([5,6,np.NaN,1,2],city)
print('s6:\n',s6)
print(s4+s6)
print()


print('s2:\n',s2)
print()

#인덱스 삭제, 원본 시리즈는 변화 없음
s7 = s2.drop(['슬기','서현'])
print('s7:\n',s7)
print()

#범위를 설정하여 저장
s7 = s2[1:4]
print('s7:\n',s7)
print()

#범위를 설정하여 뒤에서 부터 저장
s7 = s2[4:1:-1]
print('s7:\n',s7)
print()

#인덱스로 범위 지정, 웬디 포함
s7 = s2['슬기':'웬디']
print('s7:\n',s7)
print()

s7 = s2['웬디':'슬기':-1]
print('s7:\n',s7)
print()


print('s2:\n',s2)
print()

#시리즈에 넘파이 함수 사용
#시리즈 값 중 최대 최소값 출력
print(np.max(s2))
print(np.min(s2))
#시리즈 값들의 합계 출력
print(np.sum(s2))

#인덱스 가나다순으로 정렬
s8 = s2.sort_index()
print('s8:\n',s8)
print()

#값 가나다순으로 정렬
#오름차순을 False로 설정 시 내림차순 정렬
s8 = s2.sort_values(ascending=False)
print('s8:\n',s8)
print()

#NaN을 빼고 출력
print('s4:\n',s4)
print(s4.dropna())
print()












