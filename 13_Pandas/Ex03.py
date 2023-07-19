'''
Created on 2023. 7. 19.

@author: user
'''
import pandas as pd
import numpy as np

d = {'Korea':{'capital':'서울','population':23232332}, 'China':{'capital':'베이징','population':3434345}, 'Singapore':{'capital':'싱가포르','population':3465474}, 'Vietnam':{'capital':'하노이','population':34234234}}

df = pd.DataFrame(d)
print('df:\n',df)

# print(df['pop'][2])
print(df.columns)
print(df.index)
#print(df.data)
print(df.values)

mycolumns = ['도시', 'year', 'pop', 'income']
myindex = ['one', 'two', 'three', 'four','five']

df2 = pd.DataFrame(d,myindex,mycolumns)
print('df2:\n',df2)
print()

#도시 칼럼의 값이 인덱스와 함께 출력
print(df2['도시'])
print(type(df2['도시'])) #시리즈
print()

#.으로 접근 가능
print(df2.year)
print(type(df2.year)) #시리즈
print()

#다중 조회
print(df2[['도시','year']])
print(type(df2[['도시','year']])) #데이터 프레임
print()

#칼럼에 값 넣기, 모두 같은 값으로 변경
df2['income'] = 12.34
print(df2)
print()

#칼럼에 값 넣기, 모두 각각의 값으로 변경
df2['income'] = [10,20,30,40,50]
print(df2)
print()


s = pd.Series([100,200,300],
              index=['two','four','five'])
print('s:\n',s)
print()

#칼럼에 시리즈를 삽입, 인덱스가 일치하는 칼럼에만 값이 삽입된다.
#나머지는 NaN 출력
df2['income'] = s
print(df2)

#행열 변경
print(df2.T)
print()
print(df2.transpose())
print()
print(np.transpose(df2))
print()


idx = ['one','two','three','four']
col = ['서울','부산','광주','대구']
df = pd.DataFrame(np.arange(16).reshape([4,4]),idx,col)
print('df:\n',df)
print()

#칼럼은 지정하여 출력 가능
print(df[['서울','대구']])
print()

#인덱스는 reindex 함수를 이용하여 출력
#print(df[['two','four']])
print(df.reindex(['two','four']))
print()

#없는 인덱스로 가져오면 NaN 출력,
#columns로 명시하면 출력할 수 있다.
#print(df.reindex(['서울','대구']))
print(df.reindex(columns=['서울','대구']))
print()

#인덱스와 컬럼 모두 지정 출력 가능
print(df.reindex(columns=['부산','광주'],
                 index=['one','three']))
print()

#삭제해서 출력
df2 = df.drop(['two','four'])
print('df2:\n',df2)
print()

#칼럼에서 삭제할 때는 axis=1 꼭 명시
df2 = df.drop(['서울','부산'],axis=1)
print('df2:\n',df2)
print()

#칼럼과 인덱스 모두 삭제
df2 = df.drop(['서울','부산'],axis=1).drop(['two','four'])
print('df2:\n',df2)
print()









