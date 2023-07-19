'''
Created on 2023. 7. 19.

@author: user
'''
import pandas as pd
import numpy as np

#DataFrame : 2차원 배열같은 자료구조, 행열 존재, 열 하나가 하나의 시리즈

arr = np.array([[1,2,3],[4,5,6]])
print('arr:\n',arr)
print(type(arr))
print(arr.ndim,arr.shape) #2 (2, 3)
print(arr[1][2])
print()

#이미 만들어진 배열로 데이터프레임 만들기
df = pd.DataFrame(arr)
print('df:\n',df)
#행과 열번호 자동 설정
# df:
#     0  1  2
# 0  1  2  3
# 1  4  5  6
print(type(df)) #pandas.core.frame.DataFrame
print(df.ndim,df.shape)
#데이터프레임의 요소를 출력할 때는 칼럼을 먼저 작성
#print(df[1][2])
print(df[2][1])
print()

#사전으로 데이터프레임 만들기
d = {'a':[1,3],'b':[1,2],'c':[2,4]}
df2 = pd.DataFrame(d)
print('df2:\n',df2)
# df2:
#     a  b  c
# 0  1  1  2
# 1  3  2  4
print(type(df2)) #pandas.core.frame.DataFrame
print()

#행과 열, 데이터를 지정하여 데이터프레임 생성
#data=,index=,columns= 생략가능
df3 = pd.DataFrame(data=[[4,5,6,7],[1,2,3,4]],
                   index=range(0,2),
                   columns=['A','B','C','D'])
print('df3:\n',df3)
# df3:
#     A  B  C  D
# 0  4  5  6  7
# 1  1  2  3  4
print()

#시리즈로 데이터프레임 생성
s1 = pd.Series([10,20,30,40])
print('s1:\n',s1)
s2 = pd.Series(['A','B','C','D'])
print('s2:\n',s2)
print()

df4 = pd.DataFrame([s1,s2])
print('df4:\n',df4)
# df4:
#      0   1   2   3
# 0  10  20  30  40
# 1   A   B   C   D
print(df4.ndim,df4.shape) #2 (2, 4)
print()





df5 = pd.DataFrame(data=[['서울','베이징','싱가포르','하노이'],[1232323,2243434,3454544,4233232]],
                   index=['capital','population'],
                   columns=['Korea','China','Singapore','Vietnam'])
print('df5:\n',df5)
print()

#사전 안에 사전을 넣어서 데이터프레임 생성
d = {'Korea':{'capital':'서울','population':23232332}, 'China':{'capital':'베이징','population':3434345}, 'Singapore':{'capital':'싱가포르','population':3465474}, 'Vietnam':{'capital':'하노이','population':34234234}}

df5 = pd.DataFrame(d)
print('df5:\n',df5)
# df5:
#                 Korea    China Singapore   Vietnam
# capital           서울      베이징      싱가포르       하노이
# population  23232332  3434345   3465474  34234234
print()







