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


s  = pd.Series(['A','B','C','D','E','F','G'],
               index=[49,48,47,46,2,3,4])
print('s:\n',s)
print()

#인덱스로 조회
print(s[3])
print(s[47])
print(s.loc[3])
print(s.loc[47])
#위치번호로 조회
print(s.iloc[3])

#처음부터 3인덱스까지, 3포함
print(s.loc[:3])
print()

#0부터 3 앞까지, 3 미포함
print(s.iloc[:3])
print()

print('df:\n',df)
print()

#데이터프레임의 loc
print(df.loc['two'])
print(type(df.loc['two']))
print()
print(df.loc[['two']])
print(type(df.loc[['two']]))
print(df.iloc[[1,3]])
print()

#loc으로 원하는 데이터만 출력
print(df.loc[['two','three'],['서울','광주']])
#        서울  광주
# two     4   6
# three   8  10
print()

print('df:\n',df)
print()

#해당 칼럼에서 5보다 큰 것에 True
print(df['부산'] > 5)
print()

#해당 칼럼 중 조건에 맞는 것만 출력
print(df[df['부산'] > 5])
print()













