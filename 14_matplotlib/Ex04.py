'''
Created on 2023. 7. 20.

@author: user
'''
from matplotlib import font_manager
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from plotly.validators.layout.geo.projection import rotation

font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family = font_name)

#데이터프레임 생성
df = pd.DataFrame([[40,50,50],[70,50,50],[20,20,20]],
                  ['웬디','슬기','조이'],
                  ['국어','영어','수학'])
print('df:\n',df)
print()

#df.plot()

#인덱스와 칼럼 전치
#df = df.T
df = df.transpose()
print('df:\n',df)
print()

#막대그래프로 출력
#df.plot(kind='bar') 수직 막대그래프
df.plot.bar() #수직 막대그래프
#df.plot.barh() 수평 막대그래프
#df.plot.barh(stacked=True) #수평 막대그래프+막대가 합쳐서 나옴


#세로로 출력되는 항목 이름 가로로 회전
plt.xticks(rotation=0)

#파일 저장
filename = 'graph.png'
plt.savefig(filename)

plt.show()










