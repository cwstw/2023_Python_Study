'''
Created on 2023. 7. 19.

@author: user
'''
import pandas as pd
import numpy as np

col = ('이름','나이')
mydata = [('박세리',50),('강호동',30)]

df = pd.DataFrame(mydata,columns=col)
print('df:\n',df)
print()

#데이터프레임을 다른 파일에 저장
#mode='w' : 기존 꺼 지우고 생성
#mode='a' : 기존 꺼에 추가
#index=False : index 제외
filename = "result01.csv"
df.to_csv(filename,encoding='euc-kr',mode='w')
print(filename+"에 저장")

#파일을 데이터프레임으로 읽어오기
#index_col=0 : 0 번째 자리인 인덱스를 칼럼으로 인식하지 않음
df2 = pd.read_csv(filename,encoding='euc-kr',index_col=0)
print('df2:\n',df2)
print()


















